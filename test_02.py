import csv

# filename = '/Users/KellerZhang/Downloads/user story count_PSPS.csv'
def getTotal(filename):
    '''
     get the story points for each developer
    :param filename:
    :return: a dictionary about developer name and its total story points
    '''

    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        dict = {}
        for row in reader:

            if row[5] in dict:
                dict[row[5]] += float(row[9])
            else:
                dict[row[5]] = float(row[9])

    return dict



if __name__ == "__main__":
    filename = '/Users/KellerZhang/Downloads/user story count_PSPS.csv'
    result={}
    #get the result from CSV
    result = getTotal(filename)
    print(result)