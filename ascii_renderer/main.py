from PIL import Image
import os, argparse


PIXELS = ".'`^\",:;Il!i><~+_-?][}{1)(|\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

TERMINAL_WIDTH = os.get_terminal_size().columns
PIXEL_WIDTH_MULTIPLIER = 2


def arg_parser():
    parser = argparse.ArgumentParser(description="Renders an image as ASCII art")
    parser.add_argument("image", type=str, help="Path to the image")
    parser.add_argument(
        "-c",
        "--coverage",
        type=float,
        default=0.8,
        help="how much terminal space the image takes, the higher the clearer",
    )
    return parser.parse_args()


def main():
    args = arg_parser()
    image_path = args.image
    coverage = args.coverage

    if coverage > 1 or coverage < 0:
        print("coverage must be between 0 and 1")
        return

    img = Image.open(image_path).convert("RGB")
    width, height = img.size
    image_ratio = width / height

    # ensure rendered image is not wider than terminal width
    resized_width = int(TERMINAL_WIDTH * coverage * 1 / PIXEL_WIDTH_MULTIPLIER)
    if width > resized_width:
        img = img.resize((resized_width, int(resized_width / image_ratio)))

        width, height = img.size

    pixels = img.load()
    pixel_art = ""
    for y in range(height):
        for x in range(width):
            R, G, B = pixels[x, y]
            # calculating greyscale value (Average method)
            brightness = (R + G + B) // 3
            pixel_index = int(((brightness) / 255) * len(PIXELS))
            # making sure the pixel index is within the range of PIXELS
            pixel_index = min(pixel_index, len(PIXELS) - 1)
            # increase pixel (width) to accomodate for the font-size/line-height
            pixel_art += PIXELS[pixel_index] * PIXEL_WIDTH_MULTIPLIER
        # render each line
        pixel_art += "\n"
    print(pixel_art)


if __name__ == "__main__":
    main()
