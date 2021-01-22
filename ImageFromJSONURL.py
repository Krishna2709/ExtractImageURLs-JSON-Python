# Extract the image URL from JSON file and save the image in a folder

# 1. Import required packages
import json
import pandas as pd
import numpy as np

import urllib
from PIL import Image

# 2. Read the data
path_to_json = 'num_plates.json'
data = pd.read_json(path_to_json, lines=True)
pd.set_option('display.max_colwidth', -1)

print(data.head())

# Since we need urls
data = data['content']

print(data.head())

# 3. Extracting the images from the urls and saving them into a folder
for index, row in data.iterrows():
    # Get the image from the URL
    resp = urllib.request.urlopen(row[0])
    im = Image.open(resp)
    # Converting if any 'RGBA' image to 'RGB' image
    im = im.convert('RGB')
    im.save('data/image'+str(index)+'.jpg')