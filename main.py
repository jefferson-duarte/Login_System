from utils import clean_screen
from view.sistem_views import login_view, register_view

while True:
    clean_screen()

    print('~' * 30)
    print(f'{" Login Sistem ": ^30}')
    print('~' * 30)

    option = int(input(
        '[1] - Login\n'
        '[2] - Register\n'
        '[3] - Exit\n'
        '==============================\n'
    ))

    match option:
        case 1:
            login_view()
        case 2:
            register_view()
        case 3:
            break
