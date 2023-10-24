'''
CS1026a 2023
Assingment 2 - Library
Isa Khan
251337547
ikhan97
10/23/2023
'''

def start():

    #Adding the inital books to a list
    allBooks = [
                ['9780596007126',"The Earth Inside Out","Mike B",2,['Ali']],
                ['9780134494166',"The Human Body","Dave R",1,[]],
                ['9780321125217',"Human on Earth","Jordan P",1,['David','b1','user123']]
           ]
    borrowedISBNs=[]
    #String of valid inputs for menu choice
    valid_inputs = "12345artlx"  
    run = True

    #Checking for proper user input for menu selection
    while run:
        valid_user_in = False
        while valid_user_in == False:
            printMenu()
            user_input = input("Your selection> ").lower()

            if user_input in valid_inputs and len(user_input) == 1:  #Checking if user input is part of valid inputs
                valid_user_in = True
            else:
                print("Wrong selection! Please selection a valid option.\n")

        #Selecting appropriate menu option based on user input
        if user_input == "a" or user_input == "1":  #Cases for valid number/letter inputs
            addBook(allBooks)
        elif user_input == "r" or user_input == "2":
            borrowBook(allBooks, borrowedISBNs)
        elif user_input == "t" or user_input == "3":
            returnBook(allBooks, borrowedISBNs)
        elif user_input == "l" or user_input == "4":
            listBooks(allBooks, borrowedISBNs)
        else:
            print("$$$$$$$$ FINAL LIST OF BOOKS $$$$$$$$")  #Exit case
            listBooks(allBooks, borrowedISBNs)
            run = False
    
#Function to print menu options
def printMenu():
    print('\n######################')
    print('1: (A)dd a new book.')
    print('2: Bo(r)row books.') 
    print('3: Re(t)urn a book.') 
    print('4: (L)ist all books.') 
    print('5: E(x)it.') 
    print('######################\n') 

#Function to add a book
def addBook(allBooks): 
    name_check = False
    edition_check = False

    #Checking validity of book name
    while name_check == False:
        name = input("Book name> ")
        if "*" in name or "%" in name:
            print("Invalid book name!")
        else:
            name_check = True
    author = input("Author name> ")

    #Checking validity of edition input
    while edition_check == False:
        edition = input("Edition> ")
        if edition.isdigit():
            edition_check = True
        else:
            print("Invalid edition number!")

    #Sending ISBN to checking method
    ISBN = ISBN_check(allBooks)
    if ISBN != 0:
        oneNewBook = [ISBN, name, author, edition,[]]
        allBooks.append(oneNewBook)
        print("A new book is added successfully.\n")

#Function to see if an ISBN is valid
def ISBN_check(allBooks):
    initial_check = False
    used = False
    weight = [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1]

    #Checking length of the ISBN input
    while initial_check == False:
        ISBN = input("ISBN> ")
        if len(ISBN) == 13 and ISBN.isdigit():
            initial_check = True
        else:
            print("Invalid ISBN!")
    sum = 0

    #Finding sum of ISBN entered
    for num in range(13):
        select_num = int(ISBN[num])
        number = weight[num] * select_num
        sum += number

    #Comparing to currently used ISBNs
    for num in range (len(allBooks)):
        if allBooks[num][0] == ISBN:
            used = True
            print("Duplicate ISBN is found! Cannot add the book.") #Output for a duplicate
            return 0
    if sum % 10 == 0 and used == False:
        return ISBN
    else:
        print("Invalid ISBN!")
        return 0

#Function to list books
def listBooks(allBooks, borrowedISBNs):
    for num in range(len(allBooks)):
        availability = "Available"  
        #Determining availability for each book
        if allBooks[num][0] in borrowedISBNs:
            availability = "Unavailable"
            #Printing output of list function
        print(f"-"*15+f"\n[{availability}]\n{allBooks[num][1]} - {allBooks[num][2]}\n"
              +f"E: {allBooks[num][3]} ISBN: {allBooks[num][0]}\nborrowed by: {allBooks[num][4]}")

#Function to borrow books
def borrowBook(allBooks, borrowedISBNs):
    user_name = input("Enter the borrower name> ")
    search_term = input("Search Term> ").lower()
    found = []
    #Case for % at the end of search term
    if search_term[-1] == "%":
        for num in range (len(allBooks)):
            if allBooks[num][0] not in borrowedISBNs and allBooks[num][1][:len(search_term)-1].lower() == search_term[:len(search_term) - 1]:
                found.append(allBooks[num][0])
                allBooks[num][-1].append(user_name)
                print(f'\t-"{allBooks[num][1]} is borrowed!"')
    #Case for * at the end of search term
    elif search_term[-1] == "*":
        for num in range (len(allBooks)):
            if allBooks[num][0] not in borrowedISBNs and search_term[:len(search_term) - 1] in allBooks[num][1].lower():
                found.append(allBooks[num][0])
                allBooks[num][-1].append(user_name)
                print(f'\t-"{allBooks[num][1]} is borrowed!"')
    #Case for specific search
    else:
        for num in range (len(allBooks)):
            if allBooks[num][1].lower() == search_term and allBooks[num][0] not in borrowedISBNs:
                found.append(allBooks[num][0])
                allBooks[num][-1].append(user_name)
                print(f'\t-"{allBooks[num][1]} is borrowed!"')
    #Borrowing books found
    for element in found:
        borrowedISBNs.append(element)
    if len(found) == 0:
        print("No books found!")

#Function to return a book
def returnBook(allBooks, borrowedISBNs):
    ISBN = input("ISBN: ")
    #Seeing if ISBN is in the list of Borrowed ISBNs
    if ISBN in borrowedISBNs:
        #Checking which book is being returned
        for num in range (len(allBooks)):
            if ISBN == allBooks[num][0]:
                print(f'"{allBooks[num][1]}" is returned')
        borrowedISBNs.remove(ISBN)
    #Telling user no book was found
    else:
        print("No book is found!")
    

start()