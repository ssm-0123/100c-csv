#!python3

"""
Create a function called readAsList()
Function should open data.csv and create a list of lists
Each list contained in the main list is all of the elements from each line.
You will need to use the string.split() command to separate your file into lines,
and each line into a list
"""

def readAsList():
  filename = "data.csv"
  myList = []
  
  return myList

def main():
  data = readAsList()
  assert str(type(data)) == "list"
  assert str(type(data[0])) == "list"
  assert data.find("No.,Equipment Item N") == 0
  assert data.find("Barry") == 27089
  
  
