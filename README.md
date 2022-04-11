This code is the solution for an exercise I did for the course Introduction to Programming with Python at City, University of London. The code determines whether a credit
card number is valid or invalid using the Luhn Check Algorithm. This algorithm is used to check a variety of identification numbers. The 
algorithm has five steps:

1) Double every second digit of the number from right to left, starting from the digit second from the right. If the doubled number has more than two digits, add them together.
For example, doubling 6 produces 12. The numbers 1 and 2 should be added together to get 3. 

For example, for the card number 4388576018402626 first double every second digit, starting from the digit second from the right. This gives 8 16 10 12 2 8 4 4
Then add the individual numbers of the two digit numbers, which gives; 8 7 1 3 2 8 4 4 

2) Add all of the numbers from step 2; 8 + 7 + 1 + 3 + 2 + 8 + 4 + 4 = 37

3) Add the every second number from right to left. For the card number 438857602626 this is 6 + 6 + 0 + 8 + 0 + 7 + 8 + 3 = 38 

4) Add the numbers from steps 2 and 3 

5) If the sum of the numbers from steps 2 and 3 is divisible by 10 with no remainder, the credit card number is valid, otherwise it is invalid. In this case 37 + 38 = 75
75 / 10 = 7.5 Therefore this card number is invalid. 

References:
https://en.wikipedia.org/wiki/Luhn_algorithm
Matthieu Choplin, Introduction to Programming with Python, City, University of London 
