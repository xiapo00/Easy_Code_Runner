import sys
from subprocess import call
from re import split
import os
from time import sleep


cppfile = sys.argv[1]
#cppfile = 'D:\\School Works\\2020\\C++\\C2020040301\\hello.cpp'
#cppfile = 'D:\\School Works\\2020\\C++\\C2020040302\\turn_matrix.c'
L = split('\\\\', cppfile)
name = L[-1]
path = ''
for item in L[0:-1]:
    path += item + '\\'
if '.cpp' in name:
    index = -4
    text = 'pp'
else:
    index = -2
    text = ''
call('g++ "%s" -o "%s"' % (cppfile, cppfile[0:index]))
to_bat = '%s\npause' % (path + name[0:index])
call('%s.exe' % cppfile[0:index])
print('\n-------------c%sfile finish-------------\n' % text)
while True:
    sleep(1)
