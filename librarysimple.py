list_of_books=[
    "1.Parijaat",
    "2.Shrimad Bhagwat Geeta",
    "3.Fundamentals of Computing",
    "4.Python for Data Science",
    "5.Basics of C Programming"
]
username=input("Username:")
password=input("Password:")
if username=="Student" and password=="Library@12":
    def Student_Details():
        return name,grade,roll_no
    name=input("What is your name?\n")
    grade=int(input("Which class do you study in?\n"))
    roll_no=int(input("Enter your roll no:"))
    Student_Details()
    choice=input("Are you here to take or return book?(T/R)\n")
    match choice:
        case "T":
            print("Here is the list of books that are available.You will have to return the book within 15 days else you will have to pay a fine of Rs100")
            for book in list_of_books:
                print(book)
            user_input=int(input("Tell me the index no of the book you want to take:"))
            print(list_of_books[user_input-1],f":Taken by {Student_Details()}")
        case "R":
           user_return=input("Tell me which book you want to return:")
           list_of_books.append(user_return)
else:
    print("Either username or password is wrong")



        





    
    

