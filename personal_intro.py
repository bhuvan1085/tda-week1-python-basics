# Week 1 work - Working with Python Fundamentals
# Program for User to Input Details Then Welcome Message

def main():
    # Get user information with input()
    name = input("👤 Please Enter Your Name:  ")
    age = input("🎂 Please Enter Your Age:  ")
    hobby = input("🎯 What is your favorite hobby: ")
    city = input("📍 Please Enter Your City:  ")
    gpa = input("📊 Please Enter Your GPA:  ")

    # Displaying Welcome Message And Details
    print("\n" + "=" * 50)
    print(f"🎉 WELCOME {name.upper()}! 🎉")
    print("=" * 50)
    print(f"👤 Name  : {name}")
    print(f"🎂 Age   : {age}")
    print(f"🎯 Hobby : {hobby}")
    print(f"📍 City  : {city}")
    print(f"📊 GPA   : {gpa}")
    print("=" * 50)
    print(f"✨ {name}, you are {age} years old and love {hobby}! ✨")
    print("=" * 50)

if __name__ == "__main__":
    main()