import cv2
import os
import tkinter as tk
from tkinter import simpledialog
from LCD1602 import LCD1602
import subprocess

lcd = LCD1602()
lcd.clear()
lcd.write_string("Face Shot")

root = tk.Tk()
root.withdraw()
name = simpledialog.askstring(title="Name", prompt="Enter your name: ")
save_path = f"dataset/{name}"

# Tạo thư mục nếu chưa tồn tại
if not os.path.exists(save_path):
    os.makedirs(save_path)

cam = cv2.VideoCapture(0)

cv2.namedWindow("press space to take a photo", cv2.WINDOW_NORMAL)
cv2.resizeWindow("press space to take a photo", 500, 300)

img_counter = 0

while True:
    ret, frame = cam.read()
    frame = cv2.flip(frame, 1)
    if not ret:
        lcd.clear()
        lcd.write_string("Camera error")
        print("failed to grab frame")
        break
    cv2.imshow("press space to take a photo", frame)

    k = cv2.waitKey(1)
    if k % 256 == 27:
        # ESC pressed
        lcd.clear()
        lcd.write_string("Camera off")
        print("Escape hit, closing...")
        cam.release()
        cv2.destroyAllWindows()
        subprocess.run(["python", "train_model.py"], check=True)
        break
    elif k % 256 == 32:
        # SPACE pressed
        img_name = f"{save_path}/image_{img_counter}.jpg"
        cv2.imwrite(img_name, frame)
        lcd.clear()
        lcd.write_string("Save image")
        lcd.set_cursor(1, 0)
        lcd.write_string(f"{img_counter}.jpg")
        print(f"{img_name} written!")
        img_counter += 1

cam.release()
cv2.destroyAllWindows()
