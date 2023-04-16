from typing import List


def variable_no_utilizada():
    # la variablace C no se usa
    a = 1
    b = 2
    if a > b:
        a = b
    else:
        pass


def show_payments(payments: List[int]) -> str:
    # este es un comentario muy lagor y necesito formatearlos
    # a uno mas corot en dos lienas
    # se ben serparar para que se mas facil de leeer esto es un problemas
    result_payments: str = ""
    for payment in payments:
        if len(result_payments) == 0:
            result_payments = str(payment)
        else:
            result_payments = result_payments + " - " + str(payment)
    return result_payments


print(show_payments([100000, 200000, 400000, "100000"]))

# este codigo a continuacion no es recomendado se hace con el fin de
# de que se lance el erro de bandit hook

# import hashlib

# password = "secreto123"
# salt = "abcd1234"

# hash = hashlib.md5(password + salt).hexdigest()
# print("Hash: ", hash)
