#! python 3
import requests
from bs4 import BeautifulSoup
import openpyxl
import re
import time


'''
1st function call. Searches siccode.com for business name (from Excel)
and returns all <a> tags if there are multiple results. One of these urls
on the results_page will be the business in Madison Heights/MI.
'''
def get_site(biz_name):
	
	search_url = r'https://siccode.com/en/search/' + biz_name
	
	# get page object and save as text
	# rest for a mo'
	time.sleep(2) 
	results_page = requests.get(search_url)
	results_page_doc = results_page.text
	
	# create soup object
	soup = BeautifulSoup(results_page_doc, 'html.parser')
	
	# get all <a>s to use regex on
	results_links = soup.find_all('a')
	
	# return all soup <a> objects
	return results_links
	
'''
2nd function call. Loops thru all <a> links on search results page and 
uses regex to find link of business in Michigan (starts with 480..).
'''
def get_url(results_links):
	
	for link in results_links:
		
		# returns a string but I don't totally get this
		url = link.get('href')
		
		# make regex object to find url that contains MI zip code 
		url_regex = re.compile(r'.*480\d\d')
		
		try:
			
			# create match object
			mo = url_regex.search(url)
			
			# url string that points to business-specific page
			biz_url = mo.group()
			
			return biz_url
		
		# if mo == None:
		except:
		
			pass
'''
3rd function call. Gets info from page specific to business. Will eventually merge this with 2nd function call.
'''
def call_url(biz_url):
	
	biz_page_url = r'http://siccode.com' + biz_url
	
	biz_page = requests.get(biz_page_url)
	biz_page_doc = biz_page.text
	
	
	soup_2 = BeautifulSoup(biz_page_doc, 'html.parser')
	naics_a = soup_2.find_all('a', attrs={'class':{'request-url'}})
	
	for elem in naics_a:
		
		elem_doc = elem.text
		elem_regex = r'\d{6}'
		
		try:
		
			mo = re.search(elem_regex, elem_doc)
			return mo.group()
			
		except:
			
			pass

# main loop
def master():
	wb = openpyxl.load_workbook('biz.xlsx')
	sheet = wb.active
	
	#loop through rows to get biz name
	for row_iter in range(2, sheet.max_row + 1):
		
		# get business names from Excel
		biz_name = sheet.cell(row = row_iter, column = 1).value
		
		# returns soup object
		results_links = get_site(biz_name)
		
		# uses regex on all urls to find ones with zip in MI
		biz_url = get_url(results_links)
		
		# uses regex to get naics code from specific website
		naics_code = call_url(biz_url)
		
		
			
master()
		

