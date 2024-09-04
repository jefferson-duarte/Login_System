from time import sleep

from controller.register import ControllerLogin, ControllerRegister
from utils import clean_screen


def login_view():
    user = ControllerLogin()

    while True:
        clean_screen()

        print('#' * 30)
        print(f'{" Login ": ^30}')
        print('#' * 30)

        email = input('Insert your email: ')
        password = input('Insert your password: ')

        logged = user.login_user(email=email, password=password)

        if logged:
            print('Login successfully.')
            sleep(5)
            break
        print('Email or password invalid.')
        sleep(5)


def register_view():
    user = ControllerRegister()

    while True:
        clean_screen()

        print('#' * 30)
        print(f'{" Register ": ^30}')
        print('#' * 30)

        name = input('Insert your name: ')
        email = input('Insert your email: ')
        password = input('Insert your password: ')
        confirm_password = input('Repeat your password: ')

        register = user.register_user(
            name=name, email=email, password=password, confirm_password=confirm_password  # noqa:E501
        )

        if register:
            print(f'User "{name}" registed successfully.')
            sleep(5)
            break
