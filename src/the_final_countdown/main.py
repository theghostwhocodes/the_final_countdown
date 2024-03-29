import datetime


DATES = {
    "1": datetime.datetime(year=2020, month=1, day=1),
    "2": datetime.datetime(year=2019, month=10, day=31),
    "3": datetime.datetime(year=2019, month=12, day=25),
}


def main():
    print("=" * 80)
    print("It's the final countdown")
    print("=" * 80)
    print("Select the date:")
    print("1) New year's day 2020")
    print("2) Halloween 2019")
    print("3) Christmas 2019")

    selected_date = input("Date: ")

    try:
        final_countdown_td = DATES[selected_date] - datetime.datetime.now()
        print(f"Days remaining: {final_countdown_td.days}")
    except KeyError:
        print("Please select a valid date")


if __name__ == "__main__":
    main()
