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

def getData():
    '''
    Function will read data.csv
    split the file into a list, with 1 line per element
    then, split each element into a list using "," as the delimiter
    you should return a list of lists
    
    '''
    data = open('data.csv', 'r')
    abc = data.readlines()
    newlist = []
    for a in abc:
        newlist.append(a.split(','))
    return newlist


def findSerial(needle):
    """
    input: 
    str needle: This is the string to look for
    
    return:
    dictionary of key, value pairs
    """
    laptoplist = getData()
    result = {}
    for i in laptoplist:
        if needle in i[1]:
            result[i[1]] = i[5]
    return result


def main():
    assert findSerial("141769") == {"141769": "4MLLN73"}
    assert findSerial("134432") == {}
    assert findSerial("141") == {'141610': 'BMNWN13', '141769': '4MLLN73'}

if __name__ == "__main__":
    main()
        

