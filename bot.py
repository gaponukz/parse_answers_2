from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from time import sleep
from utils import parse_answers
import json, sys

class ParseAnswers(object):
    def __init__(self) -> None:
        options = Options()
        options.add_argument("--headless")
        self.driver = webdriver.Chrome(options = options)

    def login(self, username: str, password: str) -> None:
        self.driver.get("https://perevirkaznan.com/")
        self.driver.find_element_by_xpath('/html/body/nav/div/div/a').click()
        self.driver.find_element_by_xpath('//*[@id="q"]').send_keys(username)
        self.driver.find_element_by_xpath('//*[@id="qw"]').send_keys(password)
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="login"]/form/div[3]/label/span').click()
        self.driver.find_element_by_xpath('//*[@id="login"]/form/button').click()

    def parse(self, index = '1') -> dict:
        path_to_element = '6'
        path_to_element = '10' if index == '8' else path_to_element
        path_to_element = '8' if index == '11' else path_to_element
        sleep(1)
        self.driver.find_element_by_xpath('/html/body/nav/div/div/div/div[4]/a').click()
        self.driver.find_element_by_xpath(f'/html/body/section[2]/div/div/div[{index}]/div/div[2]/a').click()
        sleep(1)
        self.driver.find_element_by_xpath(f'/html/body/section[2]/div/div[{path_to_element}]/a[2]').click()
        num = self.driver.current_url.split('/quiz/')[-1]

        return parse_answers(self.driver.page_source), num

    def close(self) -> None:
        self.driver.close()

if __name__ == "__main__":
    username = 'qwert'
    password = '147258'
    black_list = [6, 7, 8, 15, 16]

    if len(sys.argv) > 1:
        i = sys.argv[1]
        
        try:
            parser = ParseAnswers()
            parser.login(username, password)
            data, num = parser.parse(index = str(i))
                
            with open (f'{num}.json', 'w') as f:
                f.write(json.dumps(data, \
                    indent = 4, sort_keys = True))

            parser.close()
        except Exception as error:
            print(f'{error} in {i} item, please contact the author.')
    else:
        for i in range(1, 14):
            try:
                parser = ParseAnswers()
                parser.login(username, password)
                data, num = parser.parse(index = str(i))

                with open (f'{num}.json', 'w') as f:
                    f.write(json.dumps(data, \
                        indent = 4, sort_keys = True))

                parser.close()
            except:
                pass
            
            print(f'Parsed {i} successfully') /html/body/section[2]/div/div[10]/a[2]
