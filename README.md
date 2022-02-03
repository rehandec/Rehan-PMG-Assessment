# Rehan-PMG-Assessment

(Code checked in python for Windows OS)

Steps to run the code:
1. Open CMD
2. Run : $ python code_filename.py csv_filename.csv csv_filename.csv ......... 
   Example:  $python ./csv-combiner.py ./fixtures/accessories.csv ./fixtures/clothing.csv

Input: Csv Files

Output: The program prints dataframe on cmd and also creates a file named 'combined.csv' in the same folder as the code file. This is done as mentioned in the requirements.


Checks Run:
1. No csv files were given in input
2. Files were not found on the folder/ filenames were wrong.
3. Files had no data inside them (empty files)
4. Files had data which gave parsing error (encoding errors)
5. Files with wrong extension given. Here we only considered csv files as mentioned by the assessment requirement.
6. Duplicate file names were given (Here we only considered one file and ignored the duplicate to ensure non replication)

For unit tests:
I believe that I could use bash scripts for running unit tests. But that would mean that the output file 'combined.csv' would be updated as per each test run, and using that script would mean I couldn't check the combined.csv file after each run.

Tests need to be performed by changing the filename argument in the Step 2. These tests are to run for each check mentioned below. 

Also another tests that I can think of it for trying :
1. A single input file, for my code it gives only the file as result, since we append it to output dataframe
2. Multiple files (upwards of thousand) for stress test
3. Files of large sizes : I understand that Pandas is not able to handle files over a particular size limit and thus for files of size above that the code will not work. 

A solution for that stress test for larger sizes can be using dask, which is a framework using parallel processing and essentially similar to pandas. But for the requirment in hand that seems like an overkill.


