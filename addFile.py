import os

with open('plants.txt') as x:
    for line in x:
        line = line.strip()
        os.mkdir(str(line))
