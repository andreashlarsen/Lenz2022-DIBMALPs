import os.path

def out(output):
    print(output)

    outfile = 'fit.log'
    if os.path.isfile(outfile):
        with open('fit.log','a') as f:
            f.write('%s\n' % output)
    else:
        with open('fit.log','w') as f:
            f.write('%s\n' % output)
