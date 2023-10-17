import bpy
from bpy_extras.object_utils import AddObjectHelper
from ..other.face_mesh_data import vertices_number


class SEICHE_OT_add_base_face_empties(bpy.types.Operator, AddObjectHelper):
    bl_label = "Add base face empties"
    bl_idname = "wm.add_base_face_empties"
    bl_description = "Creates the face empties used by Seiche"
    bl_options = {'REGISTER', 'UNDO'}

    parent_name: bpy.props.StringProperty(
        name="Parent Name",
        description="The base name for the parent object",
        default= "Face empties"
    )

    empties_base_name: bpy.props.StringProperty(
        name="Empties base denomination Name",
        description="Empties prefix",
        default= "face_mesh_empty_"
    )

    save_to_pointer: bpy.props.BoolProperty(
        name="Save to the pointer",
        description="Save to the addon empty pointer",
        default=False
    )

    "Face empties"
    def execute(self, context):

        empty_parent = bpy.data.objects.new(name=self.parent_name, object_data=None)
        
        for i in range(vertices_number):
            new_empty_name = self.empties_base_name + str(i+1)
            new_empty = bpy.data.objects.new(name=new_empty_name, object_data=None)
            context.scene.collection.objects.link(new_empty)
            new_empty.parent = empty_parent
        

        context.scene.collection.objects.link(empty_parent)
        if self.save_to_pointer:
            context.scene.seiche_settings.target_empty = empty_parent

        return {'FINISHED'}

    # def create_blender_collection(self, name):
        
    #     if name not in bpy.data.collections:
    #         empty_collection = bpy.data.collections.new(name)
    #     else:
    #         empty_collection = bpy.data.collections[name]
            
    #     # Link the new collection to the current scene's collection hierarchy
    #     scene = bpy.context.scene
    #     scene.collection.children.link(empty_collection)
    #     empty_collection.name = name



def register():
    bpy.utils.register_class(SEICHE_OT_add_base_face_empties)


def unregister():
    bpy.utils.unregister_class(SEICHE_OT_add_base_face_empties)
