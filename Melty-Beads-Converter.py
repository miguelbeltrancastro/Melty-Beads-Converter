# Importing Image class from PIL module
from PIL import Image
 
def Pixelate_image(image,pad_size):
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
    return output_image_lines

Perler_colors = {
    'White':(255,255,255),
    'Ghost White':(239,239,239),
    'Light Gray':(211,211,203),
    'Gray':(152,153,153),
    'Pewter':(149,156,152),
    'Dark Grey':(118,119,119),
    'Charcoal':(75,82,81),
    'Dark Gray':(71,69,69),
    'Mineshaft':(35,40,43),
    'Black':(26,19,17),
    'Toasted Marshmallow':(253,234,219),
    'Sand':(246,204,153),
    'Pale Skin':(218,182,152),
    'Fawn':(215,176,135),
    'Tan':(200,157,117),
    'Sienna':(184,97,37),
    'Rust':(146,51,34),
    'Cranapple':(139,43,60),
    'Red Wine':(66,3,26),
    'beeswax':(255,231,128),
    'Dandilion':(222,185,71),
    'marigold':(180,126,0),
    'Light Brown':(158,113,75),
    'Brown':(82,53,41),
    'Cream':(222,222,159),
    'Pastel Yellow':(240,233,148),
    'canary':(243,234,93),
    'Yellow':(246,230,55),
    'corn':(255,199,44),
    'Cheddar':(252,179,57),
    'Orange':(247,144,38),
    'Butterscotch':(228,136,78),
    'Blaze Orange':(244,99,58),
    'Hot Coral':(235,91,72),
    'Flamingo':(242,130,112),
    'Blush':(245,137,120),
    'Salmon':(246,196,193),
    'Peach':(234,191,181),
    'Deep Chesnut':(170,87,97),
    'Light Pink':(234,185,211),
    'Carnation Pink ':(241,167,220),
    'Bubble Gum':(236,137,183),
    'Pink':(234,78,152),
    'Magenta':(232,57,128),
    'Red':(204,34,40),
    'Cherry':(172,37,52),
    'Paprika':(165,0,52),
    'Bloodrose Red':(81,9,24),
    'Burgundy':(171,37,86),
    'Raspberry':(189,24,96),
    'Mulberry Wood':(114,25,95),
    'Plum':(184,89,160),
    'Maverick':(197,180,227),
    'Light Lavender':(198,170,206),
    'lavender':(167,123,202),
    'Pastel Lavender':(160,119,179),
    'Purple':(116,59,151),
    'royal purple':(100,53,155),
    'purple':(51,0,114),
    'Robins Egg':(215,239,250),
    'sky blue':(170,220,235),
    'Clear Blue':(124,210,242),
    'Pastel Blue':(112,166,208),
    'Light Blue':(80,150,208),
    'true blue':(20,123,209),
    'Cobalt':(15,82,164),
    'Dark Blue':(43,48,124),
    'Midnight':(22,40,70),
    'black rock':(5,8,73),
    'Toothpaste':(179,226,233),
    'light blue':(0,144,218),
    'Turquoise':(0,143,204),
    'Light Green':(84,193,172),
    'Medium Turquoise':(0,178,169),
    'Parrot Green':(0,153,146),
    'Green tea/pea':(0,124,88),
    'dark green':(0,104,94),
    'Pistachio':(173,220,145),
    'Pastel Green':(172,211,120),
    'Kiwi Lime':(136,195,65),
    'Bright Green':(111,192,96),
    'Green':(36,158,107),
    'Shamrock':(0,153,73),
    'Dark Green':(33,90,50),
    'Prickly Pear':(215,224,65),
    'Dark Olive':(153,155,48),
    'cafe latte':(118,108,43),
    'Sage Green':(78,88,44),
    'Evergreen':(47,68,46),
    'Brunswick green':(24,48,40),
    'sea mist':(158,229,176),
    'Celadon Green':(86,154,131),
    'Neon Green':(1,158,67),
    'Neon Yellow':(220,224,2),
    'Neon Pink':(255,57,145),
    'Neon Orange':(255,119,0),
    'Silver':(119,123,129),
    'Gold':(187,118,52),
    'Copper':(154,85,22),
    'Pearl Light Pink':(215,168,162),
    'Pearl Coral':(249,126,121),
    'Pearl Yellow':(202,192,51),
    'Pearl Green':(132,183,145),
    'Pearl Light Blue':(122,174,162),
    'Fairy Dust':(169,213,162),
    'Glow Green':(190,198,150),
}

# Opens a image in RGB mode
image = Image.open(r"Lenna_(test_image).png")

pad_size = int(input("Enter the size of your pad: "))

output_image_lines = Pixelate_image(image,pad_size)

# Shows the image in image viewer
output_image_lines.show()