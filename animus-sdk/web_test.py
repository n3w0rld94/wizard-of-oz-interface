# -*- coding: utf-8 -*-
# Copyright (c) 2020, Cyberselves Universal Ltd.
# All Rights Reserved

import animus_client as animus
import animus_utils as utils
import sys
import logging
import numpy as np
import random
import cv2
from flask import Flask, render_template, Response

from loginDetails import LoginDetails

stopFlag = False
def setup():
    global stopFlag
    log = utils.create_logger("MyAnimusApp", logging.INFO)
    log.info(animus.version())

    audio_params = utils.AudioParams(
                Backends=["notinternal"],
                SampleRate=16000,
                Channels=1,
                SizeInFrames=True,
                TransmitRate=30
            )

    setup_result = animus.setup(audio_params, "PythonAnimusBasics", True)
    if not setup_result.success:
        sys.exit(-1)

    login_result = animus.login_user(LoginDetails.username, LoginDetails.password, False)
    if login_result.success:
        log.info("Login Success")
    else:
        log.info("Login Failed")
        sys.exit(-1)

    get_robots_result = animus.get_robots(True, True, False)
    if not get_robots_result.localSearchError.success:
        log.error(get_robots_result.localSearchError.description)

    if not get_robots_result.remoteSearchError.success:
        log.error(get_robots_result.remoteSearchError.description)

    if len(get_robots_result.robots) == 0:
        log.info("No Robots found")
        animus.close_client_interface()
        sys.exit(-1)

    chosen_robot_details = get_robots_result.robots[1]

    myrobot = animus.Robot(chosen_robot_details)
    connected_result = myrobot.connect()
    if not connected_result.success:
        print("Could not connect with robot {}".format(myrobot.robot_details.name))
        animus.close_client_interface()
        sys.exit(-1)

    open_success = myrobot.open_modality("vision")
    if not open_success:
        log.error("Could not open robot vision modality")
        sys.exit(-1)

print("testing 123")

app = Flask(__name__)

def gen_frames():  
    while True:
        image_list, err = myrobot.get_modality("vision", True)
        if err.success:
            
            frame = image_list[0].image
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            
            j = cv2.waitKey(1)
            if j == 27:
                break
            
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result 

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

app.run() # 82.39.229.255:9090 for external access


#cv2.namedWindow("RobotView")
#try:
#    while True:
#        image_list, err = myrobot.get_modality("vision", True)
#        if err.success:
#            cv2.imshow("RobotView", image_list[0].image)
#            j = cv2.waitKey(1)
#            if j == 27:
#                break
#
#            counter += 1
#
#            if counter > 100:
#                counter = 0
#                if motion_counter >= len(list_of_motions):
#                    motion_counter = 0
#                ret = myrobot.set_modality("motor", list(list_of_motions[motion_counter].values()))
#                motion_counter += 1

#except KeyboardInterrupt:
#    cv2.destroyAllWindows()
#    log.info("Closing down")
#    stopFlag = True
#except SystemExit:
#    cv2.destroyAllWindows()
#    log.info("Closing down")
#    stopFlag = True

#cv2.destroyAllWindows()
#if stopFlag:
#    myrobot.disconnect()
#    animus.close_client_interface()
#    sys.exit(-1)



myrobot.disconnect()
animus.close_client_interface()
