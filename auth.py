from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, status
from sqlalchemy.orm import Session
from typing import List
import numpy as np
from jose import JWTError, jwt

from database import get_db
from models import User
from schemas import UserSchema
from utils import encode_face, verify_face
from helper import create_access_token, create_refresh_token, get_current_user

router = APIRouter()

@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register_user(
    username: str,
    email: str,
    face_image: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    face_encoding = encode_face(face_image.file)
    if face_encoding is None:
        raise HTTPException(status_code=400, detail="No face detected.")
    
    existing_user = db.query(User).filter(User.email == email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists.")
    
    new_user = User(username=username, email=email, face_encoding=face_encoding.tolist())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "User registered successfully", "user": UserSchema.from_orm(new_user)}

@router.put("/update/{user_id}", status_code=status.HTTP_200_OK)
async def update_user(
    user_id: int,
    face_image: UploadFile = File(None),
    username: str = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=400, detail="User not found.")
    
    if face_image:
        if verify_face(face_image.file, user.face_encoding):
            user.face_encoding = encode_face(face_image.file).tolist()
        else:
            raise HTTPException(status_code=400, detail="Face verification failed.")
        
    if username:
        user.username = username

    db.commit()
    db.refresh(user)

    return {"message": "User updated successfully", "user": UserSchema.from_orm(user)}

@router.post("/login", status_code=status.HTTP_200_OK)

async def login(face_image: UploadFile = File(...), db: Session = Depends(get_db)):
    face_encoding = encode_face(face_image.file)
    if face_encoding is None:
        raise HTTPException(status_code=400, detail="No face detected.")

    users = db.query(User).all()
    for user in users:
        if verify_face(face_image.file, user.face_encoding):
            access_token = create_access_token(data={"sub": user.email})
            refresh_token = create_refresh_token(data={"sub": user.email})

            return {
                "message": "Login successful",
                "access_token": access_token,
                "refresh_token": refresh_token,
            }
        
    raise HTTPException(status_code=401, detail="Face not recognized.")

@router.post("/logout", status_code=status.HTTP_200_OK)
async def logout(current_user: User = Depends(get_current_user)):
    return {"message": "Logout successful"}