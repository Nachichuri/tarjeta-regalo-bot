import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

url = r'https://visahome.prismamediosdepago.com/socios/service/giftCard'


def get_balance(card_num):
    # We create the driver
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    driver = webdriver.Chrome('/bot/chromedriver', options=options)

    # Go to the webpage
    driver.get(url)

    # Input card number, and press enter key
    input_cardNumber = driver.find_element(By.ID, 'step1:loginForm:cardNumber')
    submit_button = driver.find_element(By.ID, 'step1:loginForm:button')

    input_cardNumber.send_keys(card_num)
    submit_button.send_keys(Keys.RETURN)
    submit_button.send_keys(Keys.RETURN)

    time.sleep(2)

    # First we check if the webpage detects it as valid
    if 'La tarjeta ingresada no es válida' in driver.find_element(By.TAG_NAME, 'BODY').text:
        return 'Hmm... 🤔 Según Visa el número ingresado no es válido.\n\nChequeá haber ingresado el número correcto ' \
               'y que la tarjeta no se encuentre vencida. '

    # If it does, we get the balance
    current_balance = driver.find_element(By.ID,
                                          'step2:mainContent:form:inner:aasContent:currentTrxSubTotals:j_idt44:totalCellTotalInput')

    balance = current_balance.text

    driver.quit()

    return f'El saldo actual de tu Tarjeta Regalo Visa es: ${balance}'
