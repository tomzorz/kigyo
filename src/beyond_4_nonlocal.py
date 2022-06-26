import time

def stopwatch():
    last = None

    def elapsed():
        nonlocal last
        now = time.time()

        if last is None:
            last = now
            return None

        result = now - last
        last = now
        return result

    return elapsed


# from beyond_4_nonlocal import stopwatch
# s = stopwatch()
# ... call s()