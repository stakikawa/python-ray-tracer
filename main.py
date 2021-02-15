from color import Color

def main():

    # Image
    IMAGE_HEIGHT = 256
    IMAGE_WIDTH = 256

    # Render
    print("P3\n", IMAGE_WIDTH, ' ', IMAGE_HEIGHT, "\n255\n")

    for j in range(IMAGE_HEIGHT-1, -1, -1):
        for i in range(IMAGE_WIDTH):
            pixel_color = Color(float(i)/(IMAGE_WIDTH-1), float(j)/(IMAGE_HEIGHT-1), 0.25)
            Color.write_color(pixel_color)
main()
