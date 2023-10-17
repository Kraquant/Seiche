import bpy
import bmesh
from math import radians
from bpy_extras.object_utils import AddObjectHelper
from ..other.face_mesh_data import get_face_mesh

from bpy.props import (
    FloatProperty,
)


class SEICHE_OT_add_base_face_mesh(bpy.types.Operator, AddObjectHelper):
    bl_label = "Add base face mesh"
    bl_idname = "wm.add_base_face_mesh"
    bl_description = "Creates the face mesh used by the MediaPipe library"
    bl_options = {'REGISTER', 'UNDO'}

    width: FloatProperty(
        name="Width",
        description="Box Width",
        min=0.01, max=100.0,
        default=1.0,
    )
    height: FloatProperty(
        name="Height",
        description="Box Height",
        min=0.01, max=100.0,
        default=1.0,
    )
    depth: FloatProperty(
        name="Depth",
        description="Box Depth",
        min=0.01, max=100.0,
        default=1.0,
    )

    save_to_pointer: bpy.props.BoolProperty(
        name="Save to the pointer",
        description="Save to the addon mesh pointer",
        default=False
    )

    def execute(self, context):

        verts_loc, faces = get_face_mesh(
            self.width,
            self.height,
            self.depth,
        )

        mesh = bpy.data.meshes.new("Face")

        bm = bmesh.new()

        for v_co in verts_loc:
            bm.verts.new(v_co)

        bm.verts.ensure_lookup_table()
        for f_idx in faces:
            bm.faces.new([bm.verts[i-1] for i in f_idx])

        bm.to_mesh(mesh)
        mesh.update()

        # add the mesh as an object into the scene with this utility module
        from bpy_extras import object_utils
        face_obj =  object_utils.object_data_add(context, mesh, operator=self)

        
        # Rotate the face by 90 degrees
        # face_obj.rotation_euler = (radians(90), 0, 0)
        #bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        
        if self.save_to_pointer:
            context.scene.seiche_settings.target_mesh = face_obj

        return {'FINISHED'}


def register():
    bpy.utils.register_class(SEICHE_OT_add_base_face_mesh)


def unregister():
    bpy.utils.unregister_class(SEICHE_OT_add_base_face_mesh)