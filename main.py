import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox
import pyttsx3


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()




vidio_capture = cv2.VideoCapture(0)
labels = []


while True:
    ret, frame = vidio_capture.read()
    bbox, label, conf = cv.detect_common_objects(frame)
    output_image = draw_bbox(frame, bbox, label, conf)

    cv2.imshow("Object detection", output_image)

    for item in label:
        if item in labels:
            pass
        else:
            labels.append(item)


    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


i = 0
new_sentance = []
for label in labels:
    if i == 0:
        new_sentance.append(f"I found {label},")

    else:
        new_sentance.append(f" ,{label}")

    i += 1

print("".join(new_sentance))
