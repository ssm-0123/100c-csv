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
    str: Serial number if there is only 1match
    list: list of str serial numbers if there are multiple matches
    None if no matches
    """
    laptoplist = getData()
    result = []
    for i in laptoplist:
        if needle in i[1]:
            result.append(i[5])
    if len(result) == 0:
        return None
    if len(result) == 1:
        return result[0]
    if len(result) > 1:
        return result

print(findSerial("141"))


"""
def main():
    assert findSerial("141769") == "4MLLN73"
    assert findSerial("141") == ['BMNWN13', '4MLLN73']
    assert findSerial("134432") == None

if __name__ == "__main__":
    main()

"""