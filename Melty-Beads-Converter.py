# Importing Image class from PIL module
from PIL import Image
 
# Opens a image in RGB mode
image = Image.open(r"Lenna_(test_image).png")
 
# Size of the image in pixels (size of original image)
width, height = image.size

pad_size = int(input("Enter the size of your pad: "))
 
# Resize image
newsize = (pad_size, pad_size)
image_small = image.resize(newsize)
output_image_lines = Image.new('RGB',((pad_size*10),(pad_size*10)),"rgb(0,0,0)")

input_x = 0
input_y = 0

while input_x < image_small.width * 10:
    while input_y < image_small.height * 10:
        output_image_lines.putpixel((input_x, input_y),image_small.getpixel((input_x / 10, input_y / 10)))
        if input_y % 10 == 0:
            output_image_lines.putpixel((input_x, input_y),(0,0,0))
            input_y = input_y + 1
        else:
            input_y = input_y + 1
    input_y = 0
    if input_x % 10 == 0:
        for i in range(image_small.height * 10):
            output_image_lines.putpixel((input_x, i),(0,0,0))
        input_x = input_x + 1
    else:
        input_x = input_x + 1
        
# Shows the image in image viewer
output_image_lines.show()