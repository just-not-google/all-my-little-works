from password_generator_human import HumanGenerator
from password_generator_phrase import PhraseGenerator
from password_generator_pincode import PincodeGenerator
from password_generator_random import RandomGenerator
from password_merge_check import MergeCheck
from password_security_check import SecurityCheck
from other_data import fuck_pass_art


def print_menu():
    print("=" * 60)
    print("Password Generator & Security Check Tool")
    print("=" * 60)
    print("Available commands:")
    print("  g_pass human        - Generate human-like passwords")
    print("  g_pass random       - Generate random passwords")
    print("  g_pass phrase       - Generate passwords from phrases")
    print("  g_pass pincode      - Generate pincodes")
    print("  check_security      - Check password security")
    print("  check_leak          - Check if password was leaked")
    print("  recommendations     - Show password creation rules")
    print("  help                - Show this menu")
    print("  exit                - Exit the program")
    print("=" * 60)


def print_recommendations():
    try:
        with open("recommendations.txt", "r", encoding="utf-8") as file:
            content = file.read()
            print("\n" + content)
    except FileNotFoundError:
        print("\nError: recommendations.txt file not found!")
        print("Make sure the file exists in the current directory.")
    except Exception as e:
        print(f"\nError reading recommendations file: {e}")


def display_password_tips():
    tips = [
        "Tip: Aim for at least 20 characters total",
        "Tip: Use random words, not related concepts",
        "Tip: Spread symbols throughout, not just at ends",
        "Tip: Avoid common patterns like '123', '!', 'qwerty'",
        "Tip: Consider using 5-6 random words with separators",
        "Tip: Don't use personal information in passwords",
        "Tip: Each account should have a unique password"
    ]
    print("\n" + "=" * 40)
    print("Password Security Tips")
    print("=" * 40)
    for tip in tips:
        print(tip)
    print("=" * 40)


def handle_human_generator():
    print("Human-like Password Generator")
    print("Enter: length identical_value")
    print("Example: 10 1 (where 1=True for identical_value, 0=False)")
    print("If identical_value=1, all parts will have the same length")

    show_tips = input("Show security tips before generation? (y/n): ").lower()
    if show_tips == 'y':
        display_password_tips()

    hum_an = input("\n>> ")
    try:
        hum_an_lst = hum_an.split(" ")
        if len(hum_an_lst) != 2:
            print("Error: Please enter exactly 2 numbers")
            return

        length = int(hum_an_lst[0])
        identical_value = int(hum_an_lst[1])

        if identical_value not in [0, 1]:
            print("Error: identical_value must be 0 or 1")
            return

        if length < 8:
            print("Warning: For better security, consider using length ≥ 12")
            proceed = input("Continue anyway? (y/n): ").lower()
            if proceed != 'y':
                return

        hum_ann = HumanGenerator(length, identical_value)
        print("\n" + "=" * 40)
        print("Generated password variants:")
        print("=" * 40)
        print(hum_ann)
        print("=" * 40)

        first_password = str(hum_ann).split('\n')[0].split('- ')[-1]
        security_check = SecurityCheck(first_password)
        print("\nSecurity assessment of first variant:")
        print(security_check)

    except ValueError:
        print("Error: Please enter valid integers")
    except Exception as e:
        print(f"Error: {e}")


def handle_random_generator():
    print("Random Password Generator")
    print("Enter: length is_with_word (0=False, 1=True)")
    print("Example: 12 1 (12 characters, include common words)")

    show_tips = input("Show security tips before generation? (y/n): ").lower()
    if show_tips == 'y':
        display_password_tips()

    rand_an = input("\n>> ")
    try:
        rand_an_lst = rand_an.split(" ")
        if len(rand_an_lst) != 2:
            print("Error: Please enter exactly 2 numbers")
            return

        length = int(rand_an_lst[0])
        is_with_word = int(rand_an_lst[1])

        if is_with_word not in [0, 1]:
            print("Error: is_with_word must be 0 or 1")
            return

        if length < 12:
            print("Warning: For strong random passwords, consider length ≥ 16")
            proceed = input("Continue anyway? (y/n): ").lower()
            if proceed != 'y':
                return

        rand_gen = RandomGenerator(length, bool(is_with_word))
        print("\n" + "=" * 40)
        print("Generated password variants (different character sets):")
        print("=" * 40)
        print(rand_gen)
        print("=" * 40)

    except ValueError:
        print("Error: Please enter valid integers")
    except Exception as e:
        print(f"Error: {e}")


def handle_phrase_generator():
    print("Phrase-based Password Generator")
    print("Enter: phrase is_register_replace (0=False, 1=True)")
    print("Example: 'mysecretphrase' 1 (random case changes)")

    show_tips = input("Show security tips before generation? (y/n): ").lower()
    if show_tips == 'y':
        display_password_tips()

    phrase_an = input("\n>> ")
    try:
        parts = phrase_an.split(" ", 1)
        if len(parts) != 2:
            print("Error: Please enter phrase and flag")
            return

        phrase = parts[0]
        is_register_replace = int(parts[1])

        if is_register_replace not in [0, 1]:
            print("Error: is_register_replace must be 0 or 1")
            return

        if len(phrase) < 10:
            print("Warning: Short phrases are easier to crack")
            proceed = input("Continue anyway? (y/n): ").lower()
            if proceed != 'y':
                return

        phrase_gen = PhraseGenerator(phrase, bool(is_register_replace))

        print("\n" + "=" * 40)
        print("Generated passwords from phrase:")
        print("=" * 40)
        for i in range(5):
            password = phrase_gen.generate_phrase()
            print(f"Variant {i + 1}: {password}")

            if i == 0:
                security_check = SecurityCheck(password)
                print(f"Security score: {security_check.calculator_answer()}/7")
        print("=" * 40)

    except ValueError:
        print("Error: Please enter valid values")
    except Exception as e:
        print(f"Error: {e}")


def handle_pincode_generator():
    print("Pincode Generator")
    print("Enter: length (3-12)")
    print("Example: 4 (for 4-digit pincode)")

    print("\nSecurity Note: Pincodes are inherently weak!")
    print("Use only for low-security applications.")
    print("For important accounts, use full passwords.")

    pin_an = input("\n>> ")
    try:
        length = int(pin_an)
        if length < 3 or length > 12:
            print("Error: Length must be between 3 and 12")
            return

        if length < 6:
            print(f"Warning: {length}-digit pincodes are very weak")
            proceed = input("Continue anyway? (y/n): ").lower()
            if proceed != 'y':
                return

        pin_gen = PincodeGenerator(length)
        print("\n" + "=" * 40)
        print("Generated pincodes:")
        print("=" * 40)
        print(pin_gen)
        print("=" * 40)

        print("\nIMPORTANT SECURITY WARNING:")
        print(f"- A {length}-digit pincode has only {10 ** length} possible combinations")
        print(f"- Can be brute-forced in seconds to minutes")
        print(f"- NEVER use for: banking, email, social media")
        print(f"- Only use for: temporary access, low-risk apps")

    except ValueError:
        print("Error: Please enter a valid integer")
    except Exception as e:
        print(f"Error: {e}")


def handle_security_check():
    print("Password Security Check")
    print("Enter password to check:")

    password = input(">> ")
    if not password:
        print("Error: Password cannot be empty")
        return

    security_check = SecurityCheck(password)
    print("\n" + "=" * 40)
    print("Security Analysis:")
    print("=" * 40)
    print(security_check)

    score = security_check.calculator_answer()
    print("\n" + "=" * 40)
    print("Recommendations:")
    print("=" * 40)

    if score >= 6:
        print("Excellent password! Keep using it.")
    elif score >= 4:
        print("Good password, but could be improved:")
        if not security_check.length:
            print("- Increase length to at least 12 characters")
        if not security_check.has_special:
            print("- Add some special characters")
    else:
        print("Weak password! Strongly recommend to change it:")
        print("- Use at least 3 random words with separators")
        print("- Make total length at least 16 characters")
        print("- Avoid common patterns and personal info")

    print("\nFor detailed rules, type 'recommendations'")


def handle_leak_check():
    print("Password Leak Check")
    print("Check if password appears in common leak databases")
    print("Enter password to check:")

    password = input(">> ")
    if not password:
        print("Error: Password cannot be empty")
        return

    merge_check = MergeCheck(password)
    print("\n" + "=" * 40)
    print("Leak Check Results:")
    print("=" * 40)
    print(merge_check)

    if merge_check.local_check():
        print("\nCRITICAL: This password has been leaked!")
        print("Immediately change it on ALL accounts where used.")
        print("Consider using password manager for unique passwords.")
    else:
        print("\nGood: Not found in local leak databases.")
        print("(Note: This doesn't guarantee it hasn't been leaked elsewhere)")


def main():
    print(fuck_pass_art)
    print_menu()

    while True:
        print("\nEnter command (type 'help' for menu):")
        text = input(">> ").strip().lower()

        if text == "exit":
            print("\n" + "=" * 60)
            print("Stay secure! Remember to:")
            print("- Use unique passwords for each account")
            print("- Consider a password manager")
            print("- Enable 2-factor authentication where possible")
            print("=" * 60)
            print("Goodbye!")
            break
        elif text == "help":
            print_menu()
        elif text == "recommendations":
            print_recommendations()
        elif text == "g_pass human":
            handle_human_generator()
        elif text == "g_pass random":
            handle_random_generator()
        elif text == "g_pass phrase":
            handle_phrase_generator()
        elif text == "g_pass pincode":
            handle_pincode_generator()
        elif text == "check_security":
            handle_security_check()
        elif text == "check_leak":
            handle_leak_check()
        elif text == "":
            continue
        else:
            print(f"Unknown command: {text}")
            print("Type 'help' to see available commands")


if __name__ == "__main__":
    main()