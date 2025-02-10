def main():
    # Input information with validation
    name = input("What is his name? ").strip().title()

    try:
        hourly_salary = float(input("What is his hourly salary? ").strip())
        weekly_hours = int(input("How many hours does he work per week? ").strip())
    except ValueError:
        print("Please enter valid numeric values for salary and hours.")
        return

    # Salary calculation
    weekly_salary = hourly_salary * weekly_hours
    monthly_salary = weekly_salary * 4

    # Display the result
    print(
        f"{name} earned {weekly_salary:.2f} euros this week and {monthly_salary:.2f} euros this month!"
    )


if __name__ == "__main__":
    main()
