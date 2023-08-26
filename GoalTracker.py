def moneyHave(money, goal):
    if money >= goal:
        return f"You have just enough for your trip ${goal:.2f}"
    else:
        return f"You dont have enough you need ${goal - money:.2f} to reach your goal"

def payCalculated(money, goal):
    hours_per_week = float(input("How many hours do you work per week: "))
    hourly_wage = float(input("What is your hourly wage $"))

    if hours_per_week <= 0 or hourly_wage <= 0:
        return "Hours per week and hourly wage must be greater than zero."

    weekly_earnings = hours_per_week * hourly_wage

    if weekly_earnings <= 0:
        return "Your weekly earnings are not enough to make progress toward your goal."

    weeks_to_goal = (goal - money) / weekly_earnings

    if weeks_to_goal <= 0:
        return "Congratulations! You already have enough money to reach your goal."

    return f"It will take you {weeks_to_goal:.2f} weeks to reach your goal with your current earnings."

def main():
    print("=========== Welcome to Goal Tracker ===========")

    name_of_goal = input("What is the name of your goal: ")
    print(name_of_goal)

    money = float(input("How much money do you have $"))

    goal = float(input("What is your financial goal $"))

    results = moneyHave(money, goal)
    print(results)

    get_ans = input("Would you also like to calculate your paycheck to see how long that would take?(yes or no)")

    if get_ans == "yes".lower():
        paycheck_results = payCalculated(money, goal)
        print(paycheck_results)
    else:
        return "Have a nice day!"

if __name__ == "__main__":
    main()