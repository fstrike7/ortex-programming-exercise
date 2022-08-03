from datetime import datetime
'''
This task is to fix this code to write out a simple monthly report. The report should look professional.
The aim of the exercise is to:
- Ensure that the code works as specified including date formats
- Make sure the code will work correctly for any month
- Make sure the code is efficient
- Ensure adherence to PEP-8 and good coding standards for readability
- No need to add comments unless you wish to
- No need to add features to improve the output, but it should be sensible given the constraints of the exercise.
Code should display a dummy sales report
'''
### Do not change anything in the section below, it is just setting up some sample data
# test_data is a dictionary keyed on day number containing the date and sales figures for that day
month = "02"
test_data = {f"{x}": {"date": datetime.strptime(f"2021{month}{x:02d}", "%Y%m%d"),
                      'sales': float(x ** 2 / 7)} for x in range(1, 29)}
### Do not change anything in the section above, it is just setting up some sample data
start = test_data[min(test_data.keys())].copy()
end = test_data[max(test_data.keys())].copy()


def DateToDisplayDate(date):
    # E.g. Monday 8th February, 2021
    return (f"""{date.strftime("%a")} {date.strftime("%d")}th {date.strftime("%B")}, {date.strftime("%Y")}""")


start["date"] = DateToDisplayDate(start["date"])
end["date"] = DateToDisplayDate(end["date"])
print("Sales Report\nReport start date: " + start["date"] + "\nstarting value: " + str(
    start["sales"]) + "\nReport end date: " + end["date"] + "\ntotal sales: " + str(end["sales"]) + "\n")
total = 0
print(f"{'Date'.ljust(40)}{'Sales'.ljust(30)}{'Month to Date'.ljust(30)}")
for k, v in test_data.items():
    if month == "2" and k == "29":
        print("Leap year")  # Must be displayed if data is for a leap year
    print(
        f"{DateToDisplayDate(v['date']).ljust(40)}{str(v['sales']).ljust(30)}${str(total).ljust(30)}")
    total += v['sales']
print(f"Total sales for the month:\t{total}")
