## Spirohash: human-readable hashing for images

Spirohash provides a human-readable, color-agnostic hash for images, providing a signature from an image itself. This signature follows the [Golden Ratio](https://en.wikipedia.org/wiki/Golden_ratio) and [Rule of Thirds](https://en.wikipedia.org/wiki/Rule_of_thirds), describing the spiral followed by the human eye in a format useful to search engines.

This library samples pixels from a Golden Ratio spiral traced around an image, computing a hash based on the most common colors encountered. When placed on the subject of the image itself, this can be used to assist search engines by providing metadata about what the human eye sees. Generating a hash and placing it with your work can also identify you as its original owner, should someone search for a same or similar hash in Google.

Thus, this tool seeks to aid the attribution of an original image, by helping artists provide both search metadata and unambiguous proof of ownership. This library does _not_ replace the function of copyright, nor does it act as a watermark.

This hash is also designed to be resilient to common attempts to obscure attribution. This means tolerating imprecision when an image is cropped, flipped, rotated, or when its colors are altered.

This hash _will_ fail if color values are radically altered, noise is injected to the image itself, or the subject of the image is itself changed. Stolen _designs_, _remixes_, and _derivative works_ cannot be detected by this tool. The sole purpose of this tool is instead to aid the discovery of and reconciliation of routine art theft, including detecting publication of a complete original work without attribution.

## Sample Usage

Currently, this tool has no fancy frontend and must be run from the command line. It is invoked with two args: the image file to process, and the quadrant where the subject can be found (1 through 4). Any rectangular image format supported by [PIL](http://www.pythonware.com/products/pil/) is supported by this tool.

```
$ python spirohash.py my_test_image.jpg 1
This image's hash is SPRO261B19171312100F0D
```

## Motivation

One of the biggest open problems for professional artists is theft of their original works by content aggregators and sales organizations that fail to do due diligence. This tool aims to provide a _framework_ to handle those cases, by making it easier to provide and search for the original attribution of an image through attempts to mask or obfuscate the original work.

Because this relies on subject selection and the aesthetic properties of the human eye, this makes art theft substantially more challenging without degrading the subject of an image or dramatically altering its content.

## Installation

Simply install [Python](https://www.python.org/), [PIL](http://www.pythonware.com/products/pil/), and clone this repository. See sample usage above for how to run the tool.

## Contributing

To contribute to this project, please provide pull requests and issues as with any other Github project. This project is done in my free time; issues and pull requests will be reconciled as often as I am able to digest them.

## License

See LICENSE in the repository itself for more info.
