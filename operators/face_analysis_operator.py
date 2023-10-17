import bpy
import cv2
from ..other.utils import *
from ..other.face_mesh_module import FaceMeshDetector
from ..other import face_mesh_data

class SEICHE_OT_face_analysis(bpy.types.Operator):
    bl_label = "Face analysis Operator"
    bl_idname = "wm.face_analysis"
    bl_description = "Handles face analysis"

    _timer = None
    _cap = None
    _video_utilities = None
    _face_mesh_detector = FaceMeshDetector()
    _window_name = "Camera View"

    record_data: bpy.props.BoolProperty(
        name='Record the data to the empties',
        default=True)


    def execute(self, context):

        if (SEICHE_OT_face_analysis._timer != None):
            self.cancel(context)
            return {'FINISHED'}

        self.init_camera(context)
        context.scene.seiche_settings.detection_settings.face_data.clear() # Clear the registered values

        wm = context.window_manager
        SEICHE_OT_face_analysis._timer = wm.event_timer_add(0.01, window=context.window)
        wm.modal_handler_add(self)
        return {'RUNNING_MODAL'}
        

    def modal(self, context, event):
        
        if event.type != 'TIMER' and SEICHE_OT_face_analysis._timer != None:
            return {'PASS_THROUGH'}

        elif event.type != 'TIMER' and SEICHE_OT_face_analysis._timer == None:
            return {'FINISHED'}

        # 1: Reading the image from the camera
        _, cam_image = SEICHE_OT_face_analysis._cap.read()

        # 2: Analyzing the face features
        cam_image, faces_screen_coords, faces_world_coords = SEICHE_OT_face_analysis._face_mesh_detector.findFaceMesh(cam_image, True)

        # 3: Post-operations
        settings = context.scene.seiche_settings.detection_settings

        SEICHE_OT_face_analysis._video_utilities.register_image(cam_image, True)
        settings.detection_fps = SEICHE_OT_face_analysis._video_utilities.fps

        if settings.toggle_live_camera:
            cv2.imshow(SEICHE_OT_face_analysis._window_name, cam_image)
            cv2.waitKey(1)
    
        if len(faces_world_coords) > 0:
            self.save_data(
                context,
                faces_screen_coords[0],
                faces_world_coords[0],
                SEICHE_OT_face_analysis._video_utilities.time
            )

        return {'PASS_THROUGH'}
        

    def cancel(self, context):
        wm = context.window_manager
        wm.event_timer_remove(SEICHE_OT_face_analysis._timer)
        SEICHE_OT_face_analysis._timer = None
        # if cv2.getWindowProperty(SEICHE_OT_face_analysis._window_name, cv2.WND_PROP_VISIBLE) >= 0:
        cv2.destroyWindow(SEICHE_OT_face_analysis._window_name)
        SEICHE_OT_face_analysis._cap = None
    
    def init_camera(self, context):
        cam_settings = context.scene.seiche_settings.detection_settings.user_camera_settings

        if SEICHE_OT_face_analysis._cap == None:
            SEICHE_OT_face_analysis._cap = cv2.VideoCapture(cam_settings.camera_id)
            
            if not cam_settings.use_default_res:
                SEICHE_OT_face_analysis._cap.set(cv2.CAP_PROP_FRAME_WIDTH, cam_settings.camera_width)
                SEICHE_OT_face_analysis._cap.set(cv2.CAP_PROP_FRAME_HEIGHT, cam_settings.camera_height)

            SEICHE_OT_face_analysis._cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)

            SEICHE_OT_face_analysis._video_utilities = VideoUtilities()
            # time.sleep(1.0)
    
    def save_data(self, context, screen_coords, world_coords, time):
        new_face = context.scene.seiche_settings.detection_settings.face_data.add()
        new_face.time = time

        for i in range(face_mesh_data.vertices_number):
            new_vertex = new_face.face_vertices.add()
            new_vertex.mesh_id = i
            new_vertex.world_position = world_coords[i]
            new_vertex.screen_position = screen_coords[i]


def register():
    bpy.utils.register_class(SEICHE_OT_face_analysis)  

def unregister():
    bpy.utils.unregister_class(SEICHE_OT_face_analysis)