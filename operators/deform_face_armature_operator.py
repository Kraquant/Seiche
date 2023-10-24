import bpy
import cv2
from ..other import face_mesh_data
from ..other.utils import get_armature_pose_bones

class SEICHE_OT_deform_face_armature(bpy.types.Operator):
    bl_label = "Face armature deformation Operator"
    bl_idname = "wm.face_armature_deform"
    bl_description = "Handles face armature deformation"

    _timer = None

    def execute(self, context):
        if SEICHE_OT_deform_face_armature._timer != None:
            self.cancel(context)
            return {'FINISHED'}
        
        print("Action ca tourne")


        wm = context.window_manager
        SEICHE_OT_deform_face_armature._timer = wm.event_timer_add(0.01, window=context.window)
        wm.modal_handler_add(self)
        return {'RUNNING_MODAL'}   

    def modal(self, context, event):
        if event.type != 'TIMER' and SEICHE_OT_deform_face_armature._timer != None:
            return {'PASS_THROUGH'}

        elif event.type != 'TIMER' and SEICHE_OT_deform_face_armature._timer == None:
            return {'FINISHED'}

        data = context.scene.seiche_settings.detection_settings.face_data[-1]    
        # Animating the armature
        pose_bones = get_armature_pose_bones(context)
        bpy.ops.object.mode_set(mode='POSE')

        i = 0
        for bone in pose_bones:
            new_pos = data.face_vertices[i].world_position

            # Normalize the position
            centered_pos =  (new_pos[0], new_pos[1], new_pos[2])
            bone.location = centered_pos

            i += 1
        return {'PASS_THROUGH'}
    
    def cancel(self, context):
        wm = context.window_manager
        wm.event_timer_remove(SEICHE_OT_deform_face_armature._timer)
        SEICHE_OT_deform_face_armature._timer = None
    
    
    
    @classmethod
    def poll(cls, context):
        return context.scene.seiche_settings.target_armature != None

def register():
    bpy.utils.register_class(SEICHE_OT_deform_face_armature)

def unregister():
    bpy.utils.unregister_class(SEICHE_OT_deform_face_armature)