"""
    In  this project  tried to find and testing elements
"""
from selenium import webdriver
import time


base_url="https://play1.automationcamp.ir"
# Find path:
options = webdriver.ChromeOptions()
options.add_argument("executable_path=C:\Chromedriver.exe") 
# lunch to browser:
driver = webdriver.Chrome(options=options) 
# Open the web page:
driver.get(f"{base_url}//forms.html")

time.sleep(5)
# Find and click item:
search_filld=driver.find_element("id","check_python").click()

time.sleep(5)
# Save text item:
checkfirst=driver.find_element("id","check_validate").text
# Check text item: 
assert checkfirst == "PYTHON"

time.sleep(5)

txt = "hello autmation world"
# Find item and send text:
driver.find_element("id","notes").send_keys(txt)
# Save text item:
time.sleep(5)
checktow=driver.find_element("id","area_notes_validate").text
# Check text item:
assert checktow == "hello autmation world"

time.sleep(5)
# Close driver:
driver.quit()
driver.close()
