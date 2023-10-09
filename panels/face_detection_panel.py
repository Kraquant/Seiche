import bpy

class SEICHE_PT_face_detection(bpy.types.Panel):
    bl_label = "Face Detection"
    bl_idname = "SEICHE_PT_face_detection"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'FaceDetection'
    bl_parent_id = 'SEICHE_PT_main_panel'

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row = row.operator("wm.face_analysis", text="Toggle open CV Camera", icon="VIEW_CAMERA")
        
        # Check if the operator has a property group

class SEICHE_PT_camera_property(bpy.types.Panel):
    bl_label = "Camera Properties"
    bl_idname = "SEICHE_PT_camera_property"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'FaceDetection'
    bl_parent_id = 'SEICHE_PT_face_detection'

    def __init__(self):
        self.cam_width = 0
        self.cam_height = 0


    def draw(self, context):
        layout = self.layout
        camera_settings = context.scene.seiche_user_camera_settings
        
        layout.label(text='Resolution') 
        row = layout.row(align= True)
        row.prop(camera_settings, "use_default_res")
        row.prop(camera_settings, "camera_width")
        row.prop(camera_settings, "camera_height")
        row = layout.row()
        layout.prop(camera_settings, "camera_id")

def register():
    bpy.utils.register_class(SEICHE_PT_face_detection)
    bpy.utils.register_class(SEICHE_PT_camera_property)

def unregister():
    bpy.utils.unregister_class(SEICHE_PT_face_detection)
    bpy.utils.unregister_class(SEICHE_PT_camera_property)
