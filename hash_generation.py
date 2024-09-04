import hashlib


def hash_password(password):
    # Gera o hash da senha
    return hashlib.sha256(password.encode('utf-8')).hexdigest()


def verify_password(stored_password, provided_password):
    # Compara o hash da senha fornecida com o hash armazenado
    return stored_password == hash_password(provided_password)
