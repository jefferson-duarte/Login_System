from controller.register import ControllerLogin, ControllerRegister


def login_user():
    user = ControllerLogin()

    while True:

        email = input('Insert your email: ')
        password = input('Insert your password: ')

        user.login_user(email=email, password=password)
