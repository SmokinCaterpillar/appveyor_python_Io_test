__author__ = 'robert'


import os


os.mkdir('./test')

with open('./test/data.txt', mode='w') as fh:

    fh.wirte('testdata')


with open('./test/data.txt', mode='r') as fh:

    print(fh.read())

print 'Finished!'