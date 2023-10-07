from PIL import Image, ImageDraw
import sys
import math

f = open(sys.argv[2], "rb")
f.seek(0, 2)

if sys.argv[1] == "0":
    w = math.ceil(math.sqrt(f.tell() / 3))
else:
    w = math.ceil(math.sqrt(f.tell()))

img = Image.new("RGBA", (w, w))
draw = ImageDraw.Draw(img)
f.seek(0, 0)

i = 0
while True:
    b1 = f.read(1)
    if sys.argv[1] == "0":
        b2 = f.read(1)
        b3 = f.read(1)

    if not b1:
         break

    R = int.from_bytes(b1, 'little')
    if sys.argv[1] == "0":
        G = int.from_bytes(b2, 'little')
        B = int.from_bytes(b3, 'little')
    else:
        G = B = R

    draw.point((i%w, i/w), fill = (R, G, B))

    i += 1

f.close()
img.save(sys.argv[3])