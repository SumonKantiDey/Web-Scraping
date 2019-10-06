from selenium import webdriver
for i in range(2):
    print(i)
    hyperlink = "https://domainreg.btcl.com.bd"
    driver = webdriver.Chrome(
        executable_path="C:/Users/sumon/Desktop/Untitled Folder/driver/chromedriver.exe")
    driver.get(hyperlink)

    navigationStart = driver.execute_script(
        "return window.performance.timing.navigationStart")
    responseStart = driver.execute_script(
        "return window.performance.timing.responseStart")
    domComplete = driver.execute_script(
        "return window.performance.timing.domComplete")

    backendPerformance_calc = responseStart - navigationStart
    frontendPerformance_calc = domComplete - responseStart

    print("Back End: %s" % backendPerformance_calc)
    print("Front End: %s" % frontendPerformance_calc)

    driver.quit()
