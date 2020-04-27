from datetime import datetime
from time import sleep
import sys

def start_screen():
    print("#############################")
    print("###   Pomodoro Timer App  ###")
    print("#############################")

    print("\n\n- The study time will be broken up into 20 minute focus periods.")
    print("- Every 4 focus periods will be separated by a 5 minute rest.")
    print("- After every 4 focus periods will there will be a 10 minute rest. \n")
    
    duration = int(input("How long do you need to study? (minutes): "))
    if duration < 20:
        sys.exit("Hmmmmmm.... this sounds like you don't need this timer. So, Goodbye!")
    short_rest = 5
    long_rest = 10
    sequence = create_pomodoro_sequence(duration, short_rest, long_rest)
    print("Start!\n")
    timer(sequence)
    print("Done!")

def create_pomodoro_sequence(duration, short_rest, long_rest):
    sequence = []
    j = 0
    focus_periods = duration//20
    for i in range(focus_periods):
        if i > 0 and j < 3:
            sequence.append(5)
            j = j +1
        elif i > 0 and j == 3:
            sequence.append(10)
            j = 0
        sequence.append(20)
    return sequence

def timer(sequence):
    for i in sequence:
        start = datetime.now()
        stop = datetime.now()
        if i < 20:
            message = "Rest"
        else:
            message = "Focus"
        print(message)
        while int(((stop-start).seconds) / 60) < i:
            sleep(60)
            stop = datetime.now()
            print(f"{int((stop - start).seconds) / 60} minutes.")

def main():
    start_screen()

main()
    
