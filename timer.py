#import time module for sleep
import time

#define ans for test run
ans = ''


def timer(ans):
    #set initial timer value
    timer = 90
    #anwser not yet filled in
    while ans == '' and timer >= 1:
        timer = timer-1
        time.sleep(1)
        print(timer)
    #the right anwser, timer reset
    if ans == True:
        timer = 90
    #timer ran out, anwser is wrong.
    elif timer <= 0:
        ans == False
        timer = 90
    return timer

print(timer(ans))