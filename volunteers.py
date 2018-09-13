#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Application for the input of volunteers for the company outreach projects.
Program records transactions for each payment and saves to .csv file.
A transaction id will also be recorded with the name and payment.
"""
from random import randint
from operator import itemgetter

# Store volunteer name and payment in dictionary format
volunteers_dict = {}

# Store transaction id in a list
transaction_id = []
      
# This function will take a number as input, prompt the user for details
# and return a dictionary with the names and payments for each volunteer
def volunteer_register():
    while True:
        try:
            volunteers = int(input("How many volunteers do you wish to record on file? "))
            if volunteers < 0:
                print("Please enter a non-negative integer")
                return volunteer_register()
            else:
                break        
        except ValueError:
            print("Please enter an integer")
            return volunteer_register()
                   
    # For each item get volunteers name and payment amount       
    for i in range(volunteers):
        
        # Get name and check for alphabet input only then store in dictionary
        while True:
            name = input("Please enter a name: ")          
            volunteers_dict.update({'name': name})
            if all(name.isalpha() or name.isspace() for name in name):                              
                break
            else:
                print("Please enter alphabet characters only")
                           
        # Get payment amount and check for non-negative real number then store in dictionary 
        while True: 
            try:
                payment = float(input("Please enter a payment amount: "))
                volunteers_dict.update({'payment': payment})
                assert(payment > 0), 'Payment must be greater than 0'               
                break
            except:
                print("Please enter a non-negative real number")            


# Function to generate 3 digit transaction id
def serial_gen():
    digit = 3
    range_start = 10**(digit - 1)
    range_end = (10**digit)-1
    transaction_id.append(randint(range_start, range_end))


# This function will take a list of key values from the volunteer
# dictionary, sort them alphabetically and return a sorted list
def sort_volunteers():
    sorted(volunteers_dict, key=itemgetter('name'))


                  