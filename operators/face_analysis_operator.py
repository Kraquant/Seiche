import bpy
import cv2
from ..other.Utilities import *
from ..other.FaceMeshModule import FaceMeshDetector

class SEICHE_OT_face_analysis(bpy.types.Operator):
    bl_label = "Face analysis Operator"
    bl_idname = "wm.face_analysis"
    bl_description = "Handles face analysis"

    _timer = None
    _cap = None
    _video_utilities = None
    _face_mesh_detector = FaceMeshDetector()
    _window_name = "Camera View"

    is_camera_running : bpy.props.BoolProperty(
        name = "Is Camera Running",
        default=False)
    enable_feature_detection : bpy.props.BoolProperty(
        name = "Enable Feature Detection",
        default=True)

    def execute(self, context):

        if (SEICHE_OT_face_analysis._timer != None):
            self.cancel(context)
            return {'FINISHED'}

        self.init_camera(context)
        self.init_face_data_property(context)

        wm = context.window_manager
        SEICHE_OT_face_analysis._timer = wm.event_timer_add(0.01, window=context.window)
        wm.modal_handler_add(self)
        return {'RUNNING_MODAL'}
        

    def modal(self, context, event):
        
        if event.type != 'TIMER' and SEICHE_OT_face_analysis._timer != None:
            return {'PASS_THROUGH'}

        elif event.type != 'TIMER' and SEICHE_OT_face_analysis._timer == None:
            return {'FINISHED'}

        _, cam_image = SEICHE_OT_face_analysis._cap.read()
        cam_image, faces_screen_coords, faces_world_coords = SEICHE_OT_face_analysis._face_mesh_detector.findFaceMesh(cam_image, True)
        SEICHE_OT_face_analysis._video_utilities.print_fps(cam_image)
        cv2.imshow(SEICHE_OT_face_analysis._window_name, cam_image)
        cv2.waitKey(1)
        
        if len(faces_world_coords) > 0:
            self.write_face_data(context, faces_screen_coords[0], faces_world_coords[0]) # Just the first detected face

        return {'PASS_THROUGH'}
        
    
    def cancel(self, context):
        wm = context.window_manager
        wm.event_timer_remove(SEICHE_OT_face_analysis._timer)
        SEICHE_OT_face_analysis._timer = None
        cv2.destroyWindow(SEICHE_OT_face_analysis._window_name)
        SEICHE_OT_face_analysis._cap = None
        SEICHE_OT_face_analysis.is_camera_running = False
    
    def init_camera(self, context):
        user_camera_settings = context.scene.seiche_user_camera_settings

        if SEICHE_OT_face_analysis._cap == None:
            SEICHE_OT_face_analysis._cap = cv2.VideoCapture(user_camera_settings.camera_id)
            
            if not user_camera_settings.use_default_res:
                SEICHE_OT_face_analysis._cap.set(cv2.CAP_PROP_FRAME_WIDTH, user_camera_settings.camera_width)
                SEICHE_OT_face_analysis._cap.set(cv2.CAP_PROP_FRAME_HEIGHT, user_camera_settings.camera_height)

            SEICHE_OT_face_analysis._cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)

            SEICHE_OT_face_analysis._video_utilities = VideoUtilities()
            SEICHE_OT_face_analysis.is_camera_running=True
            # time.sleep(1.0)

    def init_face_data_property(self, context):
        
        face = context.scene.seiche_face_data.face
        face.clear()

        for i in range(SEICHE_face_data.vertices_number):
            item = face.add()
            item.mesh_id = i
            item.world_position = (0.0, 0.0, 0.0)
            item.screen_position = (0, 0)
    
    def write_face_data(self, context, screen_coords, world_coords):
        face = context.scene.seiche_face_data.face
        
        for i in range(SEICHE_face_data.vertices_number):
            face[i].screen_position = screen_coords[i]
            face[i].world_position = world_coords[i]


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
    face: bpy.props.CollectionProperty(
        type = SEICHE_face_vertex_info,
        name = "Face vertices positions"
    )

    vertices_number = 468


def register():
    bpy.utils.register_class(SEICHE_OT_face_analysis)
    bpy.utils.register_class(SEICHE_face_vertex_info)
    bpy.utils.register_class(SEICHE_face_data)

    bpy.types.Scene.seiche_face_data = bpy.props.PointerProperty(
            name='Face data',
            type=SEICHE_face_data)

    

def unregister():
    bpy.utils.unregister_class(SEICHE_face_data)
    bpy.utils.unregister_class(SEICHE_face_vertex_info)
    bpy.utils.unregister_class(SEICHE_OT_face_analysis)