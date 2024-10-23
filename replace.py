import cv2
import json
import os
import argparse

# this python script will accept arguments because it should know which 
# 5 pixels to make into a json file; for that the bash script should pass
# the current x, y coords to this fie
parser = argparse.ArgumentParser(description="Get the current coordinates")
parser.add_argument('x', type=int, help='X coords')
parser.add_argument('y', type=int, help='Y coords')
args = parser.parse_args()

# the maximum no of pixels they accept in one go
max_size = 5

# canvas.png can be replaced with any image of your liking as long as it's
# within the original canvas' dimensions; which for us is 180, 50
image_bgr = cv2.imread('canvas.png')
image = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)

# Function to convert RGB to Hex
def rgb_to_hex(rgb):
    return "#{:02x}{:02x}{:02x}".format(rgb[0], rgb[1], rgb[2])

def read_data(x=args.x, y=args.y):
    x_values = []
    y_values = [y] * max_size
    rgb_values = []
    for xi in range(x,x+max_size+1):
        x_values.append(xi)
        rgb_values.append(image[y,xi].tolist())

    return (x_values, y_values, rgb_values)

x_values, y_values, rgb_values = read_data()

# function to create data based on dynamic input
def generate_data(x_values, y_values, rgb_values):
    data = []
    for x, y, rgb in zip(x_values, y_values, rgb_values):
        data.append({
            "x": str(x),
            "y": str(y),
            "rgb": rgb_to_hex(rgb)
        })
    return data

data = generate_data(x_values, y_values, rgb_values)

# json file to edit
home_directory = os.path.expanduser("~")
json_file = os.path.join(home_directory, 'amPlace_contribution', 'pixel_update.json')

# Write the data to a JSON file
with open(json_file, 'w') as json_file:
    json.dump(data, json_file, indent=2)
    
print("suces")

