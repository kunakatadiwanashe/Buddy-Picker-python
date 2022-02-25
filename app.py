import random
from tkinter.font import names

names = ["tadiwanashe","tawanda","tanya","diana","anesu","precell"]
print(f"all names: {names}\n")

idx = random.randint(0, len(names) -2)
print(f"picked name: {names[idx]}")