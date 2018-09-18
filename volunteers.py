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

# csv file where data is stored and overwritten
input_file = 'record.csv'

# Store transaction id, volunteer names and payments in dictionary format
volunteers = {}
      
# Function will get number of entries, prompt the user for details and
# return a dictionary with the names and payments for each volunteer
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
            
    # For each item assign unique transaction id and get volunteers name and payment amount       
    for i in range(num_volunteers):     
        
        # Get name and check for alphabet input only
        while True: 
            name = input("Please enter a name: ")
            if all(name.isalpha() or name.isspace() for name in name):                              
                break
            else:
                print("Please enter alphabet characters only")
                           
        # Get payment amount and check for non-negative real number 
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
    # Store used serial numbers in a list
    used_serials = []
    
    # Generates 3 random digits
    digit = 3
    range_start = 10**(digit - 1)
    range_end = (10**digit)-1
    random_serial = randint(range_start, range_end)
    random_serial_str = str(random_serial)    
    
    # Returns randomly generated numbers if csv file doesn't exist
    if not os.path.exists(input_file):
        return random_serial_str
    
    # Read csv file and copy all data in column A to used_serial list
    with open(input_file, 'r') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            used_serials.append(row[0])
            
    # Check to see if random number already used in the list
    if random_serial_str in used_serials:
        serial_gen() 
    else:
        return random_serial_str
   

# Function to Quicksort list of tuples and
# return sorted names in alphabetical order
def sort_volunteers(tuple_list):
    l = len(tuple_list) 
    for i in range(0, l): 
        for j in range(0, l-i-1): 
            if (tuple_list[j][1] > tuple_list[j + 1][1]): 
                temp = tuple_list[j] 
                tuple_list[j]= tuple_list[j + 1] 
                tuple_list[j + 1]= temp 
    return tuple_list 
        

# Function calls volunteer_register, serial_gen and sort_volunteers
# Creates a csv file if none exists then records all volunteer details to file
# Stored data passes through sort_volunteers function where it is alphabetically
# sorted and then re-written on the same csv file    
def output_csv():
    volunteer_register() 
    serial_gen()
    
    # Print out sorted input values
    tuple_list_1 = [tuple(line) for line in volunteers.items()]
    sort_volunteers(tuple_list_1)
    
    for key, value in tuple_list_1:
        print("{},".format(key), "{},".format(value[0]), value[1])
    
    # Checks if csv file exists to record volunteer details 
    # if none exists a new csv file is created with a header template
    if not os.path.exists(input_file):
        print('\n')
        print("Data recorded on new file: record.csv")
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
    read_csv = open(input_file, 'r')
    csv1 = csv.reader(read_csv, delimiter=',')       
    header = next(csv1, None) # Ignore reading header
    tuple_list_2 = [tuple(line) for line in csv.reader(read_csv)]

    # Overwrite existing csv file with alphabetically sorted data
    with open(input_file, 'w') as csv_file:
        file_writer = csv.writer(csv_file, delimiter=',', 
                                 quotechar='|', quoting=csv.QUOTE_MINIMAL)
        if header:
            file_writer.writerow(header)
        new_sort = sort_volunteers(tuple_list_2)
        file_writer.writerows(new_sort)

          
# main function    
def main():
    output_csv()
 
    
if __name__ =="__main__":
    main()