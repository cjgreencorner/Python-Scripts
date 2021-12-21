#!/usr/bin/env python
##########################################
#               Stopwatch                #
##########################################

__author__ = "Joel Chapon"
__email__ = "joel.chapon@student.kdg.be"
__status__ = "Finished"

import time

def time_elapsed(sec):
  mins = sec // 60
  sec = sec % 60
  hours = mins // 60
  mins = mins % 60
  print("Time elapsed: = {0} hours, {1} minutes, {2} seconds".format(int(hours),int(mins),sec))
  print("")
  main()

def main():
  print("Stopwatch")
  input("Press enter to start.")
  startingTime = time.time()
  input("Press enter to stop.")
  stopTime = time.time()
  watch = stopTime - startingTime
  time_elapsed(watch)

if __name__ == '__main__':
    main()
