import argparse
import parsing
parser = argparse.ArgumentParser("Input")

# add the arguments
parser.add_argument('-p','--path',type = str, required = True)

# get the inputs
args = parser.parse_args()


# do sth to the inputs
if args.path:
    parsing.parsing(args.path)