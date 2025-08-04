import os, cleaner

cleaner.cleaning()

os.makedirs('../carpeta/folder')
os.chdir('../carpeta')
print(os.getcwd())
print(os.listdir())

