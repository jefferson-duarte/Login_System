from .model_orm import RegisterCustomer
from .sessions import return_session

session = return_session()


class Register:

    @classmethod
    def save(cls, name, email, password):
        customer = RegisterCustomer(name=name, email=email, password=password)
        session.add(customer)
        session.commit()
