from os.path import splitext, basename, join, dirname

import cv2
import numpy as np


def generate_sample_data(image_path):
    img = cv2.imread(image_path, -1)
    height, width, _ = img.shape
    points_number = 20
    data_file_name = splitext(basename(image_path))[0] + '.csv'
    data_file_path = join(dirname(image_path), '..', 'coordinates_data', data_file_name)

    heights = np.random.randint(height, size=points_number)
    widths = np.random.randint(width, size=points_number)
    coordinates = np.array((widths, heights))
    np.savetxt(data_file_path, coordinates.T, delimiter=',', fmt='%d')
