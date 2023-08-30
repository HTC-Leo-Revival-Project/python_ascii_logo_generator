from PIL import Image, ImageDraw, ImageFont
import pyfiglet
import argparse

# Parse command-line arguments
parser = argparse.ArgumentParser(description="Generate ASCII art image.")
parser.add_argument("--res", type=str, help="Image resolution (widthxheight)")
parser.add_argument("--font", type=str, help="FIGlet font name")
parser.add_argument("--output", type=str, help="Output filename")
parser.add_argument("message", type=str, help="Text message for ASCII art")
args = parser.parse_args()

# Process resolution argument
image_width, image_height = map(int, args.res.split('x'))
image_size = (image_width, image_height)

# Settings
output_filename = args.output
font_name = args.font

# Generate ASCII art text
font = pyfiglet.Figlet(font=font_name)
ascii_text = font.renderText(args.message)

# Create a new image with a black background
image = Image.new("RGB", image_size, (0, 0, 0))
draw = ImageDraw.Draw(image)

# Load a font
font_path = "FreeMono.ttf"  # Replace with the path to a TrueType font file
font_size = 8  # Initial font size decreased by 2
font = ImageFont.truetype(font_path, font_size)

# Calculate dimensions of the text
text_width, text_height = draw.textsize(ascii_text, font=font)

# Calculate text position to center it in the image
x = (image_size[0] - text_width) // 2
y = (image_size[1] - text_height) // 2

# Draw white ASCII art on the black background
for line in ascii_text.split('\n'):
    line_width, line_height = draw.textsize(line, font=font)
    
    # Adjust x position based on the individual line's width
    line_x = x + (text_width - line_width) // 2
    
    draw.text((line_x, y), line, font=font, fill=(255, 255, 255))
    y += line_height

# Save the image as BMP
image.save(output_filename)

print(f"Image saved as {output_filename}")
