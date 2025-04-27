from PIL import Image, ImageDraw
import sys
import math

def open_file(path):
    f = open(path, 'rb')
    f.seek(0, 2)

    size = f.tell()
    f.seek(0)

    return f, size

def calculate_width(size, color):
    channels = 3 if color == 0 else 1
    pixels = math.ceil(size / channels)

    return math.ceil(math.sqrt(pixels))

def process_file(file, draw, width, color):
    i = 0

    while True:
        b1 = file.read(1)

        if not b1:
            break

        R = int.from_bytes(b1, 'little')

        if color == 0:
            b2 = file.read(1) or b"\x00"
            b3 = file.read(1) or b"\x00"

            G = int.from_bytes(b2, 'little')
            B = int.from_bytes(b3, 'little')
        else:
            G = B = R

        x = i % width
        y = i // width

        draw.point((x, y), fill=(R, G, B))
        i += 1

def file_to_image(color, in_path, out_path):
    f, size = open_file(in_path)
    width = calculate_width(size, color)

    img = Image.new('RGBA', (width, width))
    draw = ImageDraw.Draw(img)

    process_file(f, draw, width, color)

    f.close()
    img.save(out_path)

usage = 'Usage: python file_to_image.py <color> <input path> <output path>'

def print_usage():
    print(usage)
    sys.exit(1)

def main():
    args = sys.argv[1:]

    if len(args) != 3:
        print_usage()

    try:
        mode = int(args[0])
    except ValueError:
        print_usage()

    if mode not in (0, 1):
        print_usage()

    in_path = args[1]
    out_path = args[2]

    file_to_image(mode, in_path, out_path)

if __name__ == '__main__':
    main()
