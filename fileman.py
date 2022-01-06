import os
def filemgmt():
    for filename in os.listdir("static/images"):
        if filename.endswith(".jpg"):
            os.remove(os.path.join("static/images", filename))
    for filename in os.listdir():
        if filename.endswith(".csv"):
            os.remove(filename)
    for filename in os.listdir():
        if filename.endswith(".pickle"):
            os.remove(filename)