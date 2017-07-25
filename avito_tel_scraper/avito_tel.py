from selenium import webdriver
from time import sleep
from PIL import Image
from pytesseract import image_to_string


class Bot:

    def __init__(self):
        self.driver = webdriver.Firefox()
        self.navigate()

    def tel_recon(self):
        image = Image.open('tel.gif')
        print(image_to_string(image))

    def crop(self, location, size):
        image = Image.open('avito_screenshot.png')
        x = location['x']
        y = location['y']
        width = size['width']
        height = size['height']
        image.crop((x, y, x + width, y + height)).save('tel.gif')
        self.tel_recon()

    def take_screenshot(self):
        self.driver.save_screenshot('avito_screenshot.png')

    def navigate(self):
        self.driver.get(
            'https://www.avito.ru/moskva/telefony/htc_desire_700_dual_sim_1185379757')
        button = self.driver.find_element_by_xpath(
            '//button[@class="button item-phone-button js-item-phone-button button-origin button-origin-blue button-origin_full-width button-origin_large-extra item-phone-button_hide-phone item-phone-button_card js-item-phone-button_card"]')
        button.click()
        sleep(5)
        self.take_screenshot()

        #//* - любой элемент, в этом случае img

        image = self.driver.find_element_by_xpath(
            '//div[@class="item-phone-big-number js-item-phone-big-number"]//*')

        location = image.location
        size = image.size
        self.crop(location, size)


def main():
    b = Bot()

if __name__ == '__main__':
    main()
