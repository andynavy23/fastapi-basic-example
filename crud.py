from sqlalchemy.orm import Session
from models.user_sqlite import User
from schemas.user import User as UserSchema

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.user_id == user_id)

def get_users(db: Session):
    return db.query(User).all()
    
def craete_user(db: Session, user_in: UserSchema):
    created_user = User(**user_in.dict())

    db.add(created_user)
    db.commit()
    db.refresh(created_user)
