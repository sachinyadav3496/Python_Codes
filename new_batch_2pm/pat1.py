print("\n\nWelcome to pattern Program \n\n")

no_row = int(input("Enter No of rows - ")) #taking input for no of lines to print

row_no = 1 #initlizing row no, loop varibale


print("\n")

while row_no <= no_row : #will run loop no_rows time

    col_no = 1 # intilizing col no, inner loop varibale

    while col_no <= row_no :

        print("*",end='')

        col_no += 1

    print()

    row_no += 1






print("\n\nThanks for using Pattern Program \n\n")
