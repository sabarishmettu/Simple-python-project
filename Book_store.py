# Define a dictionary of books with their ID numbers and prices
books = {
    1: {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "price": 10.99},
    2: {"title": "To Kill a Mockingbird", "author": "Harper Lee", "price": 9.99},
    3: {"title": "1984", "author": "George Orwell", "price": 8.99},
    4: {"title": "Animal Farm", "author": "George Orwell", "price": 7.99},
    5: {"title": "Brave New World", "author": "Aldous Huxley", "price": 11.99},
    6: {"title": "Lord of the Flies", "author": "William Golding", "price": 9.99},
    7: {"title": "Pride and Prejudice", "author": "Jane Austen", "price": 12.99},
    8: {"title": "Sense and Sensibility", "author": "Jane Austen", "price": 11.99},
    9: {"title": "Emma", "author": "Jane Austen", "price": 10.99},
    10: {"title": "The Catcher in the Rye", "author": "J.D. Salinger", "price": 8.99},
    11: {"title": "To the Lighthouse", "author": "Virginia Woolf", "price": 11.99},
    12: {"title": "Mrs. Dalloway", "author": "Virginia Woolf", "price": 10.99},
    13: {"title": "The Sun Also Rises", "author": "Ernest Hemingway", "price": 9.99},
    14: {"title": "For Whom the Bell Tolls", "author": "Ernest Hemingway", "price": 11.99},
    15: {"title": "The Old Man and the Sea", "author": "Ernest Hemingway", "price": 7.99},
    16: {"title": "One Hundred Years of Solitude", "author": "Gabriel Garcia Marquez", "price": 12.99},
    17: {"title": "Love in the Time of Cholera", "author": "Gabriel Garcia Marquez", "price": 11.99},
    18: {"title": "The Name of the Rose", "author": "Umberto Eco", "price": 10.99},
    19: {"title": "The Picture of Dorian Gray", "author": "Oscar Wilde", "price": 9.99},
    20: {"title": "The Importance of Being Earnest", "author": "Oscar Wilde", "price": 8.99},
}

# Display a list of books with their ID numbers
print("Welcome to the bookstore!")
print("Here are the books available for purchase:\n")
for id, book in books.items():
    print(f"{id}: {book['title']} by {book['author']} (${book['price']})")
print()

# Prompt the user to enter the ID number of the book they want to buy
selected_id = int(input("Enter the ID number of the book you want to buy: "))

# Check if the selected ID number is valid
if selected_id not in books:
    print("Invalid ID number. Please try again.")
else:
    # Get the selected book and its details
    selected_book = books[selected_id]
    title = selected_book["title"]
    author = selected_book["author"]
    price = selected_book["price"]
    
    # Display the details of the selected book
    print(f"\nYou selected: {title} by {author} (${price})")
    
    # Prompt the user to enter the quantity of the book they want to buy
    quantity = int(input("Enter the quantity of books you want to buy: "))
    
    # Calculate the total cost of the selected books
    total_cost = price * quantity
    
    # Display the total cost of the selected books
    print(f"\nThe total cost of {quantity} copies of {title} by {author} is ${total_cost}.")
    print("Thank you for shopping at the bookstore!")


