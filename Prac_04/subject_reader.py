"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    File_List = get_data()
    Get_Specific_Data(File_List)
    # print(File_List)

    # print("{} is taught by {} and has {} students".format(File_List[0], File_List[1], File_List[2]))



def get_data():
    List = []
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    for line in input_file:
        # print(line)  # See what a line looks like
        # print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        # print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)


        List.append(parts)


    return List

    input_file.close()

def Get_Specific_Data(File_List):
    List_Amount = 0
    for i in File_List:
        List = File_List[List_Amount]
        List_Amount += 1
        print("{} is taught by {} and has {} students".format(List[0], List[1], List[2]))




main()