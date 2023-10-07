from PIL import Image
import sys

image = Image.open(sys.argv[1])
pixels = image.getdata()

file = open(sys.argv[2], 'wb')

i = 0
for pixel in pixels:
    R = pixel[0]
    G = pixel[1]
    B = pixel[2]
    A = pixel[3]

    if A != 255:
        break

    file.write(R.to_bytes(1, 'little'))
    file.write(G.to_bytes(1, 'little'))
    file.write(B.to_bytes(1, 'little'))
    i += 1

print(i)
file.close()
