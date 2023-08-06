# imports
import glob
import os

# Variables
cwd = os.getcwd() #path to Searchifyy
programPath = cwd + "\Data" # path to data
path = os.listdir(programPath) # path of the directory
data = '' # used for urls

# for each file in the current folder
for dataFile in path:

    # make the file path a string
    strFile = programPath + "\\" + str(dataFile)

    # if the file is a javascript file...
    if (strFile.endswith(".js")):

        # open the file
        with open(strFile) as txt:

            # add file's contents to the data variable
            data += txt.read()

# get rid of js syntax
data = data.replace("var urlArray = [", "")
data = data.replace("];", ", ")
data = data[:-2]


# File
text_file = open("sitemap.js", "w", errors="ignore")
text_file.write("var urlArray = [" + str(data) + "];")
text_file.close()