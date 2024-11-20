#! /usr/bin/python

# import the necessary packages
from EmulatorGUI import GPIO
import subprocess
import time
import face_recognition
import imutils
import pickle
import cv2
from LCD1602 import LCD1602
from imutils.video import VideoStream
from imutils.video import FPS

# GPIO Pin Definitions
BTN_SHOT = 17
BTN_RUN = 22
SERVO = 18 

# GPIO Setup
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(BTN_SHOT, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BTN_RUN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(SERVO, GPIO.OUT)
GPIO.output(SERVO, GPIO.LOW)

# LCD Setup
lcd = LCD1602()
lcd.write_string("Smart Door")
lcd.set_cursor(1, 0)
lcd.write_string("Door lock")

# Load Encodings
encodingsP = "encodings.pickle"
cascade = "haarcascade_frontalface_default.xml"
data = pickle.loads(open(encodingsP, "rb").read())
detector = cv2.CascadeClassifier(cascade)


def run_script(script_name):
	try:
		subprocess.run(["python", script_name], check=True)
	except subprocess.CalledProcessError as e:
		# print(f"[ERROR] Lỗi khi chạy {script_name}: {e}")
		print(f"[ERROR] Error when running {script_name}: {e}")


def facial_recognition_system():
	currentname = "unknown"
	print("[INFO] starting video stream...")
	vs = VideoStream(src=0).start()
	time.sleep(2.0)

	fps = FPS().start()
	doorUnlock = False
	prevTime = 0

	try:
		while True:
			frame = vs.read()
			frame = imutils.resize(frame, width=500)
			frame = cv2.flip(frame, 1)
			gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
			rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

			rects = detector.detectMultiScale(
				gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE
			)
			boxes = [(y, x + w, y + h, x) for (x, y, w, h) in rects]
			encodings = face_recognition.face_encodings(rgb, boxes)
			names = []

			for encoding in encodings:
				matches = face_recognition.compare_faces(data["encodings"], encoding)
				name = "Unknown"
				if True in matches:
					matchedIdxs = [i for (i, b) in enumerate(matches) if b]
					counts = {}
					for i in matchedIdxs:
						name = data["names"][i]
						counts[name] = counts.get(name, 0) + 1
					name = max(counts, key=counts.get)

					if currentname != "Unknown":
						currentname = name
						lcd.clear()
						lcd.write_string(currentname)
						lcd.set_cursor(1, 0)
						lcd.write_string("Door unlock")
						GPIO.output(SERVO, GPIO.HIGH)
						prevTime = time.time()
						doorUnlock = True
						print("door unlock")

				names.append(name)

			if doorUnlock and time.time() - prevTime > 5:
				doorUnlock = False
				GPIO.output(SERVO, GPIO.LOW)
				lcd.clear()
				lcd.write_string("Smart Door")
				lcd.set_cursor(1, 0)
				lcd.write_string("Door lock")
				print("door lock")

			for ((top, right, bottom, left), name) in zip(boxes, names):
				cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
				y = top - 15 if top - 15 > 15 else top + 15
				cv2.putText(frame, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)

			cv2.imshow("Facial Recognition is Running", frame)
			key = cv2.waitKey(1) & 0xFF
			if key == 27:  # Nhấn ESC để thoát
				break

			fps.update()

	finally:
		fps.stop()
		print("[INFO] Elapsed time: {:.2f}".format(fps.elapsed()))
		print("[INFO] Approx. FPS: {:.2f}".format(fps.fps()))
		vs.stop()
		cv2.destroyAllWindows()


def main():
	print("[INFO] System is waiting for signal...")
	try:
		while True:
			if GPIO.input(BTN_SHOT) == GPIO.LOW:
				print("[INFO] Take a face shot")
				run_script("face_shot.py")
			elif GPIO.input(BTN_RUN) == GPIO.LOW:
				print("[INFO] Start facial recognition system")
				facial_recognition_system()
			time.sleep(0.1)
	except KeyboardInterrupt:
		print("[INFO] End of program.")
		lcd.close()
		GPIO.close()


if __name__ == "__main__":
	main()
