from PIL import Image, ImageDraw, ImageFont
import pyfiglet
import argparse
import random

# Parse command-line arguments
parser = argparse.ArgumentParser(description="Generate ASCII art image.")
parser.add_argument("--res", type=str, help="Image resolution (widthxheight)")
parser.add_argument("--font", type=str, help="FIGlet font name")
parser.add_argument("--fontsize", type=int, help="Font size")
parser.add_argument("--color", action="store_true", help="Randomly color the text with gradients")
parser.add_argument("--output", type=str, help="Output filename")
parser.add_argument("message", type=str, help="Text message for ASCII art")
args = parser.parse_args()

# Process resolution argument
image_width, image_height = map(int, args.res.split('x'))
image_size = (image_width, image_height)

# Settings
output_filename = args.output
font_name = args.font
font_size = args.fontsize

# Generate ASCII art text
font = pyfiglet.Figlet(font=font_name)
ascii_text = font.renderText(args.message)

# Calculate font size based on image resolution if not provided
if font_size is None:
    font_size = min(image_width // len(ascii_text.split('\n')[0]), image_height // len(ascii_text.split('\n')))

# Create a new image with a black background
image = Image.new("RGB", image_size, (0, 0, 0))
draw = ImageDraw.Draw(image)

# Load a font
font_path = "FreeMono.ttf"  # Replace with the path to a TrueType font file
font = ImageFont.truetype(font_path, font_size)

# Calculate dimensions of the text
text_width, text_height = draw.textsize(ascii_text, font=font)

# Calculate text position to center it in the image
x = (image_size[0] - text_width) // 2
y = (image_size[1] - text_height) // 2

# Draw white ASCII art on the black background

# Adjust x position based on the maximum width of each line
max_line_width = max(draw.textsize(line, font=font)[0] for line in ascii_text.split('\n'))
x = (image_size[0] - max_line_width) // 2

if args.color:
    colors = [tuple(random.randint(0, 255) for _ in range(3)) for _ in range(len(ascii_text.split('\n')))]
    for line, color in zip(ascii_text.split('\n'), colors):
        line_width, line_height = draw.textsize(line, font=font)
        line_x = x + (max_line_width - line_width) // 2
        char_x = line_x  # Initialize char_x for each line
        for char in line:
            char_width = draw.textsize(char, font=font)[0]
            char_y = y + (line_height - font.getsize(char)[1]) // 2
            draw.text((char_x, char_y), char, font=font, fill=color)
            char_x += char_width  # Move char_x by char_width for the next character
        y += line_height
else:
    for line in ascii_text.split('\n'):
       line_width, line_height = draw.textsize(line, font=font)
    
       # Adjust x position based on the maximum width of each line
       line_x = x + (max_line_width - line_width) // 2
    
       draw.text((line_x, y), line, font=font, fill=(255, 255, 255))
       y += line_height


# Save the image as BMP
image.save(output_filename)

print(f"Image saved as {output_filename}")
