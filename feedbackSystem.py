from flask import Flask, request, jsonify

app = Flask(__name__)

feedbacks = []

def submit_feedback():
    name = input("Enter your name: ")
    rating = int(input("Enter your rating (1-5): "))
    comment = input("Enter your comment: ")
    feedback = {
        "name": name,
        "rating": rating,
        "comment": comment
    }
    feedbacks.append(feedback)
    print("Feedback submitted successfully.")

def get_all_feedbacks():
    if not feedbacks:
        print("No feedbacks found")
        return
    for feedback in feedbacks:
        print("Name:", feedback["name"])
        print("Rating:", feedback["rating"])
        print("Comment:", feedback["comment"])
        print()

def calculate_average_rating():
    total_ratings = sum(feedback.get("rating", 0) for feedback in feedbacks)
    average_rating  = total_ratings / len(feedbacks) if feedbacks else 0
    print("Average Rating", average_rating)

def menu():
    while True:
        print("1. Submit Feedback")
        print("2. View All Feedbacks")
        print("3. Calculate Average Rating")
        print("4. Exit")
        choice = input("Enter choice: ")
        print()

        if choice == "1":
            submit_feedback()
        elif choice == "2":
            get_all_feedbacks()
        elif choice == "3":
            calculate_average_rating()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Try again")
        print()

if __name__ == "__main__":
    menu()