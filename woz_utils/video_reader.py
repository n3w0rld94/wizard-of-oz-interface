import time
import cv2
import eventlet

eventlet.monkey_patch()


class Video_Reader():

    def __init__(self):
        self.video = None
        self.capture = True

    def start_capture(self):
        self.video = cv2.VideoCapture(0)
        time.sleep(2)
        while self.capture:

            success, image = self.video.read()
            print('got a frame, success: ' + str(success))

            ret, jpeg = cv2.imencode('.jpg', image)
            frame = jpeg.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
            time.sleep(0)
            
        
        self.video.release()
        raise StopIteration
