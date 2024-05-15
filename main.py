import random
from Boar_detect import WildBoarDetect
from ESPCAM import ESP_CAM
import time

ip_address  = "192.168.3.210"

camera = ESP_CAM(cam_ip=ip_address)

detector = False

ai = WildBoarDetect()
while True:
    print("capturing..")
    image = camera.capture_photo()
    print("captured")
    time.sleep(5)
    detector =  ai.detect()
    if detector:
        camera.toggle_pin_on()

        time.sleep(3)
        print(" Turning off pin 13.")

        camera.toggle_pin_off()

    else:
        time.sleep(5)  # Sleep for 5 seconds before capturing the next photo
