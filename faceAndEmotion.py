import cv2
import numpy as np
from keras.models import load_model

object_cascade = cv2.CascadeClassifier("C:\\Users\\marvi\\PycharmProjects\\pythonProject1\\venv\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml")
emotion_model = load_model()

cap = cv2.VideoCapture(0)

while True:
