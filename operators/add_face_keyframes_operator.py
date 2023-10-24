import bpy
import bmesh
from ..other import face_mesh_data
from ..other.utils import get_armature_pose_bones

class SEICHE_OT_add_face_keyframes(bpy.types.Operator):
    bl_label = "Add face keyframes"
    bl_idname = "wm.add_face_keyframes"
    bl_description = "Creates keyframes from previous face recording"
    bl_options = {'REGISTER', 'UNDO'}

    def get_record_values_bounds(self, record):
        values = None

        for data in record:
            for vertice in data.face_vertices:
                vert_pos = vertice.world_position
                if values == None:
                    values = [
                        vert_pos[0], # Min X
                        vert_pos[1], # Min Y
                        vert_pos[2], # Min Z
                        vert_pos[0], # Max X
                        vert_pos[1], # Max Y
                        vert_pos[2]  # Max Z
                    ]
                # Mins
                if vert_pos[0] < values [0]: values[0] = vert_pos[0]
                if vert_pos[1] < values [1]: values[1] = vert_pos[1]
                if vert_pos[2] < values [2]: values[2] = vert_pos[2]

                # Maxs
                if vert_pos[0] > values [3]: values[3] = vert_pos[0]
                if vert_pos[1] > values [4]: values[4] = vert_pos[1]
                if vert_pos[2] > values [5]: values[5] = vert_pos[2]
        return values

    def execute(self, context):
        settings = context.scene.seiche_settings
        record = settings.detection_settings.face_data
        render_fps = context.scene.render.fps
        
        bounds = self.get_record_values_bounds(record)
        record_size = len(record)
        step = 0
    
        # Animating the armature
        pose_bones = get_armature_pose_bones(context)
        bpy.ops.object.mode_set(mode='POSE')
        for data in record:
            step += 1
            print(f"Step: {step} / {record_size}")
            
            i = 0
            print(data.time)
            for bone in pose_bones:
                new_pos = data.face_vertices[i].world_position

                # Normalize the position
                centered_pos =  (new_pos[0] - bounds[0], new_pos[1] - bounds[1], new_pos[2] - bounds[2])
                bone.location = centered_pos
                
                bone.keyframe_insert(data_path="location", frame = data.time * render_fps)

                i += 1

        return {'FINISHED'}

   


def register():
    bpy.utils.register_class(SEICHE_OT_add_face_keyframes)


def unregister():
    bpy.utils.unregister_class(SEICHE_OT_add_face_keyframes)