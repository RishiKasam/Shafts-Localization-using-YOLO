

import argparse
import os
import cv2
import numpy as np
from tqdm import tqdm
from yolo_preprocessing import read_annotations
from yolo_utils import draw_kpp
from yolo_frontend import SpecialYOLO
import json

os.environ["CUDA_DEVICE_ORDER"]="PCI_BUS_ID"
os.environ["CUDA_VISIBLE_DEVICES"]="0"

argparser = argparse.ArgumentParser(
    description='Train and validate YOLO_v2 model on any dataset')

argparser.add_argument(
    '-c',
    '--conf',
    help='path to configuration file')

argparser.add_argument(
    '-w',
    '--weights',
    help='path to pretrained weights')

argparser.add_argument(
    '-i',
    '--input',
    help='path to an image or an video (mp4 format)')

def _main_(args):
    config_path  = args.conf
    weights_path = args.weights
    image_path   = args.input

    with open(config_path) as config_buffer:
        config = json.load(config_buffer)

    ###############################
    #   Make the model
    ###############################

    yolo = SpecialYOLO( input_width  = config['model']['input_width'],
                input_height  = config['model']['input_height'],
                labels              = config['model']['labels'],
                max_kpp_per_image   = config['model']['max_kpp_per_image'])

    ###############################
    #   Load trained weights
    ###############################

    grid_height, grid_width = yolo.load_weights(weights_path)
    print( "grid_height, grid_width=", grid_height, grid_width )


    ###############################
    #   Predict bounding boxes
    ###############################



    image = cv2.imread(image_path)


    image = image[:,:,1]#green channel only


    image = np.expand_dims( image, -1 )

    kpp = yolo.predict(image)

    image = np.concatenate( (image, image, image), axis = 2 )

    image = draw_kpp(image, grid_width, grid_height, kpp, config['model']['labels'])  # 4,4 sind die Ausgangsdimensionen des Grids

    print(len(kpp), 'keypoints are found')
    cv2.imwrite(image_path[:-4] + '_detected' + image_path[-4:], image)









if __name__ == '__main__':
    args = argparser.parse_args()

    #testein
    args.conf = "yolo_config.json"
    args.input = "C:\\imagescupstrainvalid\\train\\Img_000026.bmp"
    args.weights = "transparent.h5"

    _main_(args)
