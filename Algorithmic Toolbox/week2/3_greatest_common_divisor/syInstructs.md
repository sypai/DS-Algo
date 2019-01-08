## Last Digit of a Large Fibonacci Number

#### Task:
The greatest common divisor GCD(a, b) of two non-negative integers a and b
(which are not both equal to 0) is the greatest integer d that divides both a and b.
Your goal in this problem is to implement the Euclidean algorithm for computing
the greatest common divisor.
Efficient algorithm for computing the greatest common divisor is an important
basic primitive of commonly used cryptographic algorithms like RSA. 
    
    GCD(1344, 217)
    = GCD(217, 42)
    = GCD(42, 7)
    = GCD(7, 0)
    =7

---
#### Input format: 
    The two integers a, b are given in the same line separated by space.
#### Output format:
    Output GCD(a, b)
#### Constraints:
    1 ≤ a, b ≤ 2 · 10 9 .

---
---
#### Sample 1
   Input:
   
    18 35
    
   Output:
   
    1
---
#### Sample 2
   Input:
   
    28851538 1183019    
   Output:
   
    17657

28851538 = 17657 · 1634, 1183019 = 17657 · 67.