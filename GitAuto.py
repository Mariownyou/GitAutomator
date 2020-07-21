from selenium import webdriver
from time import sleep
import sys

class GitHubAuto():
    username = 'ник'
    password = 'парольчик'
    driver = webdriver.Chrome()
    repName = str(sys.argv[1])
    is_private = str(sys.argv[2])
    gitignor = str(sys.argv[3])

    def createNewRep(self):
        self.login()
        self.fillRepData()
        
    def login(self):
        self.driver.get('https://github.com/new')
        self.driver.find_element_by_xpath("//input[@name=\"login\"]").send_keys(self.username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(self.password)
        self.driver.find_element_by_xpath("//input[@type='submit']").click()

    def fillRepData(self):
        # rep name
        self.driver.find_element_by_xpath("//input[@name=\"repository[name]\"]").send_keys(self.repName)
        # choose private or public
        if self.is_private == 'private':
            self.driver.find_element_by_xpath("//input[@id='repository_visibility_private']").click()
        elif self.is_private == 'p':
            self.driver.find_element_by_xpath("//input[@id='repository_visibility_public']").click()
        # add gitignor
        self.driver.find_element_by_xpath("//i[contains(text(), 'Add .gitignore:')]").click()
        self.driver.find_element_by_xpath("//input[@id='context-ignore-filter-field']").send_keys(self.gitignor)
        self.driver.find_element_by_xpath(f"//span[contains(text(), '{self.gitignor}')]").click()
        sleep(1)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Create repository')]").click()


if __name__ == '__main__':
    github = GitHubAuto()
    github.createNewRep()