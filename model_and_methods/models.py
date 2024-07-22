from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "mysql+mysqlconnector://root:root@127.0.0.1/user_management"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    password = Column(String(50), nullable=False)
    is_admin = Column(Boolean, default=0)

    user_type = Column(String(50))  # * Guest, Worker, Employee

    full_name = Column(String(50))
    contact_number = Column(String(50))
    national_id = Column(String(50))

    is_helmet_check = Column(String(50), default="disable")
    is_helmet_verify = Column(Boolean, default=0)
    helmet_voilation_count = Column(Integer, default=0)

    is_vest_check = Column(String(50), default="disable")
    is_vest_verify = Column(Boolean, default=0)
    vest_voilation_count = Column(Integer, default=0)

    is_goggles_check = Column(String(50), default="disable")
    is_goggles_verify = Column(Boolean, default=0)
    goggles_Voilation_count = Column(Integer, default=0)

    is_gloves_check = Column(String(50), default="disable")
    is_gloves_verify = Column(Boolean, default=0)
    gloves_voilation_count = Column(Integer, default=0)

    is_boot_check = Column(String(50), default="disable")
    is_boot_verify = Column(Boolean, default=0)
    boot_voilation_count = Column(Integer, default=0)

    total_violation_count = Column(Integer, default=0)


# Create the database tables
Base.metadata.create_all(bind=engine)
