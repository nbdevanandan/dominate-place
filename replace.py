import cv2
import json
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
image = cv2.imread('canvas.png')

def read_data(args.x, args.y):
    #image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)
    return (x, y, rgb)


# function to create data based on dynamic input
def generate_data(x_values, y_values, rgb_values):
    data = []
    for x, y, rgb in zip(x_values, y_values, rgb_values):
        data.append({
            "x": str(x),
            "y": str(y),
            "rgb": rgb
        })
    return data

# the json file we need to edit:
json_file = ''

# Write the data to a JSON file
with open(json_file, 'w') as json_file:
    json.dump(data, json_file, indent=2)

