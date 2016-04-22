import csv
import urllib2
import requests


male_black_url = 'https://gist.githubusercontent.com/mbejda/61eb488cec271086632d/raw/6340b8045b28c2abc0b1d44cfbc80f40284ef890/Black-Male-Names.csv'
male_white_url = 'https://gist.githubusercontent.com/mbejda/6c2293ba3333b7e76269/raw/60aa0c95e8ee9b11b915a26f47480fef5c3203ed/White-Male-Names.csv'	
female_black_url = 'https://gist.githubusercontent.com/mbejda/9dc89056005a689a6456/raw/bb6ef2375f1289d0ef10dbd8e9469670ac23ceab/Black-Female-Names.csv'
female_white_url = 'https://gist.githubusercontent.com/mbejda/26ad0574eda7fca78573/raw/6936d1a8f5fa5220f2f60a51a06a35b172c50f93/White-Female-Names.csv'

def downloadData(url):
	r = requests.get(url)
	rawText = r.iter_lines()
	reader = csv.DictReader(rawText, delimiter = ',')
	return reader

def getNameList():
	male_name_list = getMaleName()
	female_name_list = getFemaleName()
	return ([(name, 'male') for name in male_name_list] + [(name, 'female') for name in female_name_list])

def getMaleName():	
	male_white_reader = downloadData(male_black_url)
	male_black_reader = downloadData(male_white_url)
	return ([r['first name'].split(' ')[1] for r in male_white_reader] + [r[' first name'].split(' ')[1] for r in male_black_reader])

def getFemaleName():
	female_white_reader = downloadData(female_white_url)
	female_black_reader = downloadData(female_black_url)
	return ([r[' first name'].split(' ')[1] for r in female_white_reader] + [r[' first name'].split(' ')[1] for r in female_black_reader])