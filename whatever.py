import os
import shutil

from_dir = 'Images'
to_dir = 'anything'

listOfFiles = os.listdir(from_dir)
#print(listOfFiles)

for i in listOfFiles:
    name,extension = os.path.splitext(i)
#    print(extension)
    if extension == '':
        continue
    if extension in['.gif','.png','.jpg','.jpeg','.jfif']:
        path1 = from_dir + '/' + i
        path2 = to_dir + '/' + 'imagefiles'
        path3 = to_dir + '/' + 'imagefiles' + '/' + i
        if os.path.exists(path2):
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            shutil.move(path1,path3) 