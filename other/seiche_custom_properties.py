import bpy

def armature_filter(self, object):
    return object.type == 'ARMATURE'
def empty_filter(self, object):
    return object.type == 'EMPTY'
def mesh_filter(self, object):
    return object.type == 'MESH'


class SEICHE_face_vertex_info(bpy.types.PropertyGroup):
    mesh_id: bpy.props.IntProperty(
        name="Vertex Index",
        default = 0,
        description="Represents the vertex index")

    world_position: bpy.props.FloatVectorProperty(
        name="3D world positions",
        size=3)

    screen_position: bpy.props.IntVectorProperty(
        name="Picture pixel position",
        size=2
    )

class SEICHE_face_data(bpy.types.PropertyGroup):
    face_vertices: bpy.props.CollectionProperty(
        type = SEICHE_face_vertex_info,
        name = "Face vertices positions"
    )

    time: bpy.props.FloatProperty(
        name="Recorded time")

class SEICHE_camera_settings(bpy.types.PropertyGroup):
    camera_width: bpy.props.IntProperty(
        name="Camera width",
        default = 600,
        min = 0,
        max = 10000,
        description="Represents the camera width")

    use_default_res: bpy.props.BoolProperty(
        name="Use default cam resolution",
        default=True,
    )

    camera_height: bpy.props.IntProperty(
        name="Camera height",
        default = 600,
        min = 0,
        max = 10000,
        description="Represents the camera height")

    camera_id: bpy.props.IntProperty(
        name="Camera id",
        default = 1,
        description="Represents the camera id")

class SEICHE_face_detection_settings(bpy.types.PropertyGroup):
    user_camera_settings: bpy.props.PointerProperty(
        name='User camera settings',
        type=SEICHE_camera_settings)

    toggle_live_camera: bpy.props.BoolProperty(
        name='Toggle camera on',
        default=True)
    
    face_data: bpy.props.CollectionProperty(
        name='Face data',
        type=SEICHE_face_data)

    detection_fps: bpy.props.FloatProperty(
        name='Detection framerate',
        default=False
    )


class SEICHE_settings(bpy.types.PropertyGroup):
    
    detection_settings: bpy.props.PointerProperty(
        name='Face detection settings',
        type=SEICHE_face_detection_settings)
    
    target_mesh: bpy.props.PointerProperty(
        name='Target Mesh',
        type=bpy.types.Object,
        poll=mesh_filter)
    
    target_armature: bpy.props.PointerProperty(
        name='Target Armature',
        type=bpy.types.Armature,
        poll=armature_filter)
    
    target_empty: bpy.props.PointerProperty(
        name='Target Empty Parent',
        type=bpy.types.Object,
        poll=empty_filter)

classes = [
    SEICHE_face_vertex_info,
    SEICHE_face_data,
    SEICHE_camera_settings,
    SEICHE_face_detection_settings,
    SEICHE_settings
]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.Scene.seiche_settings = bpy.props.PointerProperty(
        name='Seiche addon settings',
        type=SEICHE_settings)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)