import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import pandas as pd
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class autokart:
    def __init__(self):
        self.opts = webdriver.ChromeOptions()
        self.opts.add_experimental_option("detach", True)
        self.opts.add_argument("--user-data-dir=C:/Users/91888/AppData/Local/Google/Chrome/User Data")
        self.driver = webdriver.Chrome(options=self.opts)

    def launch_flipkart(self):
        # Opens Flipkart page
        self.driver.get("https://www.flipkart.com/")
        self.driver.maximize_window()

        # set implicit wait time
        self.driver.implicitly_wait(120)  # seconds
        time.sleep(2)  # 2 Second Wait

    def search_product(self, product, brand, rating):
        # clear search field
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@name = 'q']").send_keys(Keys.CONTROL,"a", Keys.DELETE)
        time.sleep(1)

        # Automatically enters product name
        self.driver.find_element(By.XPATH, "//input[@name = 'q']").send_keys(product)
        self.driver.find_element(By.XPATH, "//input[@name = 'q']").send_keys(Keys.ENTER)

        # click checkbox option for Brand
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//div[contains(text(),'" + brand + "')]/preceding-sibling::div").click()

        # click checkbox option for Rating
        time.sleep(2)
        self.driver.find_element(
            By.XPATH, "//div[contains(text(),'" + str(
                rating) + "') and contains(text(),'& above')]/preceding-sibling::div").click()

        # click on sorting by Price Low to High
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//div[text()='Price -- Low to High']").click()

    def add_product_to_cart(self):
        # select the first product
        time.sleep(2)#container > div > div.nt6sNV.JxFEK3._48O0EI > div > div:nth-child(2) > div:nth-child(2) > div > div > div > a > div.Otbq5D > div.yPq5Io > div > div
        self.driver.find_element(By.CSS_SELECTOR,
                                 "#container > div > div.nt6sNV.JxFEK3._48O0EI > div > div:nth-child(2) > div:nth-child(2) > div > div > div > a > div.Otbq5D > div.yPq5Io > div > div").click()

        # switch to newly open tab
        time.sleep(2)
        tabs = self.driver.window_handles

        # Add product to Cart
        time.sleep(5)
        self.driver.switch_to.window(tabs[1])
        add_to_cart = self.driver.find_element(By.CSS_SELECTOR,
                                               "#container > div > div._39kFie.N3De93.JxFEK3._48O0EI > div.DOjaWF.YJG4Cf > div.DOjaWF.gdgoEp.col-5-12.MfqIAz > div:nth-child(2) > div > ul > li:nth-child(1) > button")

        # wait for add to cart button to be clickable
        wait = WebDriverWait(self.driver, timeout=120)
        wait.until(expected_conditions.element_to_be_clickable(add_to_cart))
        add_to_cart.click()

        # place order
        time.sleep(2)
        self.driver.find_element(By.XPATH, "// span[text() = 'Place Order'] / parent::button").click()

        # close the place order tab and switch to main tab
        time.sleep(5)
        self.driver.close()
        self.driver.switch_to.window(tabs[0])

    def close_browser(self):
        # close the main tab
        self.driver.close()

    def launch_amazon(self):
        # Opens Amazon page
        self.driver.get("https://www.amazon.in/")
        self.driver.maximize_window()

        # set implicit wait time
        self.driver.implicitly_wait(120)  # seconds
        time.sleep(2)  # 1 Second Wait

    def search_product_amazon(self, product, brand, rating):
        # clear search field
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@name = 'field-keywords']").send_keys(Keys.CONTROL, "a", Keys.DELETE)
        time.sleep(1)

        # Automatically enters product name
        self.driver.find_element(By.XPATH, "//input[@name = 'field-keywords']").send_keys(product)
        self.driver.find_element(By.XPATH, "//input[@name = 'field-keywords']").send_keys(Keys.ENTER)

        # click checkbox option for Brand
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//span[contains(text(),'" + brand + "')]/preceding-sibling::div").click()

        # click checkbox option for Rating
        time.sleep(2)
        self.driver.find_element(
            By.XPATH, "//section[contains(@aria-label,'"+str(rating)+"') and contains(@aria-label,'& Up')]/i").click()
        #low to high
        time.sleep(2)
        self.driver.find_element(
            By.XPATH, '//*[@id="a-autoid-0-announce"]').click()
        self.driver.find_element(
            By.XPATH, '//*[@id="s-result-sort-select_1"]').click()


    def add_product_to_cart_amazon(self):

        # Add product to Cart
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[2]/div/div/span/div/div/div/div[1]/div/div[2]/div/span/a/div').click()

        # switch to newly open tab
        time.sleep(2)
        tabs = self.driver.window_handles

        # Add product to Cart
        time.sleep(5)
        self.driver.switch_to.window(tabs[1])
       # self.driver.find_element(By.CSS_SELECTOR,
        #                         "#quantity")

        add_to_cart = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[5]/div[3]/div[1]/div[4]/div/div[1]/div/div[1]/div/div/div[2]/div/div[2]/div/form/div/div/div[37]/div[1]/span/span/span/input')
        add_to_cart.click()
      
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="attach-sidesheet-checkout-button"]/span/input').click()
       
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="shipToThisAddressButton"]/span/input').click()

        # close the place order tab and switch to main tab
        time.sleep(5)
        self.driver.close()
        self.driver.switch_to.window(tabs[0])

def run_automation_on_csv(filename):
    try:
        df = pd.read_csv(filename)
        filter_df = df[df["required"] == "Y"]
        autokart_obj = autokart()

        for index, row in filter_df.iterrows():
            platform = row["Platform"]
            product_name = row["Product Name"]
            brand = row["Brand"]
            rating = row["Ratings"]

            if platform == "Flipkart":
                autokart_obj.launch_flipkart()
                autokart_obj.search_product(product_name, brand, rating)
                autokart_obj.add_product_to_cart()
            elif platform == "Amazon":
                autokart_obj.launch_amazon()
                autokart_obj.search_product_amazon(product_name, brand, rating)
                autokart_obj.add_product_to_cart_amazon()

        messagebox.showinfo("Success", "Automation completed successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

class AutokartUI:
    def __init__(self, master):
        self.master = master
        master.title("Autokart Automation")

        self.label = tk.Label(master, text="Select CSV File:")
        self.label.pack()

        self.select_button = tk.Button(master, text="Select", command=self.select_csv)
        self.select_button.pack()

    def select_csv(self):
        filename = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if filename:
            try:
                run_automation_on_csv(filename)
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {e}")        

def main():
    root = tk.Tk()
    app = AutokartUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()