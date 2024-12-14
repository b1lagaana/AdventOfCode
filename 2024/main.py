# Get files and run through them to get solutions

import os
import sys

# get directory of python script
python_main_path = os.path.dirname(os.path.dirname(__file__))

# check if filename is provided
try:
    sys.argv[1]
except IndexError:
    filename = os.listdir(python_main_path)
else:
    filename = sys.argv[1]


if __name__ == '__main__':
    print(python_main_path)
