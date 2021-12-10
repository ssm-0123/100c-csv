#!python3

"""
Create a function that will read the contents of the csv file "data.csv" and create a list that stores the contents of each line
"""

def readData():
  '''
  input: none required
  
  return:
  list : contains all of the contents of "data.csv" broken up into lines
  '''
  filename = "data.csv"
  
  return None


def main():
  data = readData()
  assert str(type(data)) == "list"
  assert "Placed in Service" in data[0] == True
  assert "MAC 6c299551c1b5" in data[33] == True
  
if __name__ == "__main__":
  main()
