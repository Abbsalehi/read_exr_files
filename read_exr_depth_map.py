import os
import OpenEXR
import numpy as np

def read_exr(file_path):
    exr_file = OpenEXR.InputFile(file_path)
    header = exr_file.header()
    dw = header['dataWindow']
    width = dw.max.x - dw.min.x + 1
    height = dw.max.y - dw.min.y + 1

    # Get all channel names
    channels = exr_file.header()['channels'].keys()

    # Read the pixel data for each channel
    rgb_data = {}
    for channel in channels:
        rgb_data[channel] = np.frombuffer(exr_file.channel(channel), dtype=np.float32)

    # Reshape the data
    for channel in channels:
        rgb_data[channel] = np.reshape(rgb_data[channel], (height, width))

    return rgb_data


base_dir= 'your local directory path'
PATH_TO_EXR_FILE= os.path.join(base_dir,'data0/0/d0.exr' )

image_data = read_exr(PATH_TO_EXR_FILE)

# Access channels: here is just Z channel; you may have more channels
#use image_data.keys() to see the channels names

data = image_data['Z']
#print(data.shape)
