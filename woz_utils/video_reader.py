from models.modalities import Robot_Modality
import time
import cv2
import eventlet

eventlet.monkey_patch()


class Video_Reader:
    def __init__(self, robot=None):
        self.video = None
        self.capture = True
        self.robot = robot

    def start_capture(self):
        if not self.robot: 
            yield None
            raise StopIteration

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


class Mockup_Video_Reader:
    def __init__(self, robot=None):
        self.video = None
        self.capture = True
        self.robot = robot

    def start_capture(self):
        videoReader = cv2.VideoCapture(0)
        while self.capture:
            success, image = videoReader.read()
            if success:
                print("got a frame list, success: " + str(success))
                ret, jpeg = cv2.imencode(".jpg", image)
                frame = jpeg.tobytes()
                yield (
                    b"--frame\r\n"
                    b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n\r\n"
                )
                time.sleep(0)

        videoReader.release()
        raise StopIteration
