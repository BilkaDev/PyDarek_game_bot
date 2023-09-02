import time


def get_frequency():
    count_cycles = 0
    time_in_seconds = time.time()

    def frequency():
        nonlocal count_cycles
        count_cycles += 1
        return count_cycles / (time.time() - time_in_seconds)

    return frequency
