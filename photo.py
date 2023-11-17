# !/usr/bin/python
# -*- coding: utf-8 -*-
import cv2
import time

AUTO = False  # 自动拍照，或手动按s键拍照
INTERVAL = 2  # 自动拍照间隔

cap = cv2.VideoCapture(0 + cv2.CAP_DSHOW)  # windows下开启摄像头是采用如下语句(微软特有):cv2.VideoCapture( camera_number + cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 2560)  # 设置双目的宽度
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)  # 设置双目的高度

# 显示缓存数
# print(cap.get(cv2.CAP_PROP_BUFFERSIZE))
# 设置缓存区的大小
# cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)

print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# 设置FPS
# print('setfps', cap.set(cv2.CAP_PROP_FPS, 25))
# print(cap.get(cv2.CAP_PROP_FPS))

counter = 0
utc = time.time()
folder = "./images/"  # 拍照文件目录


def shot(pos, frame):
    global counter
    path = folder + pos + "_" + str(counter) + ".jpg"
    cv2.imwrite(path, frame)
    print("snapshot saved into: " + path)


while True:
    ret, frame = cap.read()

    if not ret:
        print("camera is not connected!")
        break

    left_frame = frame[0:720, 0:1280]
    right_frame = frame[0:720, 1280:2560]

    cv2.imshow("left", left_frame)
    cv2.imshow("right", right_frame)

    now = time.time()
    if AUTO and now - utcq >= INTERVAL:
        shot("left", left_frame)
        shot("right", right_frame)
        counter += 1
        utc = now

    key = cv2.waitKey(1)
    if key == ord("q"):
        break
    elif key & 0xFF == ord("s"):
        shot("left", left_frame)
        shot("right", right_frame)
        counter += 1

cap.release()