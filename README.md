# Sprite Sheet Generator
Generation of sprite sheets from a sequence of image files.
It creates a single file merged with specified columns and rows, from right to bottom direction

## How to setup

``pip install -r requirements.txt``

## Usage
```
usage: python main.py [-h] -i FILES -e EXTENSION -d DIGITS -c COLUMNS -r ROWS [-cc COLORCHANNELS] output_filename

From a sequence of image files, it creates a single file merged with specified columns and rows, from right to bottom direction

positional arguments:
  output_filename       The output filename with ou without sequence of folders, including file extension

options:

  -h, --help            show this help message and exit

  -i FILES, --files FILES
                        The input files (can have folder and path) without the numbers and without extension. It is expected to start from zero. Ex: ./folder/file_000.png, should put ./folder/file_

  -e EXTENSION, --extension EXTENSION
                        The extension of the input files, without de dot(.)

  -d DIGITS, --digits DIGITS
                        The total of digits of numbers to be filled with zeros

  -c COLUMNS, --columns COLUMNS
                        The number of columns generated in the output file. The count (colums X rows) have to match the total of files.

  -r ROWS, --rows ROWS  The number of rows generated in the output file. The count (colums X rows) have to match the total of files.

  -cc COLORCHANNELS, --colorchannels COLORCHANNELS
                        The number of color channels the input files have. Usually 4 with alpha channels in PNG
```

## Example

For creating a file named sprite1.png from a 5x12 sprite sheet from PNGs files like /Users/PNGs/splash_00000.png

```python sprite_gen.py -i /Users/PNGs/splash_ -e png -d 5 -c 5 -r 12 sprite1.png```
                        
