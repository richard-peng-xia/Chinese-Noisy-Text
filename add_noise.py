"""Main script to add noise to your corpus"""

import argparse

from noise_functions import *
from tqdm import tqdm
from utils import *

parser = argparse.ArgumentParser()
parser.add_argument('--input',
                    help="The text file you want to add noise to")
parser.add_argument('--redundant_probability', default=0.163, type=float,
                    help="Optional, the probability to redundant each token, default=0.163")
parser.add_argument('--selection_probability', default=0.163, type=float,
                    help="Optional, the probability to replace each token with a filler token, default=0.163")
parser.add_argument('--missing_probability', default=0.163, type=float,
                    help="Optional, the probability to miss each token, default=0.163")
parser.add_argument('--ordering_probability', default=0.163, type=float,
                    help="Optional, the probability to change the order of each token, default=0.163")
parser.add_argument('--comprehensive_error_probability', default=0.163, type=float,
                    help="Optional, the probability to error each token comprehensively, default=0.163")

if __name__ == '__main__':
    args = parser.parse_args()

    file_input = args.input
    print(redundant_token(file_input, args.redundant_probability))
    print(missing_token(file_input, args.missing_probability))
    print(ordering_token(file_input, args.ordering_probability))
    print(selection_token(file_input, args.selection_probability))
    print(comprehensive_token(file_input, args.comprehensive_error_probability))
