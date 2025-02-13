from rest_framework import viewsets
from .models import User
from .utils import encode_face, verify_face
from rest_framework.response import Response
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        face_image = request.FILES.get('face_image') 
        if not face_image:
            return Response({"error": "Face image is required."}, status=400)
        
        face_encoding = encode_face(face_image)
        if face_encoding is None:
            return Response({"error": "No face detected."}, status=400)

        user = User.objects.create(
            username=request.data['username'],
            email=request.data['email'],
            face_encoding=face_encoding
        )
        return Response({"message": "User created successfully."}, status=201)

    def perform_update(self, serializer):

        face_image = self.request.FILES.get('face_image')
        if face_image:
            user = self.get_object()
            if verify_face(face_image, user.face_encoding):
                user.face_encoding = encode_face(face_image)
                user.save()
        super().perform_update(serializer)