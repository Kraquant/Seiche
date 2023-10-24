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

        
        
        

        row = layout.row(align=True)
        row.prop_search(context.scene.seiche_settings, "target_mesh", context.scene, "objects", text="Select Mesh")
        ope = row.operator("wm.add_base_face_mesh", text="Add mesh", icon="MESH_MONKEY")
        ope.save_to_pointer=True

        row = layout.row(align=True)
        row.prop_search(context.scene.seiche_settings, "target_empty", context.scene, "objects", text="Select Empty parent")
        ope = row.operator("wm.add_base_face_empties", text="Add empties", icon="MESH_MONKEY")
        ope.save_to_pointer=True

        row = layout.row(align=True)
        row.prop_search(context.scene.seiche_settings, "target_armature", context.scene, "objects", text="Select Armature")
        ope = row.operator("wm.add_base_face_armature", text="Add armature", icon="MESH_MONKEY")
        ope.save_to_pointer=True

        row = layout.row()
        row.operator("wm.face_mesh_deform", text="Start realtime mesh deformation", icon="MESH_GRID")
        row.operator("wm.face_armature_deform", text="Start realtime armature deformation", icon="OUTLINER_OB_ARMATURE")
        

def register():
    bpy.utils.register_class(SEICHE_PT_facial_mesh)

def unregister():
    bpy.utils.unregister_class(SEICHE_PT_facial_mesh)