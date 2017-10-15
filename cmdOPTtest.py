import getopt
import sys

version = '1.0'
verbose = False
output_filename = 'default.out'
app = 'default'
key = '123456'

print 'ARGV      :', sys.argv[1:]

options, remainder = getopt.getopt(sys.argv[1:], 'vka:o:', [ 
                                                         'version=',
                                                         'key=',
                                                         'app=',
                                                         'output='
                                                         ])
print 'OPTIONS   :', options

for opt, arg in options:
    if opt in ('-o', '--output'):
        output_filename = arg
    elif opt in ('-v', '--verbose'):
        verbose = True
    elif opt == '--version':
        version = arg
    elif opt in ('-k', '--key'):
        key = arg
    elif opt in ('-a', '--app'):
        app = arg

print 'VERSION   :', version
print 'VERBOSE   :', verbose
print 'OUTPUT    :', output_filename
print 'REMAINING :', remainder
print 'APP       :', app
print 'KEY       :', key