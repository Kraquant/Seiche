import bpy

class SEICHE_PT_face_detection(bpy.types.Panel):
    bl_label = "Face Detection"
    bl_idname = "SEICHE_PT_face_detection"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'FaceDetection'
    bl_parent_id = 'SEICHE_PT_main_panel'

    toggle_camera: bpy.props.BoolProperty(
        name="Toggle the camera",
        description="Save to the addon armature pointer",
        default=True
    )

    def draw(self, context):
        layout = self.layout
        settings = context.scene.seiche_settings.detection_settings


        split = layout.split()
        col = split.column()
        col.operator("wm.face_analysis", text="Detect Face", icon="VIEW_CAMERA")
        col = split.column(align=True)
        col.prop(settings, "toggle_live_camera", text="Toggle Camera")

        row = layout.row(align=True)
        row.enabled = False
        row.prop(settings, "detection_fps", text="Camera capture FPS")

        row = layout.row()
        row.operator("wm.add_face_keyframes", text="Add Keyframes", icon="DECORATE_KEYFRAME")
        row.prop(context.scene.render, "fps", text="Frame Rate (FPS)")
        row.prop(context.scene, "frame_end", text="End Frame")


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
        camera_settings = context.scene.seiche_settings.detection_settings.user_camera_settings
        
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
