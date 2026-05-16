from PIL import Image

def pixel_generator(image_path):
    with Image.open(image_path) as img:
        rgb_img = img.convert('RGB')
        width, height = rgb_img.size
        for y in range(height):
            for x in range(width):
                yield (x, y), rgb_img.getpixel((x, y))

def find_color_in_image(target_color):
    found = False
    for (x, y), color in pixel_generator('D:/Prog/Lab7/picture.jpg'):
        if color == target_color:
            found = f"Цвет {target_color}\nнайден в координатах:\nx={x}, y={y}"
            print(found)
            break
    if not found:
        found = "Такого цвета в изображении нет"
        print(found)
    return found