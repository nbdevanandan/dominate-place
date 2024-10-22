import cv2
import json
import argparse

# the maximum no of pixels they accept in one go
max_size = 5

# canvas.png can be replaced with any image of your liking as long as it's
# within the original canvas' dimensions; which for us is 180, 50
image = cv2.imread('canvas.png')

# shape -- (height, width, 3) of image
# 3 to indicate R, G, B
shape = image.shape

####
####
image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)

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

