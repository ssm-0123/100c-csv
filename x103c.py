#!python3

"""
You will need to search through the document and find information that is being searched for by the user.
Search for the Equipment Item Number
show the Serial Number

If there are multiple matches, return a list of the serial numbers

Method 1:
Search the entire file, line by line to see if your search string (the needle) is located on the line.
Add the line to a list for later analysis.

For each item in your list, display the relevant information for the line.

"""

def findSerial(needle):
    """
    input: 
    str needle: This is the string to look for
    
    return:
    str: Serial number if there is only 1match
    list: list of str serial numbers if there are multiple matches
    None if no matches
    """
    filename = "data.csv"
    
    
    return None

def main():
    assert findSerial("141769") == "4MLLN73"
    assert findSerial("141") == ['NXEF2AA005608103CA7600', 'BMNWN13', '4MLLN73']
    assert findSerial("134432") == None

if __name__ == "__main__":
    main()
        

