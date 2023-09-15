years=["Not a leap year","leap year"]
year=int(input("enter a year".))
result=year[(year % 4==0 and year % 100!=0) or(year % 400==0)]
print(f"{year} is a {result}")