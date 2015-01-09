__author__ = 'robert'


import os


if not os.path.isdir('./test'):
    os.mkdir('./test')

with open('./test/data.txt', mode='w') as fh:

    fh.write('testdata')


with open('./test/data.txt', mode='r') as fh:

    print(fh.read())

fh = open('./test/data.txt', mode='a')

fh.write('wuba luba dup dup')

os.fsync(fh)

fh.close()

print 'Finished!'