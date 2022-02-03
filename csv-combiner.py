import os
import pandas as pd
import sys


#inp = input() #Take input
#inp = inp.split(" ") #split input to array of filenames. We use space to seperate filenames.

inp = sys.argv   
#inp = inp.split(" ") 
inp = inp[1:]      

if inp == []:
  print("No file recieved")

#print(inp)

before_rep_check = len(inp)
inp = set(inp)

print(f"{before_rep_check} files combined")

not_csv = 0

df = pd.DataFrame() # create dummy dataframe which we fill
for fname in inp:  #traverse through all filenames
    #print(fname.split("."))
    if fname.split(".")[-1]!= "csv":
      not_csv+=1

    if fname.split(".")[-1]== "csv":  #don't consider files which are not of csv type           
      
      try:
          file_df = pd.read_csv(fname, index_col=0) #read file as a dataframe
      except FileNotFoundError:
          print("File not found.")
      except pd.errors.EmptyDataError:
          print("No data")
      except pd.errors.ParserError:
          print("Parse error")
    
      file_df['filename'] = fname.split("/")[2]      #add filename as an extra column as required                       
      df = df.append(file_df)          #append current file dataframe to the dummy dataframe which we return  
      #print(file_df)

if before_rep_check!= len(inp):
  print(f"{before_rep_check - len(inp)} Files were repeated. We considered only {len(inp)} ignoring duplication.")

if not_csv:
  print(f"Received {not_csv} files which are not csv. Ignored them while combining.")


print(df)                              #print dataframe as required

df.to_csv('combined.csv') #saves a new csv file in the directory as required




