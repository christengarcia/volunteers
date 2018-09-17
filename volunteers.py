#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Application for the input of volunteers for company outreach projects.
Program assigns unique transaction id number for each payment then saves 
details to .csv file in alphabetical order. Program will automatically 
create a new record.csv file if non exists.
"""

import os
import csv
import pandas as pd
from random import randint
from collections import OrderedDict

# csv file where data is stored and overwritten
input_file = 'record.csv'

# Store transaction id, volunteer names and payments in dictionary format
volunteers = {}
      
# This function will get number of entries, prompt the user for details
# and return a dictionary with the names and payments for each volunteer
def volunteer_register():
    while True:
        try:
            num_volunteers = int(input("How many volunteers do you wish to record on file? "))
            if num_volunteers < 0:
                print("Please enter a non-negative integer")
                return volunteer_register()
            else:
                break        
        except ValueError:
            print("Please enter an integer")
            return volunteer_register()
            
    # For each item assign transaction id and get volunteers name and payment amount       
    for i in range(num_volunteers):     
        
        # Get name and check for alphabet input only then store in dictionary
        while True: 
            name = input("Please enter a name: ")
            if all(name.isalpha() or name.isspace() for name in name):                              
                break
            else:
                print("Please enter alphabet characters only")
                           
        # Get payment amount and check for non-negative real number then store in dictionary 
        while True: 
            try:
                input_payment = float(input("Please enter a payment amount: "))
                assert(input_payment > 0), 'Payment must be greater than 0'
                payment = '${:.2f}'.format(input_payment)
                break
            except:
                print("Please enter a non-negative real number")  
        # Add transaction id, name and payment data to dictionary
        transaction_id = serial_gen()
        volunteers[transaction_id] = name, payment

    print("\n")
        

# Function to generate 3 digit transaction id then 
# checks numbers in existing csv file for uniqueness
def serial_gen():
    digit = 3
    range_start = 10**(digit - 1)
    range_end = (10**digit)-1
    random_serial = randint(range_start, range_end)
    
    # Store used serials in a list
    used_serials = []
    
    # Check if csv file exists then create a copied list of column A
    if os.path.exists(input_file):
        with open(input_file, 'r') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                used_serials.append(row[0])
                break
    else:
        return random_serial
    
    # Check if random numbers generated is already being used
    if random_serial in used_serials:
        serial_gen()
    else:
        return random_serial

    
# Read existing csv file and convert into list of tuples
# Quicksort tuples alphabetically and overwrite csv file 
def sort_volunteer(tuple_list):
    l = len(tuple_list) 
    for i in range(0, l): 
        for j in range(0, l-i-1): 
            if (tuple_list[j][1] > tuple_list[j + 1][1]): 
                tempo = tuple_list[j] 
                tuple_list[j]= tuple_list[j + 1] 
                tuple_list[j + 1]= tempo 
    return tuple_list 
        

# Function calls volunteer_register, serial_gen and sort_volunteers
# Creates a csv file if none exists then records all volunteer details to file  
def output_csv():
    volunteer_register() 
    serial_gen()
    
    # Print out sorted input values
    alpha = OrderedDict(sorted(volunteers.items(), key=lambda x: x[1]))
    for key, value in alpha.items():
        print("{},".format(key), "{},".format(value[0]), value[1])
    
    # Checks if csv file exists to record volunteer details 
    # if none exists a new csv file is created
    if not os.path.exists(input_file):
        print('\n')
        print("Data recorded on new csv file")
        with open(input_file, 'a') as csv_file:
            file_writer = csv.writer(csv_file, delimiter=',', 
                       quotechar='|', quoting=csv.QUOTE_MINIMAL)
            file_writer.writerow(['Transaction_ID', 'Name', 'Payment'])               
    else:
        print('\n')
        print("Data recorded on existing file")
        
    # Records volunteer details in comma seperated format
    # value_1, value_2, Value_3
    mode = 'a' 
    df = pd.DataFrame(volunteers)
    df = df.transpose()                                   
    df.to_csv(input_file, mode=mode, encoding='utf-8', header=False, sep=',',)
    
    # Read existing csv file and convert into tuple list
    #with open(input_file, 'r') as f:
    read_csv = open(input_file, 'r')
    csv1 = csv.reader(read_csv, delimiter=',')
    
    # Ignore reading header
    header = next(csv1, None)
    create_tuple_list = [tuple(line) for line in csv.reader(read_csv)]

    # Overwrite existing csv file with alphabetically sorted data
    with open(input_file, 'w') as csv_file:
        file_writer = csv.writer(csv_file, delimiter=',', 
                                 quotechar='|', quoting=csv.QUOTE_MINIMAL)
        if header:
            file_writer.writerow(header)
        new_sort = sort_volunteer(create_tuple_list)
        file_writer.writerows(new_sort)

          
# main function    
def main():
    output_csv()
 
    
if __name__ =="__main__":
    main()
