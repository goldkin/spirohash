## Human-readable hashing for images

Spirohash provides a human-readable, color-agnostic hash for images, providing a signature from an image itself. This signature follows the [Golden Ratio](https://en.wikipedia.org/wiki/Golden_ratio) and [Rule of Thirds](https://en.wikipedia.org/wiki/Rule_of_thirds), allowing artists to prove their ownership of a work and provide attribution to search engines using the same method the human eye uses to process an image.

This library traces a spiral around the subject of an image, computing the ratio of its most common colors (in selectable, but typically 16-bit, colorspace). This ratio, calculated from the subject of the image itself, can be then used to assist search engines and prove original ownership when provided at the same time an image is published.

While useful, this approach has some limitations. Most notably, this can only be applied to a work itself; stolen _designs_, _remixes_, and _derivative works_ cannot be detected by this tool, nor are they protected by law in many jurisdictions. The sole purpose of this tool is to aid the discovery of and reconciliation of routine art theft, including publication of a complete original work without attribution.

## Code Example

TODO

## Motivation

One of the biggest open problems for professional artists is theft of their original works by content aggregators and sales organizations that fail to do due diligence. This tool aims to provide a _framework_ to handle those cases, by making it easier to provide and search for the original attribution of an image through attempts to mask or obfuscate the original work.

Because this relies on subject selection and the aesthetic properties of the human eye, this makes art theft substantially more challenging without degrading the subject of an image or dramatically altering its content.

## Installation

Simply install [Python](https://www.python.org/), [ImageMagick](https://www.imagemagick.org/script/index.php), [PythonMagick](https://wiki.python.org/moin/ImageMagick), and clone this repository. See the code example above for how to run the tool.

## Contributing

To contribute to this project, please provide pull requests and issues as with any other Github project. This project is done in my free time; issues and pull requests will be reconciled as often as I am able to digest them.

## License

See LICENSE in the repository itself for more info.
