import time
import cv2
import bpy

class VideoUtilities():
    def __init__(self):
        self.t0 = time.time()
        self.time = 0
        self.fps = 0
    def register_image(self, img, write_fps = True):
        c_time = time.time()-self.t0
        self.fps = 1 / (c_time - self.time) if c_time - self.time != 0 else 0
        self.time = c_time
    
        if not write_fps: return
        cv2.putText(img,
                    f'FPS: {int(self.fps)}',
                    (20, 70),
                    cv2.FONT_HERSHEY_PLAIN,
                    3,
                    (0, 255, 9),
                    3)

       