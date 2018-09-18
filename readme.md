### Volunteer payment register

This program allows the user to choose any number of names and payment details to be recorded on csv file. A unique transaction id is generated for each entry. It also checks if there is an existing 'record.csv' file and if non exists a new file will be automatically created/saved on pwd. All records on the csv file are automatically sorted and updated in alphabetical order. 

### To run the program under Shell

1. A "shebang" line is already included on the first line of the program which indicates the location of the Python interpreter on the hard drive.

 #!/usr/bin/env python3
 
2. You must make the script executable, using the following command:

 chmod +x volunteers.py

3. You can run the program by invoking the Python interpreter manually as follows:

 python3 volunteers.py

### Program instructions

1. The program will ask you how many volunteers you would like to record. please input a non-negative integer otherwise a ValueError will be trggered.

2. Enter your name using alphabet characters only otherwise you'll be prompted to enter the name again.

3. Enter payment account using non-negative real numbers otherwise a ValueError will be triggered.

4. The program will automatically create a 'record.csv' file for you to view if the file doesn't already exist.