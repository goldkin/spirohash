import argparse
import sys
from collections import defaultdict
from math import cos, sin, sqrt
from operator import itemgetter
from PIL import Image


GOLDEN_RATIO = 1.61803398875 # Mathematical constant
HASH_LENGTH = 9              # Number of color bins to count in the output hash
MAX_NUMBER_OF_BINS = 16      # Number of color bins for hashing
SAMPLES_PER_ROTATION = 360   # Must be int, ideally divisible by four
SHRINK_ITERATIONS = 10       # How many iterations to shrink the golden ratio "spiral" to start with
SPIRAL_APPROXIMATION = GOLDEN_RATIO * 4 / SAMPLES_PER_ROTATION
                             # This variable *approximates* a golden ratio spiral uniformly, without changing the origin.


difference = lambda origin,current: [m - n for m, n in zip(origin, current)]
get_pythagorean = lambda x,y: sqrt(x*x + y*y)
get_c = lambda origin,current: get_pythagorean(*difference(origin, current))


def rotate_and_extrude(origin, current):
    s = sin(2.0 / SAMPLES_PER_ROTATION)
    c = cos(2.0 / SAMPLES_PER_ROTATION)
    marginal_extrusion = sqrt((SPIRAL_APPROXIMATION**2) / 2)
    diff = [n * (1 + marginal_extrusion) for n in difference(origin, current)]
    current[0] = origin[0] + (diff[0] * c - diff[1] * s)
    current[1] = origin[1] + (diff[0] * s + diff[1] * c)
    return current


def hash(args):
    image_to_hash = Image.open(args[0])
    quadrant = int(args[1])

    assert(image_to_hash)
    assert(quadrant >= 0)
    assert(quadrant <= 3)

    x_origin = int(image_to_hash.size[0] / 3) * 1 + (quadrant % 2)
    y_origin = int(image_to_hash.size[1] / 3) * 1 + ((2 - quadrant)**2 < 4)

    bins = defaultdict(int)
    current = [x_origin, y_origin]
    initial_offset = min(*image_to_hash.size) / (GOLDEN_RATIO ** SHRINK_ITERATIONS)
    origin = [x_origin, y_origin]
    step = 0

    current = [x_origin, int(y_origin + initial_offset + 1)]
    cutoff_diameter = max(get_c(origin, (0, 0)),
                          get_c(origin, (image_to_hash.size[0], 0)),
                          get_c(origin, (0, image_to_hash.size[1])),
                          get_c(origin, image_to_hash.size))

    image_data = image_to_hash.getdata()
    while get_c(origin, current) < cutoff_diameter:
        current = rotate_and_extrude(origin, current)
        if current[0] >= 0 and current[1] >= 0 and current[0] <= image_to_hash.size[0] and current[1] <= image_to_hash.size[1]:
            raw_color = image_data[int(current[0]) + (image_to_hash.size[0] * int(current[1]))]
            bins[tuple([c * MAX_NUMBER_OF_BINS / 256 for c in raw_color])] += 1

    output_hash = "SPRO"
    for _, count in sorted(bins.items(), key=itemgetter(1), reverse=True)[:HASH_LENGTH]:
        output_hash += "{0:02x}".format(count)

    print "This image's hash is %s" % output_hash.upper()


if __name__ != 'main':
    hash(sys.argv[1:])
