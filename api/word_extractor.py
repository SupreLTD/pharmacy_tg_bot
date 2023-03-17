import json
import string
from os import listdir
from os.path import isfile, join
import re

words = set()
base_dir = '../drugs'
files = [f for f in listdir(base_dir) if isfile(join(base_dir, f))]
for i in files:
    with open(base_dir + '/' + i, encoding='utf8') as f:
        docs = json.load(f)
        for d in docs:
            name = d['товар'].rstrip(string.punctuation)
            for w in re.split(r'\s|\(|\)|,|\\|/|\w\.|\.\w', name):
                words.add(w.rstrip(string.punctuation).lower())

with open("names.txt", 'w+', encoding='utf8') as f:
    f.write('\n'.join(words))
