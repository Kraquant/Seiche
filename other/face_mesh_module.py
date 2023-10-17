import cv2
import mediapipe as mp
import time

class FaceMeshDetector:

    def __init__(self, static_mode=False, max_faces=2, min_detection_con=0.5, min_track_con=0.5):
        self.staticMode = static_mode
        self.maxFaces = max_faces
        self.minDetectionCon = min_detection_con
        self.minTrackCon = min_track_con

        self.mpDraw = mp.solutions.drawing_utils
        self.mpFaceMesh = mp.solutions.face_mesh
        self.faceMesh = self.mpFaceMesh.FaceMesh(static_image_mode=self.staticMode,
                                                 max_num_faces=self.maxFaces,
                                                 min_detection_confidence=self.minDetectionCon,
                                                 min_tracking_confidence=self.minTrackCon)

        self.drawSpec = self.mpDraw.DrawingSpec(thickness=1, circle_radius=1)  # Drawing parameters

    def findFaceMesh(self, img, draw=True):

        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Convert the image format
        results = self.faceMesh.process(imgRGB)
        faces_pixels = []
        faces_coords = []

        if not results.multi_face_landmarks: return img, faces_pixels, faces_coords

        for faceLandmarks in results.multi_face_landmarks:
            face_pixels = []
            face_coords = []
            for vertexId, lm in enumerate(faceLandmarks.landmark):  # Each landmark in the face
                # Landmark values are normalized between 0 and 1
                ih, iw, ic = img.shape  # Height, Width, Depth
                x, y = int(lm.x * iw), int(lm.y * ih)
                face_pixels.append([x, y])
                face_coords.append([lm.x, lm.z, -lm.y])


            if draw:
                self.mpDraw.draw_landmarks(img, faceLandmarks, self.mpFaceMesh.FACEMESH_FACE_OVAL, self.drawSpec)

            faces_pixels.append(face_pixels)
            faces_coords.append(face_coords)

        return img, faces_pixels, faces_coords