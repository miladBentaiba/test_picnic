Dear candidate,

Thank you for your interest in Picnic and for taking the time to
apply.

For this part of the application process, we would like you to solve 3
puzzles, with Python. While the time it will take you to complete them
is not measured, we estimate it should take you 1 hour.

## Instructions

- The exercises are described in this file, in the sections below.

- You should fill the attached file `main.py`. It contains a basic
  skeleton of 3 functions, corresponding to the 3 exercises.

- All 3 exercises are independent.

- You are allowed (and encouraged!) to modify the `__main__` part of
  the program, e.g. to add more test cases.

- Please only use Python's standard library. If you think the problem
  would be better solved with an external dependency, write down a
  reasoning (e.g. in a comment before the `import`).

- Some exercises are focused on the correctness of your solution, and
  some on the correctness and performance.

- If you have any, write notes about the different exercises in the
  corresponding function docstring. We would appreciate if you write
  the big-O complexity of your solutions there as well.
  
- We will carefully read your solutions, and while there is a focus on
  the general correctness of your algorithms, you will gain extra
  points for "clean" code (good variable names, types hinting, etc).
  
- If you have any question, feel free to ask us!

Good luck, and we hope you enjoy the puzzles!


## Maximum of one-digit integers

Write a function:

    def max_of_one_digit_ints(integers)

that, given an array `integers` consisting of N integers, returns the maximum
among all one-digit integers.

For example, given array `integers` as follows:

    [-6, -91, 1011, -100, 84, -22, 0, 1, 473]

the function should return 1.

Assume that:

- N is an integer within the range [1..1,000];
- each element of array `integers` is an integer within the range [−10,000..10,000];
- there is at least one element in the array which satisfies the condition in the task statement.

In your solution, focus on correctness. The performance of your
solution will not be the focus of the assessment.


## Maximum number of candies

Mary has N candies. The i-th candy is of a type represented by an
integer `candies[i]`.

Mary's parents told her to share the candies with her brother. She
must give him exactly half the candies. Fortunately, the number of
candies N is even.

After giving away half the candies, Mary will eat the remaining
ones. She likes variety, so she wants to have candies of various
types. Can you find the maximum number of different types of candy
that Mary can eat?

Write a function:

    def max_number_of_candies_types(candies)

that, given an array `candies` of N integers, representing all the
types of candies, returns the maximum possible number of different
types of candy that Mary can eat after she has given N/2 candies to
her brother.

For example, given:
    candies = [3, 4, 7, 7, 6, 6]

the function should return 3. One optimal strategy for Mary is to give
away one candy of type 4, one of type 7 and one of type 6. The
remaining candies would be [3, 7, 6]: three candies of different
types.

Given:
    candies = [80, 80, 1000000000, 80, 80, 80, 80, 80, 80, 123456789]

the function should also return 3. Here, Mary starts with ten
candies. She can give away five candies of type 80 and the remaining
candies would be [1000000000, 123456789, 80, 80, 80]. There are only
three different types in total, i.e. 80, 1000000000 and 123456789.

Write an efficient algorithm for the following assumptions:

- N is an integer within the range [2..100,000];
- N is even;
- each element of array `candies` is an integer within the range [1..1,000,000,000].


## Digits sequence

Let's consider the following infinite sequence:
0, 1, 1, 2, 3, 5, 8, 13, 12, 7, 10, 8, 9, ...

The 0th element is 0 and the 1st element is 1. The successive elements
are defined recursively. Each of them is the sum of the separate
digits of the two previous elements.

Write a function:

    def digits_sequence(n)

that, given an integer `n`, returns the `n`-th element of the above sequence.

Examples:

1. Given n = 2, the function should return 1.
2. Given n = 6, the function should return 8.
3. Given n = 10, the function should return 10.

Write an efficient algorithm for the following assumption:

- `n` is an integer within the range [0..1,000,000,000].
