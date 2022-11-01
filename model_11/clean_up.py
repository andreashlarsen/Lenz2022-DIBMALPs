import os

def clean_up():
    os.system('rm Idat.dat Ifit.dat')
    os.system('rm -r __pycache__')