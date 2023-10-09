bl_info = {
    "name" : "Face Detection",
    "author" : "Kerlink",
    "version" : (1, 0),
    "blender" : (3, 6, 3),
    "location" : "View3d > Tool",
    "warning" : "",
    "wiki_url" : "",
    "category" : "Facial Animation",
}

import bpy
from .panels import seiche_main_panel
from .panels import facial_mesh_panel
from .panels import face_detection_panel
from .operators import face_analysis_operator
from .operators import create_base_face_mesh
from .operators import deform_face_mesh_operator
from .other import Utilities

def register():
    # Panels
    seiche_main_panel.register()
    facial_mesh_panel.register()
    face_detection_panel.register()

    # Operators
    face_analysis_operator.register()
    create_base_face_mesh.register()
    deform_face_mesh_operator.register()

    # Others
    Utilities.register()

def unregister():
    # Panels
    seiche_main_panel.unregister()
    facial_mesh_panel.unregister()
    face_detection_panel.unregister()

    # Operators
    face_analysis_operator.unregister()
    create_base_face_mesh.unregister()
    deform_face_mesh_operator.unregister()

    # Others
    Utilities.unregister()


if __name__ == "__main__":
    register()