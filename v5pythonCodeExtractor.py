# some kind of quick thing to extract the code from a v5python json thingy and produce
# a .py file


import os
import sys
import json
from optparse import OptionParser







def main(argv):


    """
    Options
    """
    usage = "Usage: %prog [options] thing\n"
    parser = OptionParser(usage=usage)


    parser.add_option("-f", "--file", action="store", type="string",
                      default=None, dest="inputfile",
                      help="v5python file (full name) to convert")


    (options,args) = parser.parse_args()


    if not(os.path.exists(options.inputfile)):
       print ("Input file: %s doesn't seem to exist...", options.inputfile)
       sys.exit(3)


    inputfilebase=os.path.splitext(options.inputfile)[0]
    
    outputfile=inputfilebase+".py"
    
    with open(options.inputfile, "r") as read_file:
        readJson = json.load(read_file)
        
        
    f = open(outputfile, 'w')
    
    
    print (readJson["textContent"], file=f)
    
    f.close

if __name__ == '__main__':


    main(sys.argv[1:])