bl_info = {
    "name" : "Seiche",
    "author" : "Kerlink",
    "version" : (1, 0),
    "blender" : (3, 6, 3),
    "location" : "View3d > Tool",
    "warning" : "",
    "wiki_url" : "",
    "category" : "Facial Animation",
}

import bpy

# Panels
from .panels import seiche_main_panel
from .panels import seiche_face_detection_panel
from .panels import seiche_facial_mesh_panel

# Operators
from .operators import add_base_face_armature_operator
from .operators import add_base_face_empties_operator
from .operators import add_base_face_mesh_operator
from .operators import add_face_keyframes_operator
from .operators import deform_face_armature_operator
from .operators import deform_face_mesh_operator
from .operators import face_analysis_operator
from .operators import setup_capture_operator

# Menu
from .menus import add_seiche_object_menu

# Others
from .other import utils
from .other import seiche_custom_properties

def register():
    # Others
    # utils.register()
    seiche_custom_properties.register()

    # Panels
    seiche_main_panel.register()
    seiche_face_detection_panel.register()
    seiche_facial_mesh_panel.register()

    # Operators
    add_base_face_armature_operator.register()
    add_base_face_empties_operator.register()
    add_base_face_mesh_operator.register()
    add_face_keyframes_operator.register()
    deform_face_armature_operator.register()
    deform_face_mesh_operator.register()
    face_analysis_operator.register()
    setup_capture_operator.register()


    # Menu
    add_seiche_object_menu.register()

    

def unregister():
    # Others
    # utils.unregister()
    seiche_custom_properties.unregister()

    # Panels
    seiche_face_detection_panel.unregister()
    seiche_facial_mesh_panel.unregister()
    seiche_main_panel.unregister()

    # Operators
    add_base_face_armature_operator.unregister()
    add_base_face_empties_operator.unregister()
    add_base_face_mesh_operator.unregister()
    add_face_keyframes_operator.unregister()
    deform_face_armature_operator.unregister()
    deform_face_mesh_operator.unregister()
    face_analysis_operator.unregister()
    setup_capture_operator.unregister()

    # Menu
    add_seiche_object_menu.unregister()

if __name__ == "__main__":
    register()