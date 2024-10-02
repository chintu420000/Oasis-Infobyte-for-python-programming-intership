import random

print("Welcome to Password Generator")

letter = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','p','q','r','s','t','u','v','w','x','y','z']
number = ['1','2','3','4','5','6','7','8','9','0']
symbol = ['!','@','#','$','%','^','&','*','(',')']

while True:
    user_choice = int(input("Enter you want to repeat again [0.exit, 1.continue]: "))
    if user_choice == 0:
        break
    elif user_choice == 1:
        password = []
        n_letter = int(input("Enter how many letters do you want: "))
        n_number = int(input("Enter how many numbers do you want: "))
        n_symbol = int(input("Enter how many symbols do you want: "))

        for _ in range(n_letter):
            l = random.choice(letter)
            password.append(l)
        for _ in range(n_number):
            n = random.choice(number)
            password.append(n)
        for _ in range(n_symbol):
            r = random.choice(symbol)
            password.append(r)

        random.shuffle(password)
        password_list = "".join(password)
        print("Generated Password:", password_list)
    else:
        print("Invalid choice. Please enter 0 or 1.")
