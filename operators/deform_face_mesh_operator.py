import bpy
import cv2
from .face_analysis_operator import SEICHE_face_data

class SEICHE_OT_deform_face_mesh(bpy.types.Operator):
    bl_label = "Face mesh deformation Operator"
    bl_idname = "wm.face_mesh_deform"
    bl_description = "Handles face mesh deformation"

    _timer = None

    def execute(self, context):
        if SEICHE_OT_deform_face_mesh._timer != None:
            self.cancel(context)
            return {'FINISHED'}
        
        print("Action ca tourne")


        wm = context.window_manager
        SEICHE_OT_deform_face_mesh._timer = wm.event_timer_add(0.01, window=context.window)
        wm.modal_handler_add(self)
        return {'RUNNING_MODAL'}

        

    def modal(self, context, event):
        if event.type != 'TIMER' and SEICHE_OT_deform_face_mesh._timer != None:
            return {'PASS_THROUGH'}

        elif event.type != 'TIMER' and SEICHE_OT_deform_face_mesh._timer == None:
            return {'FINISHED'}

        face = context.scene.seiche_face_data.face
        ob = bpy.context.view_layer.objects.active
        me = ob.data
        for i in range(SEICHE_face_data.vertices_number):
            me.vertices[i].co = face[i].world_position[:]


        return {'PASS_THROUGH'}
    
    def cancel(self, context):
        wm = context.window_manager
        wm.event_timer_remove(SEICHE_OT_deform_face_mesh._timer)
        SEICHE_OT_deform_face_mesh._timer = None



def register():
    bpy.utils.register_class(SEICHE_OT_deform_face_mesh)

def unregister():
    bpy.utils.unregister_class(SEICHE_OT_deform_face_mesh)