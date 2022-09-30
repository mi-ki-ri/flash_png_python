from types import NoneType
import cv2
import math
import random
import sys
import os

def setEffect(pic, center=(0.5, 0.5)):
    he, wi = pic.shape[:2]
    leng = math.sqrt(he ** 2 + wi ** 2)

    for rd in range(360):
        k = rd * math.pi/180
        r = random.uniform(0.15, 0.50)  # min, max の乱数

        x = wi * center[0] + r * leng * math.cos(k)
        y = he * center[1] + r * leng * math.sin(k)
        dx = wi * center[0] + leng * math.cos(k)
        dy = he * center[1] + leng * math.sin(k)

        if random.uniform(0, 1) > 0.66:
            cv2.line(pic, (int(x), int(y)), (int(dx), int(dy)), (0, 0, 0), 1)


def main():
    args = sys.argv
    if len(args) == 1:
        return

    file = args[1]
    if not os.path.exists(file):
        return

    img = cv2.imread(file)
    if type( img ) == NoneType:
        return

    setEffect(img)
    cv2.imwrite(f"{file}_add.png", img)


if __name__ == "__main__":
    main()
