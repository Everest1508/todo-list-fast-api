from fastapi import APIRouter, HTTPException, status
from api.models.user import User
from api.schemas.user import UserRegister, UserLogin,UserResponse
from pydantic import BaseModel
import jwt
from datetime import datetime, timedelta

auth_router = APIRouter(prefix="/api/auth", tags=["Authentication"])

# Pydantic model for user response


# Secret key for JWT
SECRET_KEY = "your-secret-key"
# Token expiration time (in minutes)
TOKEN_EXPIRE_MINUTES = 30

# Generate JWT token
def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm="HS256")
    return encoded_jwt

# Route for user registration
@auth_router.post("/register", response_model=UserResponse)
async def register_user(user_data: UserRegister):
    # Check if the email is already registered
    if await User.filter(email=user_data.email).exists():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")
    # Create user
    user_obj = await User.create(username=user_data.username, email=user_data.email, password_hash=user_data.password)
    # Return user data
    return UserResponse(id=user_obj.id, username=user_obj.username, email=user_obj.email)

# Route for user login
@auth_router.post("/login")
async def login_user(user_data: UserLogin):
    # Check if the user with the provided email exists
    user_obj = await User.filter(email=user_data.email).first()
    if not user_obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    # Check if the password matches
    if not user_obj.password_hash == user_data.password:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect password")
    # Return some token or session data
    return {"message": "Login successful"}
