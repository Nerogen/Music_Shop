import json
import time

from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def collect(category: str, url: str):
    options = webdriver.ChromeOptions()
    options.add_argument(f"user-agent={UserAgent.random}")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--headless")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    driver.get(url=f"{url}")
    driver.implicitly_wait(20)
    links = []
    models = []
    full_names = []
    costs = []
    info = []
    try:
        links = [item.get_attribute("src").strip() for item in driver.find_elements(By.CLASS_NAME, value="fx-image")]
        models = [item.text.strip() for item in driver.find_elements(By.CLASS_NAME, value="title__manufacturer")]
        names_un_model = [item.text.strip() for item in driver.find_elements(By.CLASS_NAME, value="title__name")]
        full_names = [models[i] + " " + names_un_model[i] for i in range(len(models))]

        links = links[:len(models)]
        costs = [item.text.strip().replace("£", "") for item in
                 driver.find_elements(By.CLASS_NAME, value="product__price-primary")]

        lnks = [item.get_attribute("href") for item in driver.find_elements(By.CLASS_NAME, value="product__content")]
        for link in lnks:
            driver.get(link)
            info.append({item.text.strip(): item.text.strip() for item in
                         driver.find_elements(By.CLASS_NAME, value="list-item__text")})

        time.sleep(2)

        context = {
            category: {full_names[i]: {"picture": links[i], "cost": costs[i], "info": info[i]} for i in
                     range(len(full_names))}
        }

        with open(f"data/{category}.json", "w") as file:
            json.dump(context, file)

    except Exception as ex:
        print(ex)
        context = {
            category: {full_names[i]: {"picture": links[i], "cost": costs[i], "info": info[i]} for i in
                       range(len(info))}
        }

        with open(f"data/{category}.json", "w") as file:
            json.dump(context, file)

        driver.close()
        driver.quit()


def main():
    links = {
        "Guitars": "https://www.thomann.de/gb/headless_guitars.html?ls=10&gk=GIEGHL&cme=false",
        "Microfones": "https://www.thomann.de/gb/dynamic_microphones.html?ls=10&gk=MIGEDY&category%5B%5D=MIGEDY&cme=true",
        "Drums": "https://www.thomann.de/gb/complete_drumkits.html?ls=10&gk=DRADKD&category%5B%5D=DRADKD&cme=true",
        "Software": "https://www.thomann.de/gb/sequencing_software_and_virtual_studios.html?ls=10&gk=SWSQ&cme=false",
        "DJ Equipment": "https://www.thomann.de/gb/usb_audio_interfaces.html?ls=10&gk=STAIUS&cme=false",
        "Keys": "https://www.thomann.de/gb/home_keyboards.html?ls=10&gk=TAKYBH&cme=false",
        "Accessories": "https://www.thomann.de/gb/studio_headphones.html?ls=10&gk=ZUKOSK&cme=false",
        "Connectors": "https://www.thomann.de/gb/instrument_cables.html?ls=10&gk=KAIN&cme=false"
    }
    for key, value in links.items():
        collect(key, value)


if __name__ == '__main__':
    main()
