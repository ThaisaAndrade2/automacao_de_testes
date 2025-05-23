import random
import pathlib
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_sample_page():
    file_path = pathlib.Path(__file__).parent.resolve()
    driver = webdriver.Chrome()
    driver.get(f"file:////{file_path}/sample.html")
    title = driver.title
    assert title == "Sample page"
    driver.implicitly_wait(0.5)
    text_box = driver.find_element(by=By.ID, value="input")
    submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")
    text = ["cheese", "selenium", "test", "bla", "foo"]
    text_aula = text[random.randrange(len(text))]
    text_box.send_keys(text_aula)
    submit_button.click()
    message = driver.find_element(by=By.ID, value="result")
    value = message.text
    assert value == f"It works! {text_aula}!"
    driver.quit()
