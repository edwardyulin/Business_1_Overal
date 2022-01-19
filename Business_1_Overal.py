# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 04:32:49 2020

@author: csmao
"""

import requests
import json
import re
#f = open('business_test.txt')
business = open('business.txt')
#f2 = open('agency_test.txt')
agency = open('agency.txt')
all_business = str(business.readlines()) #O(N)
all_agency = str(agency.readlines()) #O(N)
input_token_business = all_business.split(",") #O(N)
input_token_agency = all_agency.split(",") #O(N)
print("original company =",input_token_business)
print("original agency =",input_token_agency)
business.close()
agency.close()
#f_file = open("business_data.txt","w",encoding="utf-8")
business_status = open("business_status.txt","w",encoding="utf-8")
output=""
total_case = len(input_token_business)*len(input_token_agency) #O(N*N)
case_counter=1


def set_token(temp):
	temp_token = input_token_business[temp] #O(t)
	temp_token = re.findall(r'\d+', temp_token)
	temp_token = str(temp_token)
	# CAN DELETE this line, since it is overwritten by the next line, this will save computational time because
	# txt.split runs on O(N) O(N) will take long, if list is long token = token.split("'")[1]
	temp_token = temp_token.split("'")[0]
	#print(token)
	return temp_token


for t in range(len(input_token_business)): #O(N)
	for t2 in range(len(input_token_agency)): #O(N)
		token = set_token(t)
		token2 = set_token(t2)

		src=str("https://data.gcis.nat.gov.tw/od/data/api/7E6AFA72-AD6A-46D3-8681-ED77951D912D?$format=json&$filter"
				"=President_No eq "+token+" and Agency eq "+token2+"")
		# "https://data.gcis.nat.gov.tw/od/data/api/F05D1060-7D57-4763-BDCE-0DAF5975AFE0?$format=json&$filter
		# =Business_Accounting_NO%20eq%2020828393" print(src)
		r=requests.get(src)
		business=r.text
		#print(business)
		if business!="":
			output = output + str(business)+"\n"
		for i in range(100):
			i+=1
			percent = i/100
			if case_counter/total_case==percent:
				print("已完成百分比 (1是指100%)", percent)
		case_counter+=1
		#	business=json.load(response)
		#clist=business[result]["results"]
	#	with open("business.data.txt","a",encoding="utf-8") as file:
		#with open("results.txt","a",encoding="utf-8") as file:
		#	file.write(str(business)+"\n")
business_status.write(output)
business_status.close()


#need to output: address, name, status (is it still alive)
