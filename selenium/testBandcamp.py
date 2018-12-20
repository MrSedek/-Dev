from webbrowser import Chrome
import time
from selenium.webdriver import Firefox
from selenium.webdriver import Chrome
from selenium.webdriver.firefox.options import Options as OptionsFirefox
from selenium.webdriver.chrome.options import Options as OptionsChrome
optsFirefox = OptionsFirefox()
optsChrome = OptionsChrome()


##Chrome
browserChrome = Chrome(options=optsChrome)
browserChrome.get('https://duckduckgo.com')
search_form = browserChrome.find_element_by_id('search_form_input_homepage')
search_form.send_keys('real python')
search_form.submit()
resultsChromeFind = browserChrome.find_elements_by_class_name('result')
print(resultsChromeFind[0])
for i in range(len(resultsChromeFind)):
    print(resultsChromeFind[i].text)
    print()
##search_form = browserChrome.find_element_by_class_name('result')
##search_form.submit()
time.sleep(5)
browserChrome.close()

print()

##Firefox
browserFirefox = Firefox(options=optsFirefox)
browserFirefox.get('https://duckduckgo.com')
search_form = browserFirefox.find_element_by_id('search_form_input_homepage')
search_form.send_keys('real python')
search_form.submit()
resultsFirefoxFind = browserFirefox.find_elements_by_class_name('result')
for i in range(len(resultsFirefoxFind)):
    print(resultsFirefoxFind[i].text)

browserFirefox.close()
