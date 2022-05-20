import traceback
import sys

def three():
    stack = traceback.format_stack()
    for s in stack:
        if "\n" in s:
            sys.stdout.write(s)
        else:
            print(s)
    print(s)


def two():
    three()


def one():
    two()


def main():
    one()


if "__main__" == __name__:
    main()