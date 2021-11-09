"""
a tool to compute the max depth inside a folder
"""

# Path is your friend
from pathlib import Path


# with Python-3.9, one can just write
#def scanner(folder) -> tuple[int, Path]:

from typing import Tuple

def scanner(folder) -> Tuple[int, Path]:
    """
    returns a tuple depth, file_as_path
    """
    path = Path(folder)
    max_depth = 0
    max_file = None
    # in this glob expression:
    # '**' means any subfolder at any depth
    # '*' means any file underneath
    for file in path.glob("**/*"):
        # file.parts contains the folders from the top folder
        depth = len(file.parts)
        # record the longest one, together with the file
        if depth >= max_depth:
            max_depth = depth
            max_file = file
    # not counting the depth of folder itself
    return max_depth-len(path.parts), max_file

###
# we use sys.argv to retrieve the command line arguments
# e.g. when we run this from the command line with
# python filescanner.py /some/folder
# then sys.argv will hold
# ['filescanner.py', '/some/folder']
import sys

# checking the number of args actually provided
if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} folder")
    exit(1)

D, F = scanner(sys.argv[1])

print(f"depth {D} found with {F.absolute()}")

# optional: print all the steps so we can visually check the result
relative = F.relative_to(Path(sys.argv[1]))
for level, piece in enumerate(relative.parts, 1):
    print (f"level {level}: {piece}")
