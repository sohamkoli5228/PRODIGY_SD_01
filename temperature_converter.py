import os
from datetime import datetime

# -------------------------------
# Temperature Converter
# Developed by: Soham Koli
# -------------------------------

HISTORY_FILE = "conversion_history.txt"


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def header():
    print("=" * 60)
    print("      TEMPERATURE CONVERTER")
    print("=" * 60)


def save_history(text):
    with open(HISTORY_FILE, "a") as file:
        file.write(text + "\n")


def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32


def celsius_to_kelvin(c):
    return c + 273.15


def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9


def fahrenheit_to_kelvin(f):
    return (f - 32) * 5 / 9 + 273.15


def kelvin_to_celsius(k):
    return k - 273.15


def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9 / 5 + 32


def convert_temperature():
    try:
        print("\nSelect Input Unit")
        print("1. Celsius")
        print("2. Fahrenheit")
        print("3. Kelvin")

        choice = input("Enter choice (1-3): ")

        value = float(input("Enter Temperature: "))

        timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        if choice == "1":
            f = celsius_to_fahrenheit(value)
            k = celsius_to_kelvin(value)

            print("\nConversion Result")
            print("-" * 30)
            print(f"Celsius    : {value:.2f} °C")
            print(f"Fahrenheit : {f:.2f} °F")
            print(f"Kelvin     : {k:.2f} K")

            save_history(
                f"[{timestamp}] {value:.2f}°C -> {f:.2f}°F | {k:.2f}K"
            )

        elif choice == "2":
            c = fahrenheit_to_celsius(value)
            k = fahrenheit_to_kelvin(value)

            print("\nConversion Result")
            print("-" * 30)
            print(f"Fahrenheit : {value:.2f} °F")
            print(f"Celsius    : {c:.2f} °C")
            print(f"Kelvin     : {k:.2f} K")

            save_history(
                f"[{timestamp}] {value:.2f}°F -> {c:.2f}°C | {k:.2f}K"
            )

        elif choice == "3":
            if value < 0:
                print("\nKelvin cannot be negative.")
                return

            c = kelvin_to_celsius(value)
            f = kelvin_to_fahrenheit(value)

            print("\nConversion Result")
            print("-" * 30)
            print(f"Kelvin     : {value:.2f} K")
            print(f"Celsius    : {c:.2f} °C")
            print(f"Fahrenheit : {f:.2f} °F")

            save_history(
                f"[{timestamp}] {value:.2f}K -> {c:.2f}°C | {f:.2f}°F"
            )

        else:
            print("\nInvalid Choice!")

    except ValueError:
        print("\nPlease enter a valid numeric value.")


def view_history():
    print("\nConversion History")
    print("-" * 40)

    if not os.path.exists(HISTORY_FILE):
        print("No history found.")
        return

    with open(HISTORY_FILE, "r") as file:
        data = file.read()

        if data.strip() == "":
            print("History is empty.")
        else:
            print(data)


def delete_history():
    if os.path.exists(HISTORY_FILE):
        open(HISTORY_FILE, "w").close()
        print("\nHistory Deleted Successfully.")
    else:
        print("\nNo history file found.")


def about():
    print("\nAbout Project")
    print("-" * 40)
    print("Temperature Conversion Program")
    print("Converts temperatures between")
    print("Celsius, Fahrenheit and Kelvin.")
    print("Developed in Python.")
    print("Features:")
    print("✔ Input Validation")
    print("✔ Conversion History")
    print("✔ Menu Driven")
    print("✔ File Handling")


def menu():
    while True:
        header()

        print("1. Convert Temperature")
        print("2. View Conversion History")
        print("3. Delete History")
        print("4. About Project")
        print("5. Exit")

        choice = input("\nEnter Choice: ")

        if choice == "1":
            convert_temperature()

        elif choice == "2":
            view_history()

        elif choice == "3":
            delete_history()

        elif choice == "4":
            about()

        elif choice == "5":
            print("\nThank you for using Temperature Converter!")
            break

        else:
            print("\nInvalid Choice!")

        input("\nPress Enter to Continue...")
        clear_screen()


if __name__ == "__main__":
    clear_screen()
    menu()