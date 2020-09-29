from selenium import webdriver

# app_dir =  "C:\\Users\\hp\Desktop\\Test\\chp1\\geckodriver.exe"
# create a new Firefox session
driver = webdriver.Chrome(executable_path='C:\Python38\chromedriver.exe')
driver.implicitly_wait(30)
driver.maximize_window()


# navigate to the application home page
driver.get("http://demo-store.seleniumacademy.com/")


# get the search textbox
search_field = driver.find_element_by_name("q")
search_field.clear()

# enter search keyword and submit
search_field.send_keys("shirts")
search_field.submit()

# get all the anchor elements which have product names displayed
# currently on result page using find_elements_by_xpath method
products = driver.find_elements_by_xpath("//h2[@class='product-name']/a")

# get the number of anchor elements found
print ('Found ' + str(len(products)) + ' products:')

# iterate through each anchor element and print the text that is
# name of the product
for product in products: 
    print (product.text)
    
# close the browser window
driver.quit()