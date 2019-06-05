"""
How to use CMATERdb dataset
Author: Omkar Prabhu (prabhuomkar)
License: Apache 2.0
"""
import numpy as np
import os


def load(numeral_type, path=None):
    """ Loads npz format type of data for given type of numeral 
    Args:
        numeral_type (string): type of numeral to load
        path (string): path of the directory where dataset exists (only when the dataset exists in a different location)
    Returns:
        None
    """
    if path:
    	train = np.load(path+'/training-images.npz')
    	test = np.load(path+'/testing-images.npz')
    else:
    	train = np.load(os.path.join(os.path.dirname(__file__), '../datasets/'+numeral_type+'-numerals/training-images.npz'))
    	test = np.load(os.path.join(os.path.dirname(__file__), '../datasets/'+numeral_type+'-numerals/testing-images.npz'))
    print('Total Training: ', str(len(train['labels'])))
    print('Total Testing: ', str(len(test['labels'])))
    # Access Image
    print(train['images'][0])
    # Access Label
    print(train['labels'][0])

if __name__ == '__main__':
	load('devanagari')