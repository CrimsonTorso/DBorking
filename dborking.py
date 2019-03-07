#!/usr/bin/env python

import os
import time
import sys

def author_banner():
	print('''
                _   _                
     /\        | | | |               
    /  \  _   _| |_| |__   ___  _ __ 
   / /\ \| | | | __| '_ \ / _ \| '__|
  / ____ \ |_| | |_| | | | (_) | |   
 /_/    \_\__,_|\__|_| |_|\___/|_|                                
		''')

def dorking_banner():
	print('''
                         
##          #    #          
# # ### ### # #     ##  ### 
# # # # #   ##   #  # # # # 
# # ### #   # #  ## # #  ## 
##                      ### 
                                                       
		''')


def clear_cli():
	responce = os.system("clear")

def welcome_banner():
	print('''
 /$$$$$$$  /$$$$$$$                      /$$       /$$                    
| $$__  $$| $$__  $$                    | $$      |__/                    
| $$  \ $$| $$  \ $$  /$$$$$$   /$$$$$$ | $$   /$$ /$$ /$$$$$$$   /$$$$$$ 
| $$  | $$| $$$$$$$  /$$__  $$ /$$__  $$| $$  /$$/| $$| $$__  $$ /$$__  $$
| $$  | $$| $$__  $$| $$  \ $$| $$  \__/| $$$$$$/ | $$| $$  \ $$| $$  \ $$
| $$  | $$| $$  \ $$| $$  | $$| $$      | $$_  $$ | $$| $$  | $$| $$  | $$
| $$$$$$$/| $$$$$$$/|  $$$$$$/| $$      | $$ \  $$| $$| $$  | $$|  $$$$$$$
|_______/ |_______/  \______/ |__/      |__/  \__/|__/|__/  |__/ \____  $$
                                                                 /$$  \ $$
                                                                |  $$$$$$/
                                                                 \______/ 
                        --------------------------
			| Coded By CrimsonTorso  |
			|                        |
			| Find Website info      |
			| using Google Hacking   |
			| and Python.            |
			--------------------------

		''')

def options():
	print("[1] - Dorking Database")
	print("[2] - Author")
	print("[3] - Quit")


clear_cli()
welcome_banner()

options()
option_pick = raw_input("Please select a valid number: ")

if option_pick == '1':
	clear_cli()
	dorking_banner()
	print("(1) - Find Login Portals")
	print("(2) - SQL Errors")
	print("(3) - Open Directories")
	print("\n")
	dorking_db = raw_input("Please choose an option: ")
	if dorking_db == '1':
		domain_input = raw_input("Please enter a domain: ")
		login_portaled_domain = ("site:" + domain_input + "+inurl:login")
		time.sleep(2.5)
		finished_url = ("https://www.google.com/search?q=" + login_portaled_domain)
		print("Dorked URL: " + finished_url)
		y_o_n = raw_input("Would you like to leave? [y/n]: ")
		if y_o_n == 'y':
			clear_cli()
		if y_o_n == 'n':
			responce = os.system("python dborking.py")
	if dorking_db == '2':
		domain_input2 = raw_input("Please enter a domain: ")
		sql_errored_domain = ("site:" + domain_input2 + "+Error+on+line+27")
		time.sleep(2.5)
		finished_url2 = ("https://www.google.com/search?q=" + sql_errored_domain)
		print("Dorked URL: " + finished_url2)
		y_o_n2 = raw_input("Would you like to leave? [y/n]: ")
		if y_o_n2 == 'y':
			clear_cli()
		if y_o_n2 == 'n':
			responce = os.system("python dborking.py")
	if dorking_db == '3':
		domain_input3 = raw_input("Please enter a domain: ")
		open_vector_domain = ("site:" + domain_input3 + "+index+of+/+")
		time.sleep(2.5)
		finished_url3 = ("https://www.google.com/search?q=" + open_vector_domain)
		print("Dorked URL: " + finished_url3)
		y_o_n3 = raw_input("Would you like to leave? [y/n]: ")
		if y_o_n3 == 'y':
			clear_cli()
		if y_o_n3 == 'n':
			responce = os.system("python dborking.py")
	if dorking_db > '3':
		print("Error: Invalid number!")
		time.sleep(3.0)
		responce = os.system("python dborking.py")
if option_pick == '2':
	clear_cli()
	author_banner()
	print("Github: https://github.com/CrimsonTorso")
	print("Codepen: https://codepen.io/CrimsonTorso")
	time.sleep(9.0)
	responce = os.system("python dborking.py")
if option_pick == '3':
	print("GoodBye!")
	time.sleep(2.5)
	print("\n")
	print("\n")
	

if option_pick > '3':
	responce = os.system("python dborking.py")




#Coded & Developed By CrimsonTorso
