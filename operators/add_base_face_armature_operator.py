import bpy
from bpy_extras.object_utils import AddObjectHelper
from ..other.face_mesh_data import vertices_number

class SEICHE_OT_add_base_face_armature(bpy.types.Operator, AddObjectHelper):
    bl_label = "Add base face armature"
    bl_idname = "wm.add_base_face_armature"
    bl_description = "Creates the face armature used by Seiche"
    bl_options = {'REGISTER', 'UNDO'}

    armature_name: bpy.props.StringProperty(
        name="Collection Name",
        description="The base name for the collection",
        default= "Face rig"
    )

    bones_base_name: bpy.props.StringProperty(
        name="Empties base denomination Name",
        description="The base name for the collection",
        default= "face_bone_"
    )

    save_to_pointer: bpy.props.BoolProperty(
        name="Save to the pointer",
        description="Save to the addon armature pointer",
        default=False
    )

    def execute(self, context):
        
        # Create the armature
        armature_data = bpy.data.armatures.new(self.armature_name)
        armature = bpy.data.objects.new(self.armature_name + ' Object', armature_data)
        
        # Link armature to the scene
        scene = bpy.context.scene
        scene.collection.objects.link(armature)

        # Adding bones
        # Set the armature as the active object
        bpy.context.view_layer.objects.active = armature

        # Enter Edit Mode to add a bone
        bpy.ops.object.mode_set(mode='EDIT')
        
        for i in range(vertices_number):
            ebs = armature.data.edit_bones
            eb = ebs.new(self.bones_base_name + str(i+1))
            eb.head = (0, 0, 0)
            eb.tail = (0, 0.1, 0)
        
        if self.save_to_pointer:
            context.scene.seiche_settings.target_armature = armature_data
        
        return {'FINISHED'}



def register():
    bpy.utils.register_class(SEICHE_OT_add_base_face_armature)


def unregister():
    bpy.utils.unregister_class(SEICHE_OT_add_base_face_armature)