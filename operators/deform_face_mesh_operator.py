import bpy
import cv2
from ..other import face_mesh_data

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

        face_vertices = context.scene.seiche_settings.detection_settings.face_data[-1].face_vertices
        ob = context.scene.seiche_settings.target_mesh
        me = ob.data
        for i in range(face_mesh_data.vertices_number):
            me.vertices[i].co = face_vertices[i].world_position[:]

        return {'PASS_THROUGH'}
    
    def cancel(self, context):
        wm = context.window_manager
        wm.event_timer_remove(SEICHE_OT_deform_face_mesh._timer)
        SEICHE_OT_deform_face_mesh._timer = None
    
    
    
    @classmethod
    def poll(cls, context):
        return context.scene.seiche_settings.target_mesh != None

def register():
    bpy.utils.register_class(SEICHE_OT_deform_face_mesh)

def unregister():
    bpy.utils.unregister_class(SEICHE_OT_deform_face_mesh)