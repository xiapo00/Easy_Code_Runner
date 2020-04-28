import sys
import os
from subprocess import call
from time import sleep
from re import split


javafile = sys.argv[1]
#javafile = 'D:\\School Works\\2020\\java\\java2020040302\\Vari_test.java'
L = split('\\\\', javafile)
name = L[-1]
path = ''
for item in L[0:-1]:
    path += item + '\\'
os.chdir(path)
call('javac -encoding utf-8 %s' % name)
call('java %s' % name[0:-5])
print('\n-------------javafile finish-------------\n')
while True:
    sleep(1)
