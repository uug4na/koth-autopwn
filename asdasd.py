from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import pyfiglet

def login():
    actions = ActionChains(driver)
    click = "/html/body/div[3]/div[2]/div[5]/div[2]/div"
    driver.maximize_window()
    driver.get("https://tryhackme.com/dashboard")
    driver.add_cookie({"_csrf": "mHhf4CgnFqo7Dto3DDjBHVve"})
    driver.add_cookie({"_ga": "GA1.2.985772354.1656602158", "_gat_gtag_UA_129037102_1" : "1",})
    driver.add_cookie({"_gid": "GA1.2.1717970409.1659005622"})
    driver.add_cookie({"_hjAbsoluteSessionInProgress" : "1"})
    driver.add_cookie({"_hjCachedUserAttributes" : "eyJhdHRyaWJ1dGVzIjp7ImRhdGVTaWduZWRVcCI6IlNhdCBKdW4gMTMgMjAyMCAxNToxMDo0OCBHTVQrMDEwMCAoQnJpdGlzaCBTdW1tZXIgVGltZSkiLCJkaXNwbGF5TmFtZSI6InMxbGVudCIsImV4cGVyaWVuY2UiOiJpbnRlcm1lZGlhdGUiLCJzdWJzY3JpYmVkIjoiMCJ9LCJ1c2VySWQiOiI1ZWU0ZGU2OGRkOWU2NDFlNjFkN2RlMGIifQ=="})
    driver.add_cookie({"_hjIncludedInPageviewSample" : "1"})
    driver.add_cookie({"_hjIncludedInSessionSample" : "0"})
    driver.add_cookie({"_hjSession_1950941" : "eyJpZCI6ImY3YTI0OWEzLWUzNTEtNDlmNS04NTQ2LTUyYzZmNDg3MmZkNiIsImNyZWF0ZWQiOjE2NTkwMTQ5ODYwNTcsImluU2FtcGxlIjpmYWxzZX0="})
    driver.add_cookie({"_hjSessionUser_1950941" : "eyJpZCI6IjU5MjA0OTc5LWUxNWUtNWE0ZS05OWJkLThhMWY5YmI5MjIzOSIsImNyZWF0ZWQiOjE2NTY2MDIxOTY4NTYsImV4aXN0aW5nIjp0cnVlfQ=="})
    driver.add_cookie({"AWSALB" : "PCWqMEluE1Xnv1/MKiBmSSMBchYNM5PuwxyjSzg1oLvae/JfazQMImENVs+RPzrNV7dh4gQS7NVpjgK5PuLR8GJGfOfc3zs5JLfc/Q8QP0Hp1/is2QWvtBFgamiU"})
    driver.add_cookie({"AWSALBCORS" : "PCWqMEluE1Xnv1/MKiBmSSMBchYNM5PuwxyjSzg1oLvae/JfazQMImENVs+RPzrNV7dh4gQS7NVpjgK5PuLR8GJGfOfc3zs5JLfc/Q8QP0Hp1/is2QWvtBFgamiU"})
    driver.add_cookie({"connect.sid" : "s%3A4HMN67c_Lgg6haRONG9nsI4EP4ton0Q2.jyx57Jjk1jzrEFM8RTRyrkMdf9sLPmlqp67lxAS2cgk"})
    driver.add_cookie({"cookieconsent_status" : "dismiss"})
    click.click()
    print('done')

def main():
    print('ok')
    login()


if __name__ == '__main__':
    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1600,900")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    main()
