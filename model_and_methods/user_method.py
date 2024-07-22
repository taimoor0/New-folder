from model_and_methods.models import SessionLocal, User


class UserMethod:
    def __init__(self):
        self.db = SessionLocal()

    def create_user(
        self,
        username,
        password,
        full_name,
        contact_number,
        national_id,
    ):
        user = User(
            username=username,
            password=password,
            full_name=full_name,
            contact_number=contact_number,
            national_id=national_id,
        )
        try:
            self.db.add(user)
            self.db.commit()
            return True
        except:
            self.db.rollback()
            return False

    def get_user(self, username):
        return self.db.query(User).filter(User.username == username).first()

    def get_all_user(self):
        return self.db.query(User).filter(User.is_admin == False)

    def get_user_by_username(self, username):
        return self.db.query(User).filter(User.username == username).first()

    def get_user_by_id(self, user_id):
        return self.db.query(User).filter(User.user_id == user_id).first()

    def update_user(self, user):
        try:
            self.db.merge(user)
            self.db.commit()
        except:
            self.db.rollback()
            raise

    def update_user_by_admin(
        self,
        user_id,
        username,
        full_name,
        contact_number,
        national_id,
        user_type,
        is_helmet_check,
        is_vest_check,
        is_goggles_check,
        is_gloves_check,
        is_boot_check,
    ):
        try:
            user = self.db.query(User).filter(User.user_id == user_id).first()
            if user:
                user.username = username
                user.full_name = full_name
                user.contact_number = contact_number
                user.national_id = national_id
                user.user_type = user_type
                user.is_helmet_check = is_helmet_check
                user.is_vest_check = is_vest_check
                user.is_goggles_check = is_goggles_check
                user.is_gloves_check = is_gloves_check
                user.is_boot_check = is_boot_check
                self.db.commit()
                return True
            return False
        except Exception as e:
            self.db.rollback()
            print(f"Error updating user: {e}")
            return False

    def create_user_by_admin(
        self,
        username,
        password,
        full_name,
        contact_number,
        national_id,
        user_type,
        is_helmet_check,
        is_vest_check,
        is_goggles_check,
        is_gloves_check,
        is_boot_check,
    ):
        try:
            new_user = User(
                username=username,
                password=password,
                full_name=full_name,
                contact_number=contact_number,
                national_id=national_id,
                user_type=user_type,
                is_helmet_check=is_helmet_check,
                is_vest_check=is_vest_check,
                is_goggles_check=is_goggles_check,
                is_gloves_check=is_gloves_check,
                is_boot_check=is_boot_check,
            )
            self.db.add(new_user)
            self.db.commit()
            return True
        except Exception as e:
            self.db.rollback()
            print(f"Error adding user: {e}")
            return False

    def delete_user(self, user_id):
        try:

            result = self.db.query(User).filter(User.user_id == user_id).delete()
            self.db.commit()
            return result
        except Exception as e:
            self.db.rollback()
            print(f"Error: {e}")
            return False

    def close(self):
        self.db.close()
