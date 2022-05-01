# command line arguments come from

import sys

# sys.argv[1] is the first passed parameter, 0 is the module filename

def main():
    args = sys.argv
    for item in args:
        print(item)


if __name__ == "__main__":
    main()