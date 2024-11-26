import os

folders = input("please give list of folder name:" ).split()

# print(folders)

for folder in folders:
    file = os.listdir(folder)
    print(file)