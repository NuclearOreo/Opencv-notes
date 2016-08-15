import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):
    _, frame = cap.read()
    laplacian  = cv2.Laplacian(frame, cv2.CV_64F)
    soblelx = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize = 5)
    soblely = cv2.Sobel(frame, cv2.CV_64F, 0, 1, ksize = 5)
    edges = cv2.Canny(frame,100,100)

    cv2.imshow('original',frame)
    cv2.imshow('laplacian', laplacian)
    cv2.imshow('soblelx', soblelx)
    cv2.imshow('soblely', soblely)
    cv2.imshow('edges', edges)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()
