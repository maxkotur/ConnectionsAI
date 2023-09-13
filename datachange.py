import pandas as pd

colors = ['🟡', '🟢', '🔵', '🟣']
dataset = {}

file = open("data.txt",  encoding="utf8")
for line in file:
    if line == "\n":
        continue
    if line[0] in colors:
        string = line[2:].split(":")
        title = string[0]
        words = string[1].strip()
        words = words.split(", ")
        data = {title: words}
        dataset.update(data)
        
        print(data)
    