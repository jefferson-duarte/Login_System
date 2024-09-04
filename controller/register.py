from sqlalchemy.exc import NoResultFound

from database import model_orm, register, sessions
from hash_generation import hash_password, verify_password


class ControllerRegister:
    def register_user(self, name: str, email: str, password: str, confirm_password: str):  # noqa:E501
        session = sessions.return_session()

        stored_hash = hash_password(password)
        is_valid = verify_password(stored_hash, confirm_password)

        try:
            session.query(model_orm.RegisterCustomer).filter(
                model_orm.RegisterCustomer.email == email
            ).one()
            return print('Email already registed.')

        except NoResultFound:
            if is_valid:
                register.Register.save(name, email, stored_hash)
                return True
            return print('Password and confirm password does not match.')


class ControllerLogin:
    def login_user(self, email: str, password: str) -> bool:
        session = sessions.return_session()
        stored_hash = hash_password(password)

        try:
            session.query(model_orm.RegisterCustomer).filter_by(
                email=email, password=stored_hash
            ).one()
            return True

        except NoResultFound:
            return False
