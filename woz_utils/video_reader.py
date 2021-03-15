from models.modalities import Robot_Modality
import time
import cv2
import eventlet

eventlet.monkey_patch()


class Video_Reader:
    def __init__(self, robot):
        self.video = None
        self.capture = True
        self.robot = robot

    def start_capture(self):
        while self.capture:
            success, imageList = self.robot.get_modality(Robot_Modality.VISION, True)
            if success:
                print("got a frame list, success: " + str(success))
                for image in imageList:
                    ret, jpeg = cv2.imencode(".jpg", image.image)
                    frame = jpeg.tobytes()
                    yield (
                        b"--frame\r\n"
                        b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n\r\n"
                    )
                    time.sleep(0)

        self.robot.close_modality(Robot_Modality.VISION)
        raise StopIteration
