import cv2 as cv
video = cv.VideoCapture("rtsp://192.168.0.102:8080/h264_ulaw.sdp")

while True:
    _, frame = video.read()
    cv.imshow("RTSP", frame)
    k = cv.waitKey(1)
    if k == ord('q'):
        break


video.release()
cv.destroyAllWindows()