import os
import shutil
#print(os.listdir('Images'))
exists = os.path.exists('/Users/Admin/Documents/FamilyTree.xlsx')
#print(exists) 
root,ext = os.path.splitext('/Users/Admin/Documents/FamilyTree.xlsx')
print(ext)
a,b = 0,1