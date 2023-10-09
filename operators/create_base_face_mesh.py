import bpy
import bmesh
from bpy_extras.object_utils import AddObjectHelper
from ..other.faceMesh import add_face

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

    def execute(self, context):

        verts_loc, faces = add_face(
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
        object_utils.object_data_add(context, mesh, operator=self)

        return {'FINISHED'}


def menu_func(self, context):
    self.layout.operator(SEICHE_OT_add_base_face_mesh.bl_idname, icon='MESH_MONKEY')


# Register and add to the "add mesh" menu (required to use F3 search "Add Box" for quick access).
def register():
    bpy.utils.register_class(SEICHE_OT_add_base_face_mesh)
    bpy.types.VIEW3D_MT_mesh_add.append(menu_func)


def unregister():
    bpy.utils.unregister_class(SEICHE_OT_add_base_face_mesh)
    bpy.types.VIEW3D_MT_mesh_add.remove(menu_func)


if __name__ == "__main__":
    register()