
# Version 1: Bygg ett program där användaren kan lägga till saker till en att- göra lista.
todo_list = []

print("Todo list extravaganza")
print("\n1. Se innehållet i din lista📜")
print("2. Lägga till nya punkter i din lista📝")
print("3. Avsluta👋")

while True:

    try:

        choice = input("Välj ett alternativ: ").strip()

        if choice == "1":
            print("Du valde punkt 1.")
            if not todo_list:
                print("Din lista är tom.")
            else:
                print("Din lista:")
                for item in todo_list:
                    print(f"- {item}")

        elif choice == "2":
                print("Du valde punkt 2.")
                new_item = input("Skriv in en ny sak du måste komma ihåg att göra: ")
                todo_list.append(new_item.capitalize())
                print(f"Ok, lade till \"{new_item}\" i listan.")

        elif choice == "3":
            print("Ok, du valde punct 3\nAvslutar programmet. Hej då!")
            break
        else:
            print("Ogiltigt val. Försök igen.")

    except ValueError:
        print("Ogiltigt val. Försök igen.")

# Version 2: lägg till ett menyalternativ, "Markera som klar".
# När användaren väljer det, ska programmet fråga efter vilken grej man är färdig med.
# Den färdiga grejen ska tas bort från listan.
todo_list = []

print("Todo list extravaganza")
print("\n1. Se innehållet i din lista📜")
print("2. Lägga till nya punkter i din lista📝")
print("3. Markera som klar ✅")
print("4. Avsluta👋")


while True:

    try:

        choice = input("Välj ett alternativ: ").strip()

        if choice == "1":
            print("Du valde punkt 1.")
            if not todo_list:
                print("Din lista är tom.")
            else:
                print("Din lista:")
                for item in todo_list:
                    print(f"{item}")

        elif choice == "2":
                print("Du valde punkt 2.")
                new_item = input("Skriv in en ny sak du måste komma ihåg att göra: ")
                todo_list.append(new_item)
                print(f"Ok, lade till \"{new_item}\" i listan.")

        elif choice == "3":
            print("Du valde punkt 3.")
            removed_item = input("Skriv in en sak du vill markera som  klar: ")
            if removed_item in todo_list:
                todo_list.remove(removed_item)
                print(f"\"{removed_item}\" har markerats som klar och tagits bort från listan.")
            else:
                print("Den finns inte i listan.")

        elif choice == "4":
            print("Ok, du valde punct 4\nAvslutar programmet. Hej då!")
            break
        else:
            print("Ogiltigt val. Försök igen.")

    except ValueError:
        print("Ogiltigt val. Försök igen.")


# Version 3: lägg över färdiga grejer i en ny lista.
# Användaren ska kunna välja vad man har bockat av tidigare, eller välja att lägga tillbaka grejen i att-göra-listan.

todo_list = []
done_list = []

print("Todo list extravaganza")
print("\n1. Se innehållet i din lista📜")
print("2. Lägga till nya punkter i din lista📝")
print("3. Markera som klar ✅")
print("4. Lägga tillbaka punkter i din lista📝")
print("5. Avsluta👋")

while True:

    try:

        choice = input("Välj ett alternativ: ").strip()

        if choice == "1":
            print("Du valde punkt 1.")
            if not todo_list:
                print("Din lista är tom.")
            else:
                print(f"Din lista att göra {todo_list}:")
                for item in todo_list:
                    print(f"{item}")

        elif choice == "2":
            print("Du valde punkt 2.")
            new_item = input("Skriv in en ny sak du måste komma ihåg att göra: ")
            todo_list.append(new_item)
            print(f"Ok, lade till \"{new_item}\" i listan 'att göra' {todo_list}.")

        elif choice == "3":
            print("Du valde punkt 3. Markera som klar ✅")
            removed_item = input("Skriv in en sak du vill markera som  klar: ")
            if removed_item in todo_list:
                todo_list.remove(removed_item)
                print(f"\"{removed_item}\" har markerats som klar och tagits bort från listan 'att göra' {todo_list}.")
                done_list.append(removed_item)
                print(f"Ok, lade till \"{removed_item}\" i listan 'done' {done_list}.")
            else:
                print("Den finns inte i listan.")

        elif choice == "4":
            print("Du valde punkt 4. Lägga tillbaka punkter i din lista📝")
            removed_item = input(f"Skriv in en sak som du vill lägga tillbaka i din lista 'att göra' {todo_list}: ")
            if removed_item in done_list:
                todo_list.append(removed_item)
                print(f"\"{removed_item}\" har lagt tillbaka listan 'att göra' {todo_list}.")
            else:
                print("Den finns inte i listan.")

        elif choice == "5":
            print("Ok, du valde punct 5\nAvslutar programmet. Hej då!")
            break
        else:
            print("Ogiltigt val. Försök igen.")

    except ValueError:
        print("Ogiltigt val. Försök igen.")


