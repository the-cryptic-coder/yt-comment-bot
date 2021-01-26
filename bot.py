import os, time, random, spintax, requests, config
import numpy as np
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from random import randint, randrange
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

PROXY = "3.88.169.225:80"

def stop(n):
	time.sleep(randint(2, n))

#login bot===================================================================================================
def youtube_login(email,password):

	op = webdriver.ChromeOptions()
	# op.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
	# op.add_argument('--headless')
	op.add_argument('--disable-dev-shm-usage')
	# op.add_argument('--no-sandbox')
	op.add_argument('--disable-gpu')
	# op.add_argument("--window-size=1920,1080")
	op.add_argument("disable-infobars")
	op.add_argument("--disable-extensions")
	# op.add_argument('--proxy-server=%s' % PROXY)
	# op.add_argument("--proxy-bypass-list=*")
	driver = webdriver.Chrome(options=op, executable_path= 'chromedriver.exe')
	driver.execute_script("document.body.style.zoom='80%'")
	driver.get('https://accounts.google.com/ServiceLogin?service=youtube&uilel=3&passive=true&continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Den%26next%3Dhttps%253A%252F%252Fwww.youtube.com%252F&hl=en&ec=65620')

	print("=============================================================================================================")
	print("Google Login")

	#finding email field and putting our email on it
	email_field = driver.find_element_by_xpath('//*[@id="identifierId"]')
	email_field.send_keys(email)
	driver.find_element_by_id("identifierNext").click()
	stop(5)
	print("email - done")

	#finding pass field and putting our pass on it
	find_pass_field = (By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')
	WebDriverWait(driver, 50).until(EC.presence_of_element_located(find_pass_field))
	pass_field = driver.find_element(*find_pass_field)
	WebDriverWait(driver, 50).until(EC.element_to_be_clickable(find_pass_field))
	pass_field.send_keys(password)
	driver.find_element_by_id("passwordNext").click()
	stop(5)
	print("password - done")
	WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-masthead button#avatar-btn")))
	print("Successfully login")
	print("============================================================================================================")

	return driver
#==============================================================================================================



#comment bot===================================================================================================
def comment_page(driver,urls,comment):

	if len( urls ) == 0:
		print("============================================================================================================")
		print ('Finished keyword jumping to next one...')
		return []
	
	#gettin a video link from the list
	url = urls.pop()
	
	driver.get(url)
	print("Video url:" + url)
	driver.implicitly_wait(1)

	#checking if video is unavailable
	if not check_exists_by_xpath(driver,'//*[@id="movie_player"]'):
		print("skiped")
		return comment_page(driver, urls, random_comment())


	
	time.sleep(2)
	# You can add like function by uncommenting 4 lines below
	# like_button = EC.presence_of_element_located(By.XPATH, '/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[4]/div[1]/div/div[5]/div[2]/ytd-video-primary-info-renderer/div/div/div[3]/div/ytd-menu-renderer/div/ytd-toggle-button-renderer[1]/a/yt-icon-button/button/yt-icon')
	# WebDriverWait(driver, 50).until(EC.element_to_be_clickable(like_button)).click()
	# print('Liked')
	# time.sleep(1)
	driver.execute_script("window.scrollTo(0, window.scrollY + 500)")
	time.sleep(1)

	#checking if comments are disabled
	if not check_exists_by_xpath(driver,'//*[@id="simple-box"]/ytd-comment-simplebox-renderer'):
		print("skiped")
		return comment_page(driver, urls, random_comment())

	#checking if video is a livestream
	if check_exists_by_xpath(driver,'//*[@id="contents"]/ytd-message-renderer'):
		print("skiped")
		return comment_page(driver, urls, random_comment())

	#finding comment box and submiting our comment on it
	comment_box = EC.presence_of_element_located((By.CSS_SELECTOR, '#placeholder-area'))
	WebDriverWait(driver, 4).until(comment_box)
	comment_box1 = driver.find_element_by_css_selector('#placeholder-area')
	ActionChains(driver).move_to_element(comment_box1).click(comment_box1).perform()
	add_comment_onit = driver.find_element_by_css_selector('#contenteditable-root')
	add_comment_onit.send_keys(comment) 
	time.sleep(2) 
	driver.find_element_by_css_selector('#submit-button').click()
	print("done")

	stop(5)

	return comment_page(driver, urls, random_comment())
#==============================================================================================================


#comment section
def random_comment():
# You can edit these lines if you want to add more comments===================================
	comments = [
		'Check out my channel!',
		'https://www.youtube.com/watch?v=0tPu7L_dxR4',
		'https://www.youtube.com/watch?v=S1n9NlCDUbo&t=3s',
		'https://www.youtube.com/watch?v=AAtUS0lLjvQ&t=4s',
		'https://www.youtube.com/watch?v=AAtUS0lLjvQ&t=4s',	
		'https://www.youtube.com/watch?v=PLQH3ibZZrY&t=11s',
		'https://www.youtube.com/watch?v=PLQH3ibZZrY&t=11s',
		'https://www.youtube.com/watch?v=PzbtaUyPpzQ&t=2s',
		'https://www.youtube.com/watch?v=b5Uv0CNp1o0&t=2s',
		'https://www.youtube.com/watch?v=AepFFzOIiKg&t=1s',
		'https://www.youtube.com/watch?v=6eTLwJVGiR8&t=4s',
		'https://www.youtube.com/watch?v=e83xe72_E3E',
		'https://www.youtube.com/watch?v=fbOQX3QPz-M&t=26s',
		'https://www.youtube.com/watch?v=ZQ5GYKqkEPg&t=16s',
		'https://www.youtube.com/watch?v=5-hf1EsDMt0&t=4s',
		'https://www.youtube.com/channel/UCuAjoGTTf7iaMixpiEdKFZQ',
		'I also post a lot of videos like this',
		'pls check out my channel',
		'I have a tutorial of this on my channel',
		'Learn how to make this bot on my channel',
		'subscribe to my channel',
		'subscribe to my channel for good luck',
		'pls subscribe to my channel'


	]
	a=0
	while a<100000:
		b=str(a)
		comment='Sick Trickshot on mobile (MUST SEE!!)--> https://www.youtube.com/watch?v=hkNSJ2jMtNk&t=2s '+ b
		#comment1='This video has great info on this topic--> https://www.youtube.com/watch?v=S1n9NlCDUbo&t=3s '+ b
		#comment2='https://www.youtube.com/channel/UCuAjoGTTf7iaMixpiEdKFZQ?sub_confirmation=1 '+ b
		#comment3='https://www.youtube.com/channel/UCuAjoGTTf7iaMixpiEdKFZQ?sub_confirmation=1 pls subscribe '+ b
		comments.append(comment)
		#comments.append(comment1)
		#comments.append(comment2)
		#comments.append(comment3)
		#comment='This video has great info on this topic--> https://www.youtube.com/watch?v=BO6sqPdRDc8&t=2s '+ b
		#comment1='This video has great info on this topic--> https://www.youtube.com/watch?v=e83xe72_E3E&t=9s '+ b
		#comment2='https://www.youtube.com/channel/UCuAjoGTTf7iaMixpiEdKFZQ?sub_confirmation=1 '+ b
		#comment3='https://www.youtube.com/channel/UCuAjoGTTf7iaMixpiEdKFZQ?sub_confirmation=1 pls subscribe '+ b
		#comments.append(comment)
		#comments.append(comment1)
		#comments.append(comment2)
		#comments.append(comment3)
		#comment='This video has great info on this topic--> https://www.youtube.com/watch?v=e83xe72_E3E '+ b
		#comment1='This video has great info on this topic--> https://www.youtube.com/watch?v=S1n9NlCDUbo&t=3s '+ b
		#comment2='This video has great info on this topic--> https://www.youtube.com/watch?v=ZQ5GYKqkEPg&t=2s '+ b
		#comment3='This video has great info on this topic--> https://www.youtube.com/watch?v=0tPu7L_dxR4 '+ b
		#comments.append(comment)
		#comments.append(comment1)
		#comments.append(comment2)
		#comments.append(comment3)
		#comment='This video has great info on this topic--> https://www.youtube.com/watch?v=BO6sqPdRDc8&t=6s '+ b
		#comment1='This video has great info on this topic--> https://www.youtube.com/watch?v=6eTLwJVGiR8&t=53s '+ b
		#comment2='This video has great info on this topic--> https://www.youtube.com/watch?v=e83xe72_E3E '+ b
		#comment3='This video has great info on this topic--> https://www.youtube.com/watch?v=5-hf1EsDMt0&t=5s '+ b
		#comments.append(comment)
		#comments.append(comment1)
		#comments.append(comment2)
		#comments.append(comment3)
		a+=1
# =============================================================================================
	r = np.random.randint(0, len(comments))

	return comments[r]
 
def check_exists_by_xpath(driver,xpath):
	try:
		driver.find_element_by_xpath(xpath)
	except NoSuchElementException:
		return False

	return True


#running bot------------------------------------------------------------------------------------
if __name__ == '__main__':
	email = config.email
	password = config.password

	driver = youtube_login(email, password)
	driver.maximize_window()
	while True:
		key = driver.find_element_by_name('search_query')

		key.send_keys(Keys.CONTROL,"a")
		key.send_keys(Keys.DELETE)

		#get keyword list and extract each key
		with open('gaming_keywords.txt', 'r') as f:
			keywords = [line.strip() for line in f]
			random_keyword = random.choice(keywords)
			keys = spintax.spin(random_keyword)

			#send keyword in the search box
			for char in keys:
				key.send_keys(char)
		
		time.sleep(1)


		#click search icon
		driver.find_element_by_css_selector('#search-icon-legacy > yt-icon').click()
		time.sleep(3)
		#click filter button to filter the videos for the recently uploaded, you can remove or edit this option
		driver.find_element_by_css_selector('#container > ytd-toggle-button-renderer > a').click()
		time.sleep(3)

		#filtering for this week
		driver.find_element_by_xpath("(//yt-formatted-string[@class='style-scope ytd-search-filter-renderer'])[3]").click()
		time.sleep(3)
		
		#grabbing videos titles
		for i in range(5):
			ActionChains(driver).send_keys(Keys.END).perform()
			time.sleep(3)
		titles = driver.find_elements_by_xpath('//*[@id="video-title"]')

		urls = []

		#getting url from href attribute in title
		for i in titles:
			if i.get_attribute('href') != None:
				urls.append(i.get_attribute('href'))
			else:
				continue
	
		#checking if we have links or not
		if urls == []:
			print("There is no videos for this keyword at the moment")
		else:
			comment_page(driver,urls,random_comment())