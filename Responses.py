from Selenium import get_balance


def welcome_message(username):
    answer = f'Hola {username} 👋 Todo tranqui?\nIngresá los 16 dígitos del frente de tu Tarjeta Regalo Visa y te ' \
             f'cuento cuánto saldo te queda 😊 '

    return answer


def main_answers(card_num):
    clean_card_num = card_num.replace(' ', '')

    if clean_card_num.isnumeric() and len(clean_card_num) == 16:
        return get_balance(clean_card_num)

    if clean_card_num.isnumeric() and len(clean_card_num) < 16:
        return f'Corta la bocha!\n\nTe faltaron {16 - len(clean_card_num)} números... 😅\n\nAgarrá los lentes 🤓 y ' \
               f'probemos de nuevo con los 16 números del frente de tu tarjeta regalo '

    if clean_card_num.isnumeric() and len(clean_card_num) > 16:
        return f'Epa! Te sobraron {len(clean_card_num) - 16} números...\n\nAgarrá los lentes 🤓 y probemos de nuevo 😅'

    else:
        return 'Hmmm... 😖\n\nMe parece que no ingresaste los 16 números de la tarjeta de regalo, probá de nuevo porfa 😅'
