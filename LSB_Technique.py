import cv2
import numpy as np
import random

def binary_conversion(data):
    """Convert `data` to binary format as string"""
    if isinstance(data, str):
        return ''.join([format(ord(i), "08b") for i in data]) #"0101010101 001100100"
    elif isinstance(data, bytes) or isinstance(data, np.ndarray):
        return [format(i, "08b") for i in data] #[00010101 010101001 ]
    elif isinstance(data, int) or isinstance(data, np.uint8):
        return format(data, "08b") #010101001
    else:
        raise TypeError("Type not supported.")

def encode(image_name, code_message):
    # read the image
    image = cv2.imread(image_name)
    # maximum bytes to encode
    n_bytes = image.shape[0] * image.shape[1] * 3 // 8
    print("Maximum bytes to encode: ", n_bytes)
    if len(code_message) > n_bytes:
        raise ValueError("!!!!! Insufficient bytes. Use larger image or smaller data.")
    print("***Encoding data***")
    # add stopping criteria
    code_message += "====="
    data_index = 0
    # convert data to binary
    binary_code_message = binary_conversion(code_message)
    # size of data to hide
    data_len = len(binary_code_message)
    for row in image:
        for pixel in row:
            # convert RGB values to binary format
            r, g, b = binary_conversion(pixel)
            # modify the least significant bit only if there is still data to store
            if data_index < data_len:
                # least significant red pixel bit
                pixel[0] = int(r[:-1] + binary_code_message[data_index], 2)
                data_index += 1
            if data_index < data_len:
                # least significant green pixel bit
                pixel[1] = int(g[:-1] + binary_code_message[data_index], 2)
                data_index += 1
            if data_index < data_len:
                # least significant blue pixel bit
                pixel[2] = int(b[:-1] + binary_code_message[data_index], 2)
                data_index += 1
            # if data is encoded, just break out of the loop
            if data_index >= data_len:
                break
    return image

def decode(image_name):
    print("***Decoding Started***")
    # read the image
    image = cv2.imread(image_name)
    binary_data = ""
    for row in image:
        for pixel in row:
            r, g, b = binary_conversion(pixel)
            binary_data += r[-1]
            binary_data += g[-1]
            binary_data += b[-1]
    # split by 8-bits
    all_bytes = [binary_data[i: i + 8] for i in range(0, len(binary_data), 8)]
    # convert from bits to characters
    decoded_data = ""
    for byte in all_bytes:
        decoded_data += chr(int(byte, 2))
        if decoded_data[-5:] == "=====":
            break
    return decoded_data[:-5]