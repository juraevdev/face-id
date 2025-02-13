from rest_framework import status
from rest_framework import mixins
from rest_framework import generics
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer
from .utils import encode_face, verify_face
from rest_framework.parsers import MultiPartParser

class UserCreateAPIView(generics.GenericAPIView):
    serializer_class = UserSerializer
    parser_classes = [MultiPartParser]

    def post(self, request, *args, **kwargs):
        face_image = request.FILES.get('face_image')
        if not face_image:
            return Response({"error": "Face image is required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            face_encoding = encode_face(face_image)
            if face_encoding is None:
                return Response({"error": "No face detected."}, status=status.HTTP_400_BAD_REQUEST)

            user_data = request.data.copy()
            user_data['face_encoding'] = face_encoding.tolist()  # NumPy array ni JSON formatga o'tkazish
            
            serializer = self.get_serializer(data=user_data)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "User created successfully."}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            print("Error:", str(e))
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class UserUpdateAPIView(generics.GenericAPIView):
    serializer_class = UserSerializer
    parser_classes = [MultiPartParser]

    def get_object(self):
        # Userni olish uchun query param yoki URL'dan olib kelish
        return User.objects.get(id=self.kwargs['pk'])

    def put(self, request, *args, **kwargs):
        user = self.get_object()

        # Yuzni yangilash
        face_image = request.FILES.get('face_image')
        if face_image:
            if verify_face(face_image, user.face_encoding):
                user.face_encoding = encode_face(face_image)
                user.save()

        # Userni yangilash
        return self.update(request, *args, **kwargs)
