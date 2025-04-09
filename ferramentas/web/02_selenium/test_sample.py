import random
import pathlib
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def test_sample_page_aula_2():
    #Abrindo a página
    file_path = pathlib.Path(__file__).parent.resolve()
    driver = webdriver.Chrome()
    driver.get(f"file:////{file_path}/my.html")

    #Clicando no botão de gerar o nome e confirmando que realmente foi gerado
    driver.find_element(by=By.NAME, value="generate").click()
    text_el = driver.find_element(by=By.ID, value="my-value")
    wait = WebDriverWait (driver, timeout=10)
    wait.until(lambda d: text_el.is_displayed())
    text = text_el.text
    assert text is not ""

    #Limpando o campo de texto e preenchendo com o novo valor
    field = driver.find_element(by=By.ID, value="input")
    field.clear()
    field.send_keys(text)

    #Clicando botão e no pop-up
    driver.find_element(by=By.NAME, value="button").click()
    alert = driver.switch_to.alert
    alert.accept()

    message = driver.find_element(by=By.ID, value="result")
    value = message.text
    assert value == f"It workls! {text}!"

    from time import sleep
    sleep(2)

    #title = driver.title
    #assert title == "Sample page"
    #text_box = driver.find_element(by=By.ID, value="input")
    #text = ["cheese", "selenium", "test", "bla", "foo"]
    #text_aula = text[random.randrange(len(text))]
    #text_box.send_keys(text_aula)
    #submit_button.click()

    driver.quit()
