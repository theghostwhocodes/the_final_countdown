import datetime

current_year = datetime.datetime.now().year

DATES = {
    "1": datetime.datetime(year=current_year + 1, month=1, day=1),
    "2": datetime.datetime(year=current_year, month=10, day=31),
    "3": datetime.datetime(year=current_year, month=12, day=25),
}


def main():
    print("=" * 80)
    print("It's the final countdown")
    print("=" * 80)
    print("Select the date:")
    print(f"1) New year's day {current_year + 1}")
    print(f"2) Halloween {current_year}")
    print("3) Christmas %d" % current_year)

    selected_date = input("Date: ")

    try:
        final_countdown_td = DATES[selected_date] - datetime.datetime.now()
        print(f"Days remaining: {final_countdown_td.days}")
    except KeyError:
        print("Please select a valid date")


if __name__ == "__main__":
    main()
