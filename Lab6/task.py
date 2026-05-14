from PIL import Image

def task(target_color):
    def pixel_generator(image_path):
        with Image.open(image_path) as img:
            rgb_img = img.convert('RGB')
            width, height = rgb_img.size
            for y in range(height):
                for x in range(width):
                    yield (x, y), rgb_img.getpixel((x, y))
    
    found = False
    for (x, y), color in pixel_generator('picture.jpg'):
        if color == target_color:
            print(f"Цвет {target_color} найден в координатах: x={x}, y={y}")
            found = True
            break
    if not found:
        print("Такого цвета в изображении нет")

    return found