# 0x02. Minimum Operations
`Algorithm` `Python`

For this project, you will need to understand several key algorithmic and mathematical concepts to devise a solution that efficiently calculates the minimum number of operations to achieve a given number of characters using only “Copy All” and “Paste” operations. Here is a list of concepts and resources that will be helpful:

# Concept Needed:
### 1. Dynamic Programming:
Dynamic programming is a method for solving a complex problem by breaking it down into a collection of simpler subproblems, solving each of those subproblems just once, and storing their solutions. The next time the same subproblem occurs, instead of recomputing its solution, one simply looks up the previously computed solution. This method is especially useful when the number of repeating subproblems grows exponentially as a function of the size of the input.
#### example:
    problem: Fibonacci numbers
    subproblem: F(n) = F(n-1) + F(n-2)
    base case: F(0) = 0, F(1) = 1
    solution: F(n) = F(n-1) + F(n-2)
    time complexity: O(n)
    space complexity: O(n)
#### resources:
[Dynamic Programming - GeeksforGeeks](https://www.geeksforgeeks.org/dynamic-programming/)

### 2. Prime Factorization:
Prime factorization is the process of finding the prime numbers that multiply together to make a given number. Prime factorization is useful in solving problems that involve finding the factors of a number, such as finding the greatest common divisor or least common multiple of two numbers.
#### example:
    problem: Prime factorization of 12
    solution: 2 * 2 * 3
#### resources:
[Prime Factorization - Wikipedia](https://en.wikipedia.org/wiki/Prime_factor)

### 3. Code Optimization:
Code optimization is the process of modifying code to make it more efficient, faster, and use fewer resources. Code optimization is important in solving algorithmic problems because it can help reduce the time and space complexity of the solution, making it more efficient and scalable.
#### example:
    problem: Optimize code to find the minimum number of operations to achieve a given number of characters
    solution: Use dynamic programming to store the minimum number of operations for each number of characters
    time complexity: O(n)
    space complexity: O(n)
#### resources:
[Code Optimization - GeeksforGeeks](https://www.geeksforgeeks.org/code-optimization/)

### 4. Greedy Algorithm:
A greedy algorithm is an algorithmic paradigm that follows the problem-solving heuristic of making the locally optimal choice at each stage with the hope of finding a global optimum. Greedy algorithms are used in optimization problems where the goal is to find the best solution from a set of possible solutions.
#### example:
    problem: Minimum operations to achieve a given number of characters
    solution: Use a greedy algorithm to find the minimum number of operations at each stage
    time complexity: O(n)
    space complexity: O(1)
#### resources:
[Greedy Algorithm - GeeksforGeeks](https://www.geeksforgeeks.org/greedy-algorithms/)

### 5. Basic Python Programming:
Basic Python programming skills are essential for solving algorithmic problems. You should be familiar with Python syntax, data structures, control flow, functions, and libraries to implement efficient solutions to algorithmic problems.
#### example:
    problem: Implement a function to calculate the minimum number of operations to achieve a given number of characters
    solution: Use Python functions, loops, and data structures to implement the solution
    time complexity: O(n)
    space complexity: O(n)
#### resources:
[Python Programming - W3Schools](https://www.w3schools.com/python/)




## Additional Resources:
- [Mock Interview](https://intranet.alxswe.com/rltoken/HX0vuVl1V-9T4vvh8NDCyw)


## Requirements:
- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the PEP 8 style (version 1.7.*)
- All your files must be executable
- The length of your files will be tested using wc
- All your modules should have documentation (python3 -c 'print(__import__("my_module").__doc__)')


## Tasks:
- 0. Minimum Operations
In a text file, there is a single character H. Your text editor can execute only two operations in this file: `Copy All` and `Paste`. Given a number `n`, write a method that calculates the fewest number of operations needed to result in exactly n `H` characters in the file.

- Prototype: `def minOperations(n)`
- Returns an integer
- If `n` is impossible to achieve, return `0`

Example:
```
n = 9
H => Copy All => Paste => HH => Paste => HHH => Copy All => Paste => HHHHHH => Paste => HHHHHHHHH
Number of operations: 6
```

```
carrie@ubuntu:~/0x02-minoperations$ cat 0-main.py
#!/usr/bin/python3
"""
Main file for testing
"""

minOperations = __import__('0-minoperations').minOperations

n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

carrie@ubuntu:~/0x02-minoperations$
```

```
carrie@ubuntu:~/0x02-minoperations$ ./0-main.py
Min number of operations to reach 4 characters: 4
Min number of operations to reach 12 characters: 7
carrie@ubuntu:~/0x02-minoperations$
```

**Repo:**
- GitHub repository: `alx-interview`
- Directory: `0x02-minimum_operations`
- File: `0-minoperations.py`