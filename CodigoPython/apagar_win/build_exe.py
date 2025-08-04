import PyInstaller.__main__

PyInstaller.__main__.run([
    'app.py',
    '--onefile',
    '--console', # or --windowed if you don´t need windows command line
    '--name',
    'PowerWin',
    '--clean'
])