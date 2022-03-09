import cv2
from deepface import DeepFace
import numpy as np

Image_Path = "{YOUR IMAGE PATH}";

Image = cv2.imread(Image_Path)

Analyze = DeepFace.analyze(Image,actions=['emotion'])

Analyzed_Image = cv2.putText(Image,Analyze['dominant_emotion'],(380,50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)

cv2.imshow("Recognize Emotions Finder | asefg482",Analyzed_Image);
cv2.waitKey(0)