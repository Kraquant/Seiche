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


def get_armature_object(context):
    settings = context.scene.seiche_settings
    armature_data = settings.target_armature
    if armature_data:
    # Iterate through users to find the associated object
        associated_object = None
        for obj in bpy.data.objects:
            if obj.data == armature_data:
                associated_object = obj

        if associated_object:
            return associated_object
        else:
            return None
    else:
        print(f"Face armature not found in Blender data")
    return None

def get_armature_pose_bones(context):
    armature_obj = get_armature_object(context)
    if armature_obj:
        return armature_obj.pose.bones
    return None
    

def bind_mesh_and_armature(context):
    bpy.ops.object.mode_set(mode='OBJECT')
    mesh_obj = context.scene.seiche_settings.target_mesh
    armature_obj = get_armature_object(context)

    mesh_obj.select_set(True)
    armature_obj.select_set(True)
    
    bpy.context.view_layer.objects.active = armature_obj
    bpy.ops.object.mode_set(mode='POSE')
    bpy.ops.pose.select_all(action='SELECT')
    bpy.ops.object.parent_set(type='ARMATURE_AUTO')
    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.select_all(action='DESELECT')
