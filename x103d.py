#!python3

"""
You will need to search through the document and find information that is being searched for by the user.
Search for the Equipment Item Number
show the Serial Number

If there are multiple matches, return a list of the serial numbers

Method 2:
Create a list of lists using the data file
Search through all of the equipment item numbers
Create an empty dictionary data item and add all of the Equipment Item Numbers and Serial numbers as key,value pairs

Return the dictionary item

"""

def findSerial(needle):
    """
    input: 
    str needle: This is the string to look for
    
    return:
    dictionary of key, value pairs
    """
    filename = "data.csv"


def main():
    assert findSerial("141769") == {"141769": "4MLLN73"}
    assert findSerial("134432") == {}
    assert findSerial("141") == {'138101': 'NXEF2AA005608103CA7600', '141610': 'BMNWN13', '141769': '4MLLN73'}

if __name__ == "__main__":
    main()
        

