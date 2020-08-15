from selenium import webdriver
import time
def getPosition(url):
    DRIVER_PATH = 'R:\Things\Python\chromedriver.exe'

    driver = webdriver.Chrome(DRIVER_PATH)
    driver.get(url)
    #print(driver.page_source)


    time.sleep(2)
    a = driver.find_element_by_xpath('//*[@id="page_header"]/div[1]/div[2]/div/div[2]/span[2]').text
    print(a)
    #a = a.replace('POSIÇÃO','')
    #a = (a.replace('\n', ''))
    driver.quit()
    #return a

if __name__ == "__main__":
    getPosition('https://www.zerozero.pt/player.php?id=183886')
