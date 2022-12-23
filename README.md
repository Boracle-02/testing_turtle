I saw a tiktok video about the turtle module in python and it reminded me of when I first started programming in javascript and using a turtle to draw up a small game.
I wanted to revist that part and create a analog clock since it would also let me get familar with the time module in python.

You only need to download the analog_clock.py file and run it. Make sure you have pyautogui and turtle installed. 
I believe the time module comes already installed with python. 

I am using python version 3.9.1 but any python version so to avoid any possible errors, try to have it close to that version as possible. 
Must be python 3 though since the formatting for my functions creates errors in python 2 I believe.

This is an analog clock that updates with you!
No numbers to denote the time, but should be easy to tell since we can count
Colors may be a questionable choice.

The time updates every half second since if it updates every second, there may be jumps

Fixed Issue where when you close the window you get error messages
  Cause: closing window may still cause the program to try to draw to it which creates issue since the window no longer exists
  
Note: holding the close window button or any of the title bar buttons causes the window to temporarily freeze then later jump to the correct time

Added: Hour hand now moves accordingly to the minute hand, i.e. if the time is 3:30, the hour hand should be in the middle of 3 and 4

Hope you enjoy!
