books = {
    "python basics": 10,
    "data science": 3,
    "machine learning": 0,
    "ai fundamentals": 5
}

book = input("Enter the book name you want: ").lower()

if book in books:
    while True:
        copies = input("Enter number of copies you want to buy: ")
        if copies.isdigit():
            copies = int(copies)
            break
        else:
            print("Please enter a valid number.")

    available = books[book]

    if available >= copies:
        print("Available")
    elif available > 0:
        print("Partially Available")
    else:
        print("Unavailable")
else:
    print("Unavailable")
