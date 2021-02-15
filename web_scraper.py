import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

class Bot(object):
    def __init__(self):
        self.PATH = r"C:\Users\lloyd\Desktop\webdriver\chromedriver.exe"
        self.url = "https://www.youtube.com/"
        self.driver = webdriver.Chrome(executable_path=self.PATH)
        self.action_chains = ActionChains(self.driver)
        self.action_chains = ActionChains(self.driver)
        self.driver.get(self.url)
        self.page = self.driver.page_source
        self.user_data = {
            'email': None,
            'password': None,
        }
        self.url_info = []
    
    def search_channel(self, channel):
        search = self.driver.find_element_by_xpath("//input[@id='search']")
        search.clear()
        search.send_keys(channel)
        search.send_keys(Keys.ENTER)
        time.sleep(4)
        
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "//a[@id='thumbnail']"))
        )
        channel = self.driver.find_element_by_css_selector("//a[@id='thumbnail']").click()
        time.sleep(4)

        return
    
    # Incomplete
    def sign_in(self):
        pass

    def close_down(self):
        self.driver.close()
        return
    
    # (Incomplete) Unable to perform any more actions due to not being able to log in to site as bot    
    def leave_comment(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "style-scope yt-img-shadow"))
            )
            popup_exit = self.driver.find_element_by_class_name("style-scope ytd-button-renderer style-text size-default")
            popup_exit.click()
        finally:
            is_playing = True
            button = self.driver.find_element(By.XPATH, "//button[@class='ytp-play-button ytp-button']")
            if is_playing:
                time.sleep(5)
                button.click()
                is_playing = False
            else:
                pass

            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)

            comment_sect = self.driver.find_element_by_css_selector("style-scope ytd-comment-simplebox-renderer")
            comment_sect.click()
            comment_sect = self.driver.find_element_by_css_selector(("ytd-comments ytd-comment-simplebox-renderer" 
                                            "iron-autogrow-textarea #textarea"))
            comment_sect.click()
            comment_sect.send_keys("This is a Comment")

            return

bot = Bot()
print(bot.search_channel("Example channel name")
print(bot.leave_comment())
