
# coding: utf-8

# In[1]:

import sys, os, multiprocessing, csv
from urllib import request, error
from PIL import Image
from io import BytesIO

data_file = "C:\\R_Lang\\Hackathons\\Kaggle\\Google Landmark Recognition Challenge\\test.csv\\test.csv"
#out_dir =  "C:\\R_Lang\Hackathons\\Kaggle\\Google Landmark Recognition Challenge\\train.csv\\train_im\\"
out_dir =  "E:\\Nitin\\ML\\Google Landmark Recognition Challenge\\Test_Data\\"

# In[2]:

#!/usr/bin/python

# Note to Kagglers: This script will not run directly in Kaggle kernels. You
# need to download it and run it on your local machine.

# Downloads images from the Google Landmarks dataset using multiple threads.
# Images that already exist will not be downloaded again, so the script can
# resume a partially completed download. All images will be saved in the JPG
# format with 90% compression quality.



def download_image(key_url):
    #out_dir = sys.argv[2]
    (key, url) = key_url
    filename = os.path.join(out_dir, '{}.jpg'.format(key))

    if os.path.exists(filename):
        print('Image {} already exists. Skipping download.'.format(filename))
        return

    try:
        response = request.urlopen(url)
        image_data = response.read()
    except:
        print('Warning: Could not download image {} from {}'.format(key, url))
        return

    try:
        pil_image = Image.open(BytesIO(image_data))
    except:
        print('Warning: Failed to parse image {}'.format(key))
        return

    try:
        pil_image_rgb = pil_image.convert('RGB')
    except:
        print('Warning: Failed to convert image {} to RGB'.format(key))
        return

    try:
        pil_image_rgb.save(filename, format='JPEG', quality=90)
    except:
        print('Warning: Failed to save image {}'.format(filename))
        return



# In[3]:

def parse_data(data_file):
    csvfile = open(data_file, 'r')
    csvreader = csv.reader(csvfile)
    key_url_list = [line[:2] for line in csvreader]
    return key_url_list[1:]  # Chop off header


# In[4]:

def loader():

    key_url_list = parse_data(data_file)
    pool = multiprocessing.Pool(processes=4)  # Num of CPUs
    pool.map(download_image, key_url_list)
    pool.close()
    pool.terminate()


# In[ ]:



