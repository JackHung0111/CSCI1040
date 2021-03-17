# Hung Yiu Pan
# 1155108381
# CSCI1040 Lab4 Q5

import os

str = input("Input path to search: ")

for dirPath, dirNames, fileNames in os.walk("q5_dir"):
    for f in fileNames:
        print (os.path.join(dirPath, f))