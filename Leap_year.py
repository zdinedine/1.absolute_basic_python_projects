"""In this program, you input a year and check whether it is a leap year or not. For this, you’ll have to create a
function that recognizes the pattern of leap years and can try fitting the inputted year into the pattern. In the
end, you can print the result using a boolean expression."""



def x (leap_year):
    if leap_year%4 == 0 or leap_year%100 == 0:
        print (f"{leap_year} is a leap year")
    else: print (f"{leap_year} is not a leap year")


leap_year = int(input("Enter the year"))
x(leap_year)
