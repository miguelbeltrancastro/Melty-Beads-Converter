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
output_image = Image.new('RGB',(pad_size*2,pad_size*2),"rgb(0,0,0)")

for input_x in range(image_small.width):
    for input_y in range(image_small.height):
        output_image.putpixel((input_x, input_y),image_small.getpixel((input_x, input_y)))
# Shows the image in image viewer
output_image.show()