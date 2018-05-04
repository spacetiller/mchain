#!/usr/bin/env python
#-*- coding: utf-8 -*-

import sys
import os
import time
#import hashlib
import random
#import commands
#import urllib
import subprocess
import http.client

import logging
logging.basicConfig(filename='log-shawalker.log',
                    format='%(asctime)s\t%(message)s',
					                    datefmt='%Y-%m-%d %H:%M:%S',
										                    level=logging.DEBUG)

# format='%(asctime)s -%(name)s-%(levelname)s-%(module)s:%(message)s',

def http_get(url, resource, params=''):
	conn = http.client.HTTPSConnection(url, timeout=10)
	conn.request("GET", resource)
	response = conn.getresponse()
	data = response.read().decode('utf-8')
	return data

def utxo_get(data):
	idx = data.find('final_balance')
	if idx <= 0:
		return -1
	idx = idx + 52
	gap = data[idx:].find('<')
	content = data[idx:idx+gap]
	#print(content)
	logging.info(content)
	if not content[0].isdigit() or content[-3:] != 'BTC':
		return -2
	return content[:-3].strip()

def run():
	randkey = ''
	while True:
		for i in range(0,64) :
			a = random.randint(0,15)
			randkey += hex(a)[2:3]
		#print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) + '\tgot: ' + randkey
		#print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()) + '\tgot: ' + randkey)
		logging.info('got: ' + randkey)

		status,btcid= subprocess.getstatusoutput('./bx ec-to-public -u ' + randkey + ' | ./bx sha256 | ./bx ripemd160 | ./bx address-encode')
		#print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()) + '\ttry: ' + btcid)
		logging.info('try: ' + btcid)

		data = http_get('blockchain.info','/address/' + btcid)
		utxo = utxo_get(data)
		if float(utxo) != 0.0:
			print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()) + '\tBingo: ' + randkey + '\t' + btcid)
			logging.info('Bingo!')
		
		#time.sleep(1)
		randkey = ''
		#break

if __name__ == '__main__':
	run()

