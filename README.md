## ASCII Image Renderer
A simple command line tools to render the ASCII art of a given image.

```bash
usage: main.py [-h] [-c COVERAGE] image

Renders an image as ASCII art

positional arguments:
  image                 Path to the image

optional arguments:
  -h, --help                         show this help message and exit
  -c COVERAGE, --coverage COVERAGE   how much terminal space the image takes, the higher the clearer
```

### Result
![example](/assets/example.jpg)
<br/>
![example-ascii](/assets/example-ascii.png)

It simply maps each pixel's brightness to a character within `.'^",:;Il!i><~+_-?][}{1)(|\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$` (darkest to lightest) and renders it as ASCII art.

![zoomed](/assets/zoomed.png)