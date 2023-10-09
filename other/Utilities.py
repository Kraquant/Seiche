import time
import cv2
import bpy

class VideoUtilities():
    def __init__(self):
        self.p_time = 0
    def print_fps(self, img):
        c_time = time.time()
        fps = 1 / (c_time - self.p_time) if c_time - self.p_time != 0 else 0

        cv2.putText(img,
                    f'FPS: {int(fps)}',
                    (20, 70),
                    cv2.FONT_HERSHEY_PLAIN,
                    3,
                    (0, 255, 9),
                    3)

        self.p_time = c_time

class SEICHE_camera_settings(bpy.types.PropertyGroup):
    camera_width: bpy.props.IntProperty(
        name="Camera width",
        default = 600,
        min = 0,
        max = 10000,
        description="Represents the camera width")

    use_default_res: bpy.props.BoolProperty(
        name="Use default cam resolution",
        default=True,
    )

    camera_height: bpy.props.IntProperty(
        name="Camera height",
        default = 600,
        min = 0,
        max = 10000,
        description="Represents the camera height")

    camera_id: bpy.props.IntProperty(
        name="Camera id",
        default = 1,
        description="Represents the camera id")

def register():
    bpy.utils.register_class(SEICHE_camera_settings)
    bpy.types.Scene.seiche_user_camera_settings = bpy.props.PointerProperty(
        name='User camera settings',
        type=SEICHE_camera_settings)
    


def unregister():
    bpy.utils.unregister_class(SEICHE_camera_settings)
