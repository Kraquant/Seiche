import bpy
from ..operators import add_base_face_empties_operator
from ..operators import add_base_face_armature_operator
from ..operators import add_base_face_mesh_operator

class SEICHE_MT_objects_menu(bpy.types.Menu):
    bl_label = "Seiche objects menu"
    bl_idname = "SEICHE_MT_objects_menu"

    def draw(self, context):
        self.layout.operator(add_base_face_empties_operator.SEICHE_OT_add_base_face_empties.bl_idname, icon='MESH_MONKEY')
        self.layout.operator(add_base_face_armature_operator.SEICHE_OT_add_base_face_armature.bl_idname, icon='MESH_MONKEY')
        self.layout.operator(add_base_face_mesh_operator.SEICHE_OT_add_base_face_mesh.bl_idname, icon='MESH_MONKEY')



def draw_menu(self, context):
    self.layout.menu(SEICHE_MT_objects_menu.bl_idname)


def register():
    bpy.utils.register_class(SEICHE_MT_objects_menu)
    bpy.types.VIEW3D_MT_mesh_add.append(draw_menu)

def unregister():
    bpy.utils.unregister_class(SEICHE_MT_objects_menu)  
    bpy.types.VIEW3D_MT_mesh_add.remove(draw_menu)