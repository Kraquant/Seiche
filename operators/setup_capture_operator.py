import bpy
from ..other.utils import bind_mesh_and_armature
import time

class SEICHE_OT_setup_capture(bpy.types.Operator):
    bl_label = "Face armature deformation Operator"
    bl_idname = "wm.setup_capture"
    bl_description = "Handles face armature deformation"

    def execute(self, context):
        bpy.ops.wm.add_base_face_mesh(save_to_pointer=True)
        bpy.ops.wm.add_base_face_armature(save_to_pointer=True)
        bind_mesh_and_armature(context)
        bpy.ops.wm.face_analysis()

        return {'FINISHED'}
        
        
def register():
    bpy.utils.register_class(SEICHE_OT_setup_capture)

def unregister():
    bpy.utils.unregister_class(SEICHE_OT_setup_capture)