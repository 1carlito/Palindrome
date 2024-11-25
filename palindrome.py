while True:
    print("Palindrome Checker")
    pal = input("Input your Palindrome >\n ").lower().strip()
    
    if len(pal) <= 2:
        print("Invalid input. Must be greater than 2 characters.")
    else:
        if pal == pal[::-1]:  # Slice with `[::-1]` reverses the string
            print("Yes, that is a Palindrome.")
        else:
            print("Unfortunately, this isn't a Palindrome.")
    
    exit_choice = input("Exit (Y/N) > ").upper()
    if exit_choice == "Y":
        break
