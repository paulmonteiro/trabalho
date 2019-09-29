import re


# this function tests passwords for a given criteria and returns a list of the passwords that match that criteria
def test_passwords(passwords_to_test):
    # create a list for storing the passwords that match the criteria
    matched_passwd = []
    # test each password individually
    list_of_passwords = passwords_to_test.split(',')
    for passwd in list_of_passwords:
        # regular expression explanation:
        # (?=.*\d+) means the password must contain a digit
        # and
        # (?=.*[a-zA-Z]) means the password must contain a character lower or uppercase
        # and
        # (?=.*[$#@] means the password must contain at least one of this characters
        # [0-9a-zA-Z$#@]{6,12}  means that the password can only contain digits,
        # alphanumeric chars and the special characters "$#@"
        # with a size limit of {6,12} (6 is the minimum number of chars , 12 is the max)
        if re.search(r"(?=.*\d+)(?=.*[a-zA-Z])(?=.*[$#@])[0-9a-zA-Z$#@]{6,12}", passwd):
            matched_passwd.append(passwd)
    return matched_passwd


# input passwords to be tested separated by comma
passwords = input("Please input a sequence of passwords separated by commas : ")
result = test_passwords(passwords)
print(f"Password(s) that match the criteria : {result}")
