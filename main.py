#!/usr/bin/env python

'''
Control FriendRank from the command line.
Author: Sean Behan
Inspired by an idea from Terri Dobbins
'''
import argparse
import sys
import libs.functions  # local reference to lib/functions.py

sys.path.append("libs")


def main():
    """ Main function
    """
    class MyParser(argparse.ArgumentParser):
        """ Class for argument handling
        """
        def error(self, message):
            # (description='Control FriendRank from the command line.')
            sys.stderr.write('error: %s\n' % message)
            self.print_help()
            sys.exit(2)

    parser = MyParser()
    parser.add_argument('name', nargs='+')

    parser.add_argument("-v", "--verbose",
                        help="increase output verbosity",
                        action="store_true")

    parser.add_argument('-a', '--add',
                        help='add a person to the friend list',
                        action="store_false")

    '''
    parser.add_argument('names', metavar='name', type=str,
        help='a string for the persons name')

    parser.add_argument('ranks', metavar='rank', type=int,
        help='an integer for the persons rank')
    '''

    args = parser.parse_args()
    print(args.help)


if __name__ == "__main__":
    main()
