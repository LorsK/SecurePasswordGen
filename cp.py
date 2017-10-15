import os, sys, getopt
from Crypto.Hash import SHA256

#################
#create password#
#################
 
def run(key, app):
    hash = SHA256.new()
    hash.update(key + app)
    hashlength = len(key)+len(app)
    
    if (hashlength < 9):
        hashlength += 9
        
    print hash.hexdigest()[0:hashlength]

def usage():
    print ('Usage:	' + os.path.basename(__file__) + ' options file ')
    print ('Options:')
    print ('\t -k key, --key=key')
    print ('\t -a app, --app=app')    
    print ('\t -o output_file, --output=output_file')
    sys.exit(2) 

def main(argv):
    try:
        options, remainder = getopt.getopt(sys.argv[1:], 'vka:o:', [ 
                                                                 'version=',
                                                                 'key=',
                                                                 'app=',
                                                                 'output='
                                                                 ])
    except getopt.GetoptError as err:
        print(err)
        usage()
    # extract arguments
    key = None
    app = None
    output_filename = None
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
    # check arguments

    if (key is None):
        print('key option is missing\n')
        usage()
    if (app is None):
        print('app option is missing\n')
        usage()        

    #run command
    run(key, app)    
 
if __name__ == "__main__":
    main(sys.argv[1:])