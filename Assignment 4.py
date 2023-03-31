full_name = input('Enter your Full Name: ').strip().title()
birth_year = int(input("Enter your Birth's year: ").strip())
user_age = 2023 - birth_year

mobile_number = input('Enter your Mobile Number (must be as 05x-xxxx-xxx): ').strip()
if mobile_number[3] != "-" or mobile_number[8] != "-":
    part1 = input('Enter the 1st part of your Mobile Number, ex: (059-xxxx-xxx): ').strip()
    part2 = input('Enter the 2nd part of your Mobile Number, ex: (xxx-1234-xxx): ').strip()
    part3 = input('Enter the 3rd part of your Mobile Number, ex: (xxx-xxxx-567): ').strip()
    mobile_number = part1 + "-" + part2 + "-" + part3
mobile_number_splitted = mobile_number.split('-')

print(full_name)
print(user_age)
print(mobile_number_splitted)