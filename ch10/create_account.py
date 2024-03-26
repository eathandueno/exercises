def main():
    full_name = get_full_name()
    print()

    password = get_password()
    print()

    email = get_email()
    print()

    phone_number = get_phone_number()
    print()

    first_name = get_first_name(full_name)   
    print(f"Hi {first_name}, thanks for creating an account.")
    print(f"Your registered email is: {email}")
    print(f"Your registered phone number is: {format_phone_number(phone_number)}")

def get_full_name():
    while True:
        name = input("Enter full name:       ").strip()
        if " " in name:
            return name
        else:
            print("You must enter your full name.")

def get_first_name(full_name):
    index1 = full_name.find(" ")
    first_name = full_name[:index1]
    return first_name

def get_password():
    while True:
        digit = False
        cap_letter = False
        password = input("Enter password:        ").strip()
        for char in password:
            if char.isdigit():
                digit = True
            elif char.isupper():
                cap_letter = True
        if digit == False or cap_letter == False or len(password) < 8:
            print(f"Password must be 8 characters or more \n"
                  f"with at least one digit and one uppercase letter.")
        else:
            return password

def get_email():
    while True:
        email = input("Enter email:        ").strip()
        if "@" in email and email.endswith(".com"):
            return email
        else:
            print("You must enter a valid email address.")

def get_phone_number():
    while True:
        phone_number = input("Enter phone number:        ").strip()
        phone_number = phone_number.replace(" ", "").replace("-", "").replace("(", "").replace(")", "").replace(".", "")
        if phone_number.isdigit() and len(phone_number) == 10:
            return phone_number
        else:
            print("You must enter a valid phone number.")

def format_phone_number(phone_number):
    return f"{phone_number[:3]}.{phone_number[3:6]}.{phone_number[6:]}"

if __name__ == "__main__":
    main()