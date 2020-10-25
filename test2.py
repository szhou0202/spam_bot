from py_imessage import imessage
import time as time

phone = "7745340078"

for i in range(7):
    guid = imessage.send(phone, "deviated septum check oop")
    time.sleep(10)
