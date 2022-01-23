import cv2 as cv
import time
import argparse
import random
  
  
# define a video capture object


def rounds(t):
    
    #random_cord = (random.sample(range(1, 10),1), random.sample(range(1, 10),1))
    
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

        vid = cv.VideoCapture(0)
        ret, frame = vid.read()
  
        # Display the resulting frame
        
        #print(random.sample(range(1, 10),1))
        path = r'/Users/jean-pierreciotta/Documents/PYTHON/OpenCV/test.jpeg'
        image = cv.imread(path, 1)
        radius = 200
        color = (0, 0,  255)
        thickness = -1
        random_cord = (220, 550)
        image = cv.circle(image, random_cord, radius, color, thickness)

        cv.imshow('basic frame', image)

        if cv.waitKey(1) & 0xFF == ord('q'):
            break
  
    # After the loop release the cap object
    vid.release()
      
    print('Fire in the hole!!')
  
  
# input time in seconds
t = input("Enter the time in seconds: ")
  
# function call
rounds(int(t)) 