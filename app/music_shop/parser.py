import json

from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def collect(url: str):
    options = webdriver.ChromeOptions()
    options.add_argument(f"user-agent={UserAgent.random}")
    options.add_argument("--disable-blink-features=AutomationControlled")
    # options.add_argument("--headless")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    driver.get(url=f"{url}")
    driver.implicitly_wait(20)

    try:
        links = [item.get_attribute("src").strip() for item in driver.find_elements(By.CLASS_NAME, value="fx-image")]
        models = [item.text.strip() for item in driver.find_elements(By.CLASS_NAME, value="title__manufacturer")]
        names_un_model = [item.text.strip() for item in driver.find_elements(By.CLASS_NAME, value="title__name")]
        full_names = [models[i] + " " + names_un_model[i] for i in range(len(models))]

        links = links[:len(models)]
        costs = [item.text.strip().replace("£", "") for item in
                 driver.find_elements(By.CLASS_NAME, value="product__price-primary")]
        info = []
        lnks = [item.get_attribute("href") for item in driver.find_elements(By.CLASS_NAME, value="product__content")]
        for link in lnks:
            driver.get(link)
            info.append({item.text.split(":")[0]: item.text.split(":")[-1].strip() for item in
                         driver.find_elements(By.CLASS_NAME, value="list-item__text")})

        context = {
            "data": {full_names[i]: {"picture": links[i], "cost": costs[i], "info": info[i]} for i in
                     range(len(full_names))}
        }
        with open("data/data.json", "w") as file:
            json.dump(context, file)

    except Exception as ex:
        print(ex)
        driver.close()
        driver.quit()


def main():
    collect("https://www.thomann.de/gb/headless_guitars.html?ls=100&gk=GIEGHL&cme=false")


if __name__ == '__main__':
    main()
