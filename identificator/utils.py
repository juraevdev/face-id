import face_recognition
import cv2
import numpy as np

def encode_face(image_file):
    image = face_recognition.load_image_file(image_file)
    face_encodings = face_recognition.face_encodings(image)
    if face_encodings:
        return face_encodings[0]
    return None

def verify_face(image_file, user_encoding):

    new_face_encoding = encode_face(image_file)
    if new_face_encoding is None:
        return False
    return face_recognition.compare_faces([user_encoding], new_face_encoding)[0]