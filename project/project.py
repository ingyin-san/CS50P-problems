#A flashcard app which allows to study and add flashcards

import csv
import random
import os

def main():
    while True:
        print("Let's start studying with flashcards!")
        print("\t 1. Study flashcards")
        print("\t 2. Add new flashcards")
        print("\t 3. Edit an existing flashcard")
        print("\t 4. Delete a flashcard")
        print("\t 5. Exit")

        action = input("Please choose an option (1, 2, 3, 4, or 5): ").strip()

        if action == "1":
            try:
                study("flashcards.csv")
            except FileNotFoundError:
                print("No flashcards exist! Please create one by choosing option 2: Add new flashcards.")
                continue
        elif action == "2":
            while True:
                question = input("Enter the question (press 'q' to quit): ").strip()

                if question.lower() == "q":
                    break

                answer = input("Enter the answer: ").strip()
                add(question, answer)
        elif action == "3":
            card = input("Enter the question or answer of the flashcard you want to edit: ").strip()
            change = input("Enter the new question or answer for the flashcard: ").strip()
            try:
                edit(card, change)
            except FileNotFoundError:
                print("No flashcards exist! Please create one by choosing option 2: Add new flashcards.")
                continue
        elif action == "4":
            card = input("Enter the question or answer of the flashcard you want to delete: ").strip()
            try:
                delete(card)
            except FileNotFoundError:
                print("No flashcards exist! Please create one by choosing option 2: Add new flashcards.")
                continue
        elif action == "5":
            break


def study(filename):
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        flashcards = list(reader)
        random.shuffle(flashcards)

        if not flashcards:
            print("No flashcards available. Please add some first.")
            return

        correct = 0
        for flashcard in flashcards:
            print("Question:", flashcard["question"])
            answer = input("Answer: ")
            if answer.lower().strip() == flashcard['answer'].lower():
                print("Correct!")
                correct += 1
            else:
                print("Incorrect. The correct answer is:", flashcard["answer"])

        print(f"Score: {correct}/{len(flashcards)}")


def add(question, answer):
    file_exists = os.path.isfile('flashcards.csv')

    with open('flashcards.csv', 'a') as file:
        writer = csv.DictWriter(file, fieldnames = ["question", "answer"])

        if not file_exists:
            writer.writeheader()

        writer.writerow({"question": question, "answer": answer})
        print("A flashcard successfully added!")


def edit(card, change):
    updated = False
    rows = []
    with open("flashcards.csv", 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if (question := card.lower() == row["question"].lower()) or (answer := card.lower() == row["answer"].lower()):
                if question:
                    row["question"] = change
                elif answer:
                    row["answer"] = change
                updated = True

            rows.append(row)

    with open("flashcards.csv", 'w') as file:
        writer = csv.DictWriter(file, fieldnames = ["question", "answer"])
        writer.writeheader()
        for row in rows:
            writer.writerow({"question": row["question"], "answer": row["answer"]})

    if updated:
        print("The flashcard is successfully updated!")
    else:
        print("The flashcard is not found.")


def delete(card):
    new_rows = []
    with open("flashcards.csv", 'r') as file:
        reader = csv.DictReader(file)
        old_rows = list(reader)
        for row in old_rows:
            if (card.lower() != row["question"].lower()) and (card.lower() != row["answer"].lower()):
                new_rows.append(row)

        if len(old_rows) == len(new_rows):
            print("The provided card doesn't exist in the flashcards!")
        else:
            print("The flashcard successfully deleted!")

    with open("flashcards.csv", 'w') as file:
        writer = csv.DictWriter(file, fieldnames = ["question", "answer"])
        writer.writeheader()

        for row in new_rows:
            writer.writerow({"question": row["question"], "answer": row["answer"]})


if __name__ == "__main__":
    main()
