import bpy

class SEICHE_PT_facial_mesh(bpy.types.Panel):
    bl_label = "Facial Mesh"
    bl_idname = "SEICHE_PT_facial_mesh"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'FaceDetection'
    bl_parent_id= 'SEICHE_PT_main_panel'

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row = row.operator("wm.add_base_face_mesh", text="Add Base face Mesh", icon="MESH_MONKEY")
        row = layout.row()
        row = row.operator("wm.face_mesh_deform", text="Start mesh deformation", icon="MESH_GRID")
        row = layout.row()
        row = layout.prop(context.scene, 'seiche_user_camera_settings')
        row = layout.row()
        row = layout.prop(context.scene, "seiche_face_data")


def register():
    bpy.utils.register_class(SEICHE_PT_facial_mesh)

def unregister():
    bpy.utils.unregister_class(SEICHE_PT_facial_mesh)