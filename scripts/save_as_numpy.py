"""
Note: Do not refer to this script for any usage!
Developer script to convert CMATERdb datasets into NumPy format
Author: Omkar Prabhu (prabhuomkar)
License: Apache 2.0
"""
from glob import glob
import os
import re
import matplotlib.pyplot as plt

import numpy as np
from PIL import Image

DIMS = (32, 32)
BANGLA_SINGLE_COUNT = 500
DEV_TEL_SINGLE_COUNT = 250


def load(numeral_type):
    """ Loads npz format type of data for given type of numeral 
    Args:
        numeral_type (string): type of numeral to load
    Returns:
        None
    """

    train = np.load(os.path.join(os.path.dirname(__file__), '../datasets/'+numeral_type+'-numerals/training-images.npz'))
    test = np.load(os.path.join(os.path.dirname(__file__), '../datasets/'+numeral_type+'-numerals/testing-images.npz'))
    print('Total Training: ', str(len(train['labels'])))
    print('Total Testing: ', str(len(test['labels'])))
    print('Training Data:')
    print(train['images'][0].shape, train['labels'][0].shape)
    print('Testing Data:')
    print(test['images'][0].shape, test['labels'][0].shape)
    plt.title(test['labels'][399])
    plt.imshow(test['images'][399])
    plt.show()

def save(numeral_type):
    """ Converts training & testing images for given type of numeral into npz format
    Args:
		numeral_type (string): type of numeral to load
	Returns:
		(training_data, testing_data) (tuple): dataset to use
    """
    # Relative path things
    rel_dirname = os.path.dirname(__file__)

    # Entries
    train_x, train_y, test_x, test_y = [], [], [], []

    # List all directories & files inside the same
    for dirname in os.listdir(os.path.join(rel_dirname, './original/'+numeral_type)):
        count = 1
        for filename in glob(os.path.join(rel_dirname, './original/'+numeral_type+'/'+dirname+'/*.bmp')):
            img = Image.open(os.path.join(rel_dirname, filename))
            img = img.resize(DIMS)
            if numeral_type == "bangla" and count > BANGLA_SINGLE_COUNT:
                test_x.append(np.array(img).flatten())
                test_y.append(int(dirname))
            elif numeral_type != "bangla" and count > DEV_TEL_SINGLE_COUNT:
                test_x.append(np.array(img).flatten())
                test_y.append(int(dirname))
            else:
                train_x.append(np.array(img).flatten())
                train_y.append(int(dirname))
            count += 1

    train_x = np.array(train_x).reshape(-1, 32, 32, 3).astype(np.uint8)
    test_x = np.array(test_x).reshape(-1, 32, 32, 3).astype(np.uint8)
    train_y = np.array(train_y).reshape(-1).astype(np.int64)
    test_y = np.array(test_y).reshape(-1).astype(np.int64)

    print('Total Training: ', str(len(train_x)))
    print('Total Testing: ', str(len(test_x)))
    print('Training Data:')
    print(train_x[0].shape, train_y[0].shape)
    print('Testing Data:')
    print(test_x[0].shape, test_y[0].shape)
    plt.title(test_y[299])
    plt.imshow(test_x[299])
    plt.show()
    np.savez_compressed('../datasets/'+numeral_type+'-numerals/training-images.npz', images=train_x, labels=train_y)
    np.savez_compressed('../datasets/'+numeral_type+'-numerals/testing-images.npz', images=test_x, labels=test_y)


if __name__ == '__main__':
    save('bangla')
    # load('bangla')