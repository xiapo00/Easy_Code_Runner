import sys
from subprocess import call
from time import sleep

pyfile = sys.argv[1]
call('python "%s"' % pyfile)
print('\n-------------pyfile finish-------------\n')
while True:
    sleep(1)
