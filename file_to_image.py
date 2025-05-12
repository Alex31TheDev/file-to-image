from PIL import Image, ImageDraw
import sys
import os
import math

def open_file(path):
    file = open(path, 'rb')
    file.seek(0, os.SEEK_END)

    size = file.tell()
    file.seek(0)

    return file, size

def calculate_width(size, color):
    channels = 1 if color == 0 else 3
    pixels = math.ceil(size / channels)

    return math.ceil(math.sqrt(pixels))

def process_file(file, draw, width, color):
    for i in range(width * width):
        data = file.read(1 if color == 0 else 3)

        if not data:
            break

        if color == 1 and len(data) < 3:
            data += b"\x00" * (3 - len(data))

        if color == 0:
            gray = data[0]
            R = G = B = gray
        else:
            R, G, B = data

        x = i % width
        y = i // width

        draw.point((x, y), fill=(R, G, B))

def file_to_image(color, in_path, out_path):
    file, size = open_file(in_path)
    width = calculate_width(size, color)

    img = Image.new('RGBA', (width, width))
    draw = ImageDraw.Draw(img)

    process_file(file, draw, width, color)

    file.close()
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
