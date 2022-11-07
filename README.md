# Python---Validate-or-Defang-IP-address
Created on 07th November 2022 using PyCharm IDE. Simple program uses regex to validate or defang user input IP address.

## Other options for validating IP address ##

1) Source : https://thispointer.com/check-if-a-string-is-a-valid-ip-address-in-python/
code(
import re 
def valid_IP_Address(sample_str):
    ''' Returns True if given string is a
        valid IP Address, else returns False'''
    result = True
    match_obj = re.search( r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", sample_str)
    if  match_obj is None:
        result = False
    else:
        for value in match_obj.groups():
            if int(value) > 255:
                result = False
                break
    return result
)
