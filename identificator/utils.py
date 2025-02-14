import face_recognition
import numpy as np
from PIL import Image

def encode_face(image):
    try:
        # Rasmni ochish va RGB formatga o‘tkazish
        image = Image.open(image).convert("RGB")

        # NumPy array ga o‘tkazish va uint8 formatda saqlash
        image = np.array(image, dtype=np.uint8).copy()

        # Face encoding olish
        face_encodings = face_recognition.face_encodings(image)

        if face_encodings:
            return face_encodings[0]
        return None

    except Exception as e:
        print("Encoding error:", str(e))
        return None

def verify_face(image_file, user_encoding):
    new_face_encoding = encode_face(image_file)
    if new_face_encoding is None:
        return False
    return face_recognition.compare_faces([np.array(user_encoding)], new_face_encoding)[0]

