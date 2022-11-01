import os

def store_files(data):
    os.system('mkdir -p %s' % data)
    os.system('cp %s %s' % ('Ifit.dat',data))
    os.system('cp %s %s' % ('Idat.dat',data))
    os.system('mv %s %s' % ('fit.log',data))
