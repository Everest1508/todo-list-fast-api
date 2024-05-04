from fastapi import APIRouter, HTTPException, status
from api.models.user import User
from api.schemas.user import UserRegister, UserLogin

auth_router = APIRouter(prefix="/api/auth", tags=["Authentication"])

# Route for user registration
@auth_router.post("/register", response_model=User)
async def register_user(user_data: UserRegister):
    # Check if the email is already registered
    if await User.filter(email=user_data.email).exists():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")
    # Create user
    user_obj = await User.create(username=user_data.username, email=user_data.email, password=user_data.password)
    return user_obj

# Route for user login
@auth_router.post("/login")
async def login_user(user_data: UserLogin):
    # Check if the user with the provided email exists
    user_obj = await User.filter(email=user_data.email).first()
    if not user_obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    # Check if the password matches
    if not user_obj.check_password(user_data.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect password")
    # Return some token or session data
    return {"message": "Login successful"}
