from sqlalchemy.exc import NoResultFound

from database import model_orm, register, sessions


class ControllerRegister:
    def register_user(self, name: str, email: str, password: str, confirm_password: str):  # noqa:E501
        session = sessions.return_session()

        try:
            session.query(model_orm.RegisterCustomer).filter(
                model_orm.RegisterCustomer.email == email
            ).one()
            return print('Email already registed.')

        except NoResultFound:
            if password == confirm_password:
                register.Register.save(name, email, password)
                return True
            return print('Password and confirm password does not match.')


class ControllerLogin:
    def login_user(self, email: str, password: str) -> bool:
        session = sessions.return_session()

        try:
            session.query(model_orm.RegisterCustomer).filter_by(
                email=email, password=password
            ).one()
            return True

        except NoResultFound:
            return False
