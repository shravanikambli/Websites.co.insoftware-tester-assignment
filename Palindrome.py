
def check_palindrome():
    text = input("Enter a string: ")

    processed_text = text.lower()

    reversed_text = processed_text[::-1]
   
    print("Reversed string:", reversed_text)

    if processed_text == reversed_text:
        print("This is a palindrome!")
    else:
        print("This is not a palindrome.")


while True:
    check_palindrome()
    
    choice = input("Do you want to check another string? (y/n): ")
    if choice != "y":
        print("Thank you!")
        break

