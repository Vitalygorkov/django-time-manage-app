# id: "0x2f9EDe75144E84e66511A4FFd137152c80eabb17"
{
  user(id: "0x2f9EDe75144E84e66511A4FFd137152c80eabb17"){
		id:
		liquidityPositions: {
		id:
		user:
		pair:
		liquidityTokenBalance:
}
		usdSwapped:
 }
}

{
  user(id: "0x2f9EDe75144E84e66511A4FFd137152c80eabb17"){
    id
    liquidityPositions
    usdSwapped
  }
}

import sqlite3
from selenium import webdriver
import datetime
import time
import random

options = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images": 2}
options.add_experimental_option("prefs", prefs)
print(datetime.date.today())

driver = webdriver.Chrome('/home/v/PycharmProjects/django_barakov/mysite/youtscan/moduls/chromedriver', options=options)

# conn = sqlite3.connect('baza.db')
# cur = conn.cursor()
# cur.execute("SELECT * FROM channels;")
# all_results = cur.fetchall()
# cur.execute("""CREATE TABLE IF NOT EXISTS vidos(
#    vidid INT,
#    name TEXT,
#    descr TEXT,
#    prosm INT,
#    pub TEXT,
#    link TEXT PRIMARY KEY);
# """)
# conn.commit()

link = 'https://info.uniswap.org/account/0x2f9EDe75144E84e66511A4FFd137152c80eabb17'

# '<div class="sc-bdVaJa KpMoH css-1m1dl4y">17,266 </div>'
# '<div class="sc-bdVaJa KpMoH css-1m1dl4y">0,482 </div>'

driver.get(link)
time.sleep(1)
len_scroll = 3000
for i in range(1, 10):
    driver.execute_script("window.scrollBy(0,{})".format(len_scroll))
    len_scroll += 500
    time.sleep(random(3))
    print('прокрутка')
for i in driver.find_element_by_class_name("sc-bdVaJa KpMoH css-1m1dl4y"):
    print(i)
    print(i.text)

