from selenium import webdriver
import time
import keyboard

# created by Arka Saha
# Note: If any error like, Element not found or not interactable, then try changing the xpath or id, as used in the code line


class AutoInsta:
    def post_comment(self, chrome_driver, username, password, target_account, comment):
        driver = webdriver.Chrome(chrome_driver)
        driver.maximize_window()
        time.sleep(2)
        driver.get('https://instagram.com/')
        time.sleep(3)

        # entering login details
        driver.find_element_by_name('username').send_keys(username)
        driver.find_element_by_name('password').send_keys(password)
        time.sleep(3)

        # clicking the login button
        driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button').click()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
        time.sleep(7)
        try:
            driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]').click()
        except:
            driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')

        # searching for required account
        driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[1]/div').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input').send_keys(
            target_account) # sends the target account name in the search box
        time.sleep(3)
        driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div').click() # click on the account
        time.sleep(3)

        # searching posts
        for i in driver.find_elements_by_class_name('_9AhH0'):
            i.click()
            time.sleep(3)
            try:
                driver.find_element_by_xpath(
                '/html/body/div[6]/div[2]/div/article/div/div[2]/div/div[2]/section[3]/div/form/textarea').click()
            except:
                driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/textarea').click()
            time.sleep(3)
            keyboard.write(str(comment))
            time.sleep(3)
            driver.find_element_by_xpath(
                '/html/body/div[6]/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/button[2]').click()
            time.sleep(5)
            driver.find_element_by_xpath('/html/body/div[6]/div[3]/button/div').click()
            time.sleep(3)


if __name__ == "__main__":
    insta = AutoInsta()
    CHROME_DRIVER = r"path\to\chromedriver.exe"
    USERNAME = "a_cool_username"  # enter your instagram account's username
    PSD = "secret.psd"  # enter your instagram account's password
    TARGET = "a_target_acc"   # enter the name of the target account
    COMMENT = "An Awesome Comment!"  # enter the desired comment
    insta.post_comment(CHROME_DRIVER, USERNAME, PSD, TARGET, COMMENT)
