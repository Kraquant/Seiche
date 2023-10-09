import bpy

class SEICHE_PT_main_panel(bpy.types.Panel):
    bl_label = "Seiche"
    bl_idname = "SEICHE_PT_main_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'SeicheAddon'

    def draw(self, context):
        layout = self.layout
        row = layout.row()

def register():
    bpy.utils.register_class(SEICHE_PT_main_panel)

def unregister():
    bpy.utils.unregister_class(SEICHE_PT_main_panel)