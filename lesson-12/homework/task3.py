import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager # type: ignore

json_file_path = r"D:\MAAB academy new\python\homework\lesson-12\homework\laptops.json"


def scrape_laptops():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run without opening browser
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    url = "https://www.demoblaze.com/"
    driver.get(url)
    time.sleep(3)

    # Click on the Laptops section
    laptops_tab = driver.find_element(By.XPATH, "//a[text()='Laptops']")
    laptops_tab.click()
    time.sleep(3)  # Wait for page to load

    laptop_list = []

    while True:
        time.sleep(3)  # Wait for elements to load

        laptops = driver.find_elements(By.CLASS_NAME, "card-title")
        prices = driver.find_elements(By.CLASS_NAME, "card-text")

        for i in range(len(laptops)):
            name = laptops[i].text.strip()
            price = prices[i].text.strip()
            description = "No description available"  # No description available on main page

            laptop_list.append({
                "name": name,
                "price": price,
                "description": description
            })

        # Check if the "Next" button is available
        try:
            next_button = driver.find_element(By.ID, "next2")
            if "disabled" in next_button.get_attribute("class"):
                break
            next_button.click()
            time.sleep(3)
        except:
            break  # Stop if "Next" button is not found

    driver.quit()

    return laptop_list


def save_to_json(data):
    with open(json_file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)
    print(f"Data successfully saved to {json_file_path}")


if __name__ == "__main__":
    print("Scraping laptops from Demoblaze...")
    laptops = scrape_laptops()

    print("Saving data to JSON file...")
    save_to_json(laptops)

    print("Scraping and saving completed successfully!")
