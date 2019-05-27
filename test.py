from selenium.webdriver import Chrome
path="C:\\Users\\Asus\\Downloads\\chromedriver_win32\\chromedriver.exe"
driver = Chrome(executable_path=path)
driver.get(" http://127.0.0.1:5000/ ")

#upload file
driver.find_element_by_id("uploadfile").send_keys("D:\\sem5\\software engineering project\\project\\T12\\project\\testCases\\test1.phy")
#submit file to view
driver.find_element_by_id("submit").click()
#submit file to create tree
driver.find_element_by_id("go").click()
#select first format
driver.find_element_by_xpath("//*[@id='selector']/option[1]")
#create tree
driver.find_element_by_id("next").click()
