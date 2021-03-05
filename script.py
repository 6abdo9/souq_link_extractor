try:
  from selenium import webdriver
  from time import sleep
except:
  print('Install Selinium Module And Try Again [ pip3 install selenium ]')
  sleep(10)
  
kwrd = input('Keyword? : ')
driver = webdriver.Chrome()
driver.get('https://egypt.souq.com/eg-ar/'+ kwrd +'/s/')
elems  = driver.find_elements_by_class_name('itemLink')
with open(kwrd+'.txt', 'a+') as res:
    for elem in elems:
        x = elem.get_attribute("href")
        res.write(x+'\n')
