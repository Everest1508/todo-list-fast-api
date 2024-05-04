from fastapi import APIRouter, HTTPException, status,Depends
from api.models.user import User
from api.schemas.user import UserRegister, UserLogin,UserResponse
from api.utils.authentications import get_current_user,create_access_token
import jwt
import bcrypt 
auth_router = APIRouter(prefix="/api/auth", tags=["Authentication"])

@auth_router.get("/user", response_model=UserResponse)
async def get_user(user: User = Depends(get_current_user)):
    return user

@auth_router.post("/register", response_model=UserResponse)
async def register_user(user_data: UserRegister):
    if await User.filter(email=user_data.email).exists():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")
    hashed_password = bcrypt.hashpw(user_data.password.encode('utf-8'), bcrypt.gensalt())
  
    user_obj = await User.create(username=user_data.username, email=user_data.email, password_hash=str(hashed_password))
    return UserResponse(id=user_obj.id, username=user_obj.username, email=user_obj.email)

@auth_router.post("/login")
async def login_user(user_data: UserLogin):
    user_obj = await User.filter(email=user_data.email).first()
    if not user_obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    if not bcrypt.checkpw(user_data.password.encode('utf-8'), user_obj.password_hash[2:-1].encode('utf-8')):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect password")
    token = create_access_token({"sub": user_obj.email})
    return {"access_token": token, "token_type": "bearer"}
