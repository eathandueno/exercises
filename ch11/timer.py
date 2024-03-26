#!/usr/bin/env python3

from datetime import datetime, time

def main():
    print("The Timer program")
    print()

    # start timer
    input("Press Enter to start...")
    start_time = datetime.now()
    print("Start time:", start_time.strftime("%H:%M:%S"))
    print()
    
    # stop timer
    input("Press Enter to stop...")    
    stop_time = datetime.now()
    print("Stop time: ", stop_time.strftime("%H:%M:%S"))
    print()

    # calculate elapsed time
    elapsed_time = stop_time - start_time
    hours, remainder = divmod(elapsed_time.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    print("Elapsed time: ", "{:02}:{:02}:{:02}".format(int(hours), int(minutes), int(seconds)))

if __name__ == "__main__":
    main()
