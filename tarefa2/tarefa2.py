# Task 2 find out if a sequence is a palindrome or not:

# this function reverses a given sequence
# starts at the end of the string '-1' and reads from there to the beginning
def reverse_string(sequence_to_reverse):
    return sequence_to_reverse[::-1]


# function to analise if a sequence reads the same backwards as forwards
# it compares the string with the same string reversed and if both are equal then we have a palindrome
def is_palindrome(sequence_to_check):
    if reverse_string(sequence_to_check) == sequence_to_check:
        return True
    else:
        return False


sequence = input("Please write a number, word or phrase : ")
answer = is_palindrome(sequence)

if answer:
    print(f"'{sequence}' reads the same backwards as forwards, it is a palindrome!")
else:
    print(f"The sequence you provided cannot be read the same backwards as forwards, it is NOT a palindrome.")
