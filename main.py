from typing import List

def show_payments(payments: List[int]) -> str:
    result_payments: str = ""
    for payment in payments:
        if len(result_payments)==0:
            result_payments = str(payment)
        else:
            result_payments = result_payments+ " - " +str(payment)
    return result_payments


print(show_payments([100000,200000,400000, "100000"]))