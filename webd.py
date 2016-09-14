#! python3
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

caps=DesiredCapabilities.FIREFOX

caps['marionette']=True

caps["binary"]="/usr/bin/firefox"

driver=webdriver.Firefox(capabilities=caps)

from pyvirtualdisplay import Display
display = Display(visible=0, size=(1024, 768))
display.start()
browser=webdriver.Firefox()
browser.get('http://inventwithpython.com')
try:
	elem=browser.find_element_by_class_name('bookcover')
	print('Found <%s> element with that class name' % (elem.tag_name))
except:
	print('Was not found')
browser.quit()
display.stop()
