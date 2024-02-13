# ASCII Art Image Generator

This script generates an ASCII art image from a text message using the pyfiglet library and saves it as a BMP image. The generated image is centered within the specified dimensions.

## Prerequisites

Before running the script, ensure you have the following:

- Python 3.x installed
- Required Python packages: Pillow (PIL), pyfiglet

You can install the required packages using the following command:

pip install -r requirements.txt

## Usage

Edit the figlet font name you wanna use and change the res and the text to your desired values then run:

<pre>
```bash
python3 ascii_art_generator.py --res 400x800 --font block --output output_image.bmp "HTC LEO REVIVAL PROJECT"
```
</pre>

## Pictures

![HtcLeo Revival Project Splash](https://i.imgur.com/5E1QZis.png)
![Default figlet font](https://i.imgur.com/YFSyiVI.png)
