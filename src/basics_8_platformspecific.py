# we use exceptions to get platform specific code

# on windows: msvcrt
# on unix: sys, tty, termios

try:
    import msvcrt

    def getkey():
        return msvcrt.getch()

except ImportError:

    import sys
    import tty
    import termios

    def getkey():
        fd = sys.stdin.fileno()
        original_attributes = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, original_attributes)
        return ch

# if we are on neither, a new ImportError will be raised