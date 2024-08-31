from termcolor import colored

# Print the ASCII art with green color
print(colored(" ___       _                  _  ____ _               _    ", "green"))
print(colored("|_ _|_ __ | |_ ___  __ _ _ __(_)/ ___| |__   ___  ___| | __", "green"))
print(colored(" | || '_ \\| __/ _ \\/ _` | '__| | |   | '_ \\ / _ \\/ __| |/ /", "green"))
print(colored(" | || | | | ||  __/ (_| | |  | | |___| | | |  __/ (__|   < ", "green"))
print(colored("|___|_| |_|\\__\\___|\\__, |_|  |_|\\____|_| |_|\\___|\\___|_|\\_\\", "green"))
print(colored("                   |___/                                    ", "green"))


def main():
    def entry():
        wordlist = ['password', 'admin', 'root', '1234', 'abcd']
        symbols = ['!', '#', '@', '$', '*', '_']
        numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        password = input("Enter a Password: ")
        score = 0

        def length(password, score):
            if len(password) >= 10:
                score += 1
            elif len(password) in range(6, 10):
                score += 0.5
            # The else clause is unnecessary, as score is not incremented otherwise
            return score

        def uppercase(password, score):
            if any(char.isupper() for char in password):
                score += 1
            # The else clause is unnecessary, as score is not incremented otherwise
            return score

        def symbol_check(password, score):
            if any(symbol in password for symbol in symbols):
                score += 1
            return score

        def lowercase(password, score):
            if any(char.islower() for char in password):
                score += 1
            return score

        def number_check(password, score):
            if any(x in password for x in numbers):
                score += 1
            return score

        def common(password, score):
            if any(y in password for y in wordlist):
                score -= 1
            return score

        # Update score after each function
        score = length(password, score)
        score = uppercase(password, score)
        score = symbol_check(password, score)
        score = lowercase(password, score)
        score = number_check(password, score)
        score = common(password, score)

        # Add more checks as necessary

        print(f"Password score: {score}")
        if score >= 5:
            print(colored('Strong Password', 'green'))
        elif score > 3 and score <5:
            print(colored('Medium Strength', 'yellow'))
        elif score < 3:
            print(colored('Weak Password', 'red'))

    x = True
    while x:
        entry()
        choice = input('Test again or exit ? ').upper()
        if choice == 'TEST AGAIN':
            entry()
        elif choice == 'EXIT':
            x = False


if __name__ == '__main__':
    main()
