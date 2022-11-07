# Author: Aaron Amran
# Creation Date: 07th November 2022
# Project: Defang or Validate IP Address

# re mmodule for regular expressions
import re

print("\nThis simple program is to defang or validate an IP address.")
print("This is an example of an IP address : 127.0.0.2561")
print("Each IP address can be written as 0 to 255. Example: 0.0.0.0 to 255.255.255.255")
user_ip = input("Please enter an IP address: ")

# regular expression for validating an IP address
ip_regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"

while True:
    print("\nDo you want to "
          "1) Validate"
          "\t2) Defang the IP address?")
    user_choice = input("Please enter a number: ")
    try:
        user_choice = int(user_choice)
    except:
        print('\nPlease enter a valid response.')
        continue

    if user_choice == 1:
        # regex and string is passed into search()
        if re.search(ip_regex, user_ip):
            print("The IP address is valid.")
            break

        else:
            print("The IP address is invalid.")
            break

    elif user_choice == 2:

        defanged_ip = re.sub("[.]", "[.]", user_ip)
        print("\nThe defanged ip is: " , defanged_ip)

        break

    else:
        print('\nPlease enter a valid response.')
        continue

    break
