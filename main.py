def main():

    # Image
    IMAGE_HEIGHT = 256
    IMAGE_WIDTH = 256

    # Render
    print("P3\n", IMAGE_WIDTH, ' ', IMAGE_HEIGHT, "\n255\n")

    for j in range(IMAGE_HEIGHT-1, -1, -1):
        for i in range(IMAGE_WIDTH):
            r = float(i) / (IMAGE_WIDTH - 1)
            g = float(j) / (IMAGE_HEIGHT - 1)
            b = 0.25

            ir = int(255.999 * r)
            ig = int(255.999 * g)
            ib = int(255.999 * b)

            print(ir, ' ', ig, ' ', ib, '\n')

main()
