import cv2 # Importing the OpenCV Python Module for this Program.

a = cv2.VideoCapture(0) # Taking Video from Default Camera.
while(True): # Putting a While loop.
	b, c = a.read() # Making the Program read the Video Captured in 'a'.
	cv2.imshow('Python WebCam Viewer', c) # Displaying the Video through a Pop-up Window.
	if cv2.waitKey(1) == ord('x'): # Waiting for a Particular key for the Program to exit. I have taken x, you can take it by your choice.
		break # Breaking the While loop after the Key is Pressed.

a.release() # Releasing the Video.
cv2.destroyAllWindows() # Destroying all the Windows.