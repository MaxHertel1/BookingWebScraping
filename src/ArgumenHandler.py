import sys, getopt
from err import Errormessages

class ArgumentHandler:

    def __init__(self, args):
        try:
            opts, args = getopt.getopt(args,"ha:l:c:",["amount=","location"])
        except getopt.GetoptError:
            print('main.py -a <amount> -l <location>')
            sys.exit(2)

        for opt, arg in opts:
            if opt == '-h':
                print(Errormessages.errM["help"])
                sys.exit(2)
            elif opt == '-a':
                self.amount = int(arg)
            elif opt == '-l':
                self.location = arg
        
        if self.amount == "":
            print(Errormessages.errM["amount"])
            sys.exit(2)
        elif self.location == "":
            print(Errormessages.errM["location"])
            sys.exit(2)
        else:
            # pass - hier kann nocht etwas passieren 
            print('')
    