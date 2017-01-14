# -*- coding:utf-8 -*-
from pymongo import MongoClient
import pymongo
from selenium import webdriver
import selenium
import time
from progressbar import ProgressBar
from datetime import datetime
import random
from selenium.webdriver.common.keys import Keys

def merge():
	client = MongoClient('192.168.11.153', 27018)
	db_t = client['JD']
	col_t = db_t['phone']
	db_s = client['JD2']
	col_s = db_s['phone']
	for item in col_s.find().batch_size(100):
		url = item['url']
		good = item['good']
		neutral = item['neutral']
		bad = item['bad']
		target = col_t.find_one({"url":url})
		if len(target) > 0:
			target['url'] = url
			target['positive_assess_count'] = good
			target['neutral_assess_count'] = neutral
			target['negative_assess_count'] = bad
			col_t.update({'url':url},target)
			print url
		else:
			print 'error in: ', url
			break

def check():
	client = MongoClient('192.168.11.153', 27018)
	db_t = client['JD']
	col_t = db_t['phone']
	miss_count = 0
	for item in col_t.find().batch_size(100):
		try:
			print item['positive_assess_count']
		except:
			miss_count = miss_count + 1
	print str(miss_count), ' item have no counts.'

if __name__ == '__main__':
	#driver = webdriver.Firefox()
	check()
	