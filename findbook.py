collectionOfBooks = ["The Alchemist" , "How to find friends and influence people", "The seven habits of highly effective people"]
print("Enter the name of the book: ")
bookToBeChecked = input()
for book in collectionOfBooks:
    if book == bookToBeChecked:
        print("Yes i do have this book!")
        break 
else:
    print("I do not have that book!")