import random
import smtplib
import math
import os

digits = "0123456789"


class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password


class Advocate(User):
    def __init__(
        self, name, age, case_domain, experience, contact_info, official_address
    ):
        super().__init__(name, None)
        self.age = age
        self.case_domain = case_domain
        self.experience = experience
        self.contact_info = contact_info
        self.official_address = official_address


class Student(User):
    def __init__(self, name, college_name, year):
        super().__init__(name, None)
        self.college_name = college_name
        self.year = year


class LawConnect:
    def __init__(self):
        self.users = {}
        self.advocates = {}
        self.students = {}

        # List of available case domains
        self.case_domains = [
            "Criminal",
            "Property Dispute",
            "Family Law",
            "Corporate",
            "Immigration",
        ]

    def signup(self):
        digits = "0123456789"

        OTP = ""

        for i in range(4):
            OTP += digits[math.floor(random.random() * 10)]

            otp = OTP + " is your OTP"

            message = otp

            s = smtplib.SMTP("smtp.gmail.com", 587)

            s.starttls()

            email = input("Enter your email: ")
            self.user.email(email)

            ap = input("Enter your email app password: ")

            s.login(email, ap)

            s.sendmail("&&&&&&", email, message)

            a = input("Enter your OTP >>: ")

            if a == OTP:
                print("Verified")

            elif a != OTP:
                print("Please Check your OTP\n")

                s.login(email, ap)

                s.sendmail("&&&&&&", email, message)

                a = input("Enter your OTP again>>: ")
                if a == OTP:
                    print("Verified.....")
                else:
                    print("Invalid")

            password = input("Create a password: ")
            password_confirm = input("Confirm your password: ")
            self.user.password(password_confirm)

            if password != password_confirm:
                print("Passwords do not match. Registration failed.")
            elif password == password_confirm:
                pass

                print("Sign-up successful!")
                break

    def create_profile(self, email, profile_type):
        if profile_type == "1":
            name = input("Enter your name: ")
            age = int(input("Enter your age: "))

            # Select a case domain from the available list
            print("Available case domains:")
            for i, domain in enumerate(self.case_domains, start=1):
                print(f"{i}. {domain}")

            domain_choice = int(input("Select a case domain (1-5): "))
            case_domain = self.case_domains[domain_choice - 1]

            experience = input("Enter your experience: ")
            contact_info = input("Enter your contact information: ")
            official_address = input("Enter your official address: ")

            advocate = Advocate(
                name, age, case_domain, experience, contact_info, official_address
            )
            self.advocates[email] = advocate
        elif profile_type == "2":
            name = input("Enter your name: ")
            college_name = input("Enter your college name: ")
            year = input("Enter your year: ")

            student = Student(name, college_name, year)
            self.students[email] = student
        elif profile_type == "3":
            name = input("Enter your name: ")

            user = User(name, email)
            self.users[email] = user

    def login(self):
        email = input("Enter your email address: ")
        if email not in self.users:
            print("Email not registered. Please sign up.")
            return
        elif email in self.users:
            entered_password = input("Enter your password: ")
            stored_password = self.users[email].get("password_confirm", None)

            if entered_password != stored_password:
                print("Incorrect password. Login failed.")
                return

        print("Login successful!")
        user_type = self.users[email]["user_type"]
        if user_type == "1":
            self.search_advocates()
        elif user_type == "2":
            # Student specific menu
            pass
        elif user_type == "3":
            # User specific menu
            pass

    def search_advocates(self):
        print("Available case domains:")
        for i, domain in enumerate(self.case_domains, start=1):
            print(f"{i}. {domain}")

        domain_choice = int(input("Select a case domain (1-5): "))
        selected_domain = self.case_domains[domain_choice - 1]

        print(f"Advocates in the '{selected_domain}' domain:")
        for email, advocate in self.advocates.items():
            if advocate.case_domain == selected_domain:
                print(f"Name: {advocate.name}, Email: {email}")


if __name__ == "__main__":
    law_connect = LawConnect()

    while True:
        print("Welcome to Law Connect")
        print("1. Sign Up")
        print("2. Login")
        print("3. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            law_connect.signup()

        elif choice == "2":
            law_connect.login()

        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")
