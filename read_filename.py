"""
   This utility is for change in name of all files in a directory.
"""
import os
path =  os.getcwd()
#path2 = path+'/cisco_temp/'
path = path
print(path)

files = os.listdir(path)

for file in files:
    print(file)
    os.rename(file, file.replace("cisco_", ""))
    # os.rename(path2, file.replace("cisco_ios", "ios"))
    # os.rename(path2, file.replace("cisco_xe", "xe"))
    # os.rename(path2, file.replace("cisco_xr", "xr"))
    # os.rename(path2, file.replace("cisco_asa", "asa"))
