import os

DIR_PATH = "C:/Users/naves/Downloads"


files_list = os.listdir(DIR_PATH)
for file in files_list:
    if file.endswith(".zip"):
        os.remove(f"{DIR_PATH}/{file}")
