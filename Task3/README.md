The objective is to write a program that checks password validity according to the following rules:

A. At least one lowercase letter [a-z]
B. At least one capital letter [A-Z]
C. At least one number [0-9]
D. At least one character of the following [$ # @]
E. Minimum Length: 6
F. Max Length: 12

The program must receive a sequence of passwords separated by commas, and it must verify if they are in accordance with  
the above rules. 
The passwords that pass the criteria should be displayed on the screen and all others that don't should just be ignored. 
Example, with the following input:
ACd1234@1,a F1#,2w1E*,2Wz3345
We should obtain the following output:
ACd1234@1 
