import random


def is_ticket_function_params_valid(min: int, max: int, quantity: int) -> bool:
    if 1 <= min < max <= 1000 and min <= quantity <= max:
        return True
    else:
        return False


def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    if is_ticket_function_params_valid(min, max, quantity) is False:
        return []
    return sorted(random.sample(range(min, max + 1), quantity))


lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)