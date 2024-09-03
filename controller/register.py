# import os
# import sys

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) # noqa:E501

from sqlalchemy.exc import NoResultFound

from database import model_orm, register, sessions

# from database.model_orm import RegisterCustomer
# from database.register import Register
# from database.sessions import return_session


class ControllerRegister:
    def register_user(self, name, email, password, confirm_password):
        session = sessions.return_session()

        if password != confirm_password:
            return print('Password and confirm password does not match.')

        try:
            session.query(model_orm.RegisterCustomer).filter(
                model_orm.RegisterCustomer.email == email
            ).one()
            return print('Email already registed.')

        except NoResultFound:
            register.Register.save(name, email, password)
            return print(f'User "{name}" registed successfully.')


class ControllerLogin:
    def login_user(self, email, password):
        session = sessions.return_session()

        try:
            session.query(model_orm.RegisterCustomer).filter_by(
                email=email, password=password
            ).one()

            return print('Login successfully.')

        except NoResultFound:
            return print('Email or password invalid.')
