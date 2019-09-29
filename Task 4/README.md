Objective: Create a Python script that reads a file with the following JSON content:

[
   {
       "name": "first",
       "color": "red",
       "min_version": 1.1,
       "max_version": 1.3
   },
   {
       "name": "second",
       "color": "blue",
       "min_version": 1.0,
       "max_version": 1.1
   },
   {
       "name": "third",
       "color": "red",
       "min_version": 1.2,
       "max_version": 1.4
   },
   {
       "name": "fourth",
       "color": "red",
       "min_version": 1.3,
       "max_version": 1.4
   },
   {
       "name": "fifth",
       "color": "green",
       "min_version": 1.2,
       "max_version": 1.3
   },
   {
       "name": "sixth",
       "color": "red",
       "min_version": 2.0,
       "max_version": 2.1
   },
   {
       "name": "seventh",
       "color": "green",
       "min_version": 1.2,
       "max_version": 1.3
   }
]

...and identify the compatible element groups, printing one group per line. 
Compatible elements are considered to be those whose 'color' attribute is equal and also those that the interception between the intervals 
composed of 'min_version' and 'max_version' are not empty. For example, in the above case, the result would be:

first third fourth
second
fifth seventh
sixth
