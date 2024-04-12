"""
measure the time taken by a function to run"""

import time

def time_trials(func, list, target, trials = 10):
    totaltime = 0
    for i in range(trials):
        start = time.time()
        func(list, target)
        totaltime += time.time() - start
    
    print("average = %10.7f for n = %4d" % (totaltime/trials, len(list)), end="")