from PIL import Image
import sys

def process_pixels(image, out_file, color):
    for pixel in image.getdata():
        R = pixel[0]
        G = pixel[1]
        B = pixel[2]
    
        A = pixel[3] if len(pixel) > 3 else 255
        if A != 255:
            break

        if color == 0:
            out_file.write(R.to_bytes(1, 'little'))
            out_file.write(G.to_bytes(1, 'little'))
            out_file.write(B.to_bytes(1, 'little'))
        else:
            out_file.write(R.to_bytes(1, 'little'))

def image_to_file(color, in_path, out_path):
    img = Image.open(in_path)
    out_file = open(out_path, 'wb')

    process_pixels(img, out_file, color)
    out_file.close()

usage = 'Usage: python image_to_file.py <color> <input path> <output path>'

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

    image_to_file(mode, in_path, out_path)

if __name__ == '__main__':
    main()
