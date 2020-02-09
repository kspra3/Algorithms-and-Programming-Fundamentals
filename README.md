# Algorithms and Programming Fundamentals

## Workshop 1
#### DegToRad.py
Convert a decimal value from Degrees to Radians. 
Print out cosine of this angle.
#### Sum.py
Program to add two numbers and print them.
#### TempConv.py
The conversion from F degrees Fahrenheit to C degrees Celsius.

## Workshop 2
#### AvgList.py
Calculate the average of a list of numbers, received one at a time.
#### CoinToss.py
Write a program that takes a number n as input from the user and simulates n coin flips and print the total number of heads and the total number of tails. Calculate the ratio of heads to the total coin flips.

## Workshop 3
#### ListToTable.py
List of Lists, Tables and References. Write a program that asks user to input 5 lines of numbers. Your program should represent these lines as a table.
```
For example:
Enter some numbers: 1 2 3 4 5 
Enter some numbers: 5 6 7 8 9
Enter some numbers: 1 1 1 1 1
Enter some numbers: 1 5 6 7 2 
Enter some numbers: 0 0 0 0 0
[[1, 2, 3, 4, 5], [5, 6, 7, 8, 9], [1, 1, 1, 1, 1], [1, 5, 6, 7, 2], [0, 0, 0, 0, 0]]
```

## Workshop 4
#### GraphAdjList.py
One way of storing a graph is as an adjacency list, that is, for each vertex we store a list of vertices adjacent to it. For this task you can assume the vertices are numbered 0,1,2,...,n−1 where n ≥ 1. Write a program that takes as input the number of vertices, n, and the name of a file containing an edge list representing a graph. Each line of the file has exactly one edge represented by 2 vertices.Your program should read an edge list from the file and store it as an adjacency list. It should print the adjacency list, so that you can check that you have read the file correctly.
```
For example:
Enter value for n: 4
Enter the filename: testGraph.txt
[[1, 2], [0, 2, 3], [1, 0], [1]]
```
#### GraphAdjMat.py
Another way of storing a graph is as an adjacency matrix, that is, an n × n table A where A[i][ j] = 1 if vertex i is adjacent to vertex j. In this task vertices which represent football teams are numbered 0,1,2,...,n−1, where n is the number of football teams. Two teams are adjacent in the graph, if they have played a match together in 2015. You can assume that two teams played at most one match with each other in 2015. Write a program that takes as input the number of teams, n, and the name of a file containing the edges in the graph. The file is formatted in the same way as the file in the previous tasks. Your program should store the graph as an adjacency matrix. It should print the adjacency matrix, so that you can check that you have read the file correctly.
```
For example:
Enter the number of teams: 4
Enter the filename: testGraph.txt
[[0,1,1,0],[1,0,1,1],[1,1,0,0],[0,1,0,0]]
```

## Workshop 5
#### Task1.py
Write a program that takes as input from the user the name of a file containing the information about the distance a vendor is from Monash and the cost of an item at that vendor. Each line in the file consists of the distance (stored as an integer) followed by a comma followed by the price of that item.
```
For example: the file Tiny.txt contains:
130,266.07
46,174.14
169,187.01
179,488.69
53,401.53
128,106.88
97,398.33
152,493.87
20,205.43
94,248.14
```
Your program should create a list of distance/cost pairs with each pair stored in the list. It should print the list, so that you can check that your program has performed correctly.
```
Enter name of file:  Tiny.txt
[[130, 266.07], [46, 174.14], [169, 187.01], [179, 488.69], [53, 401.53], [128, 106.88],
[97, 398.33], [152, 493.87], [20, 205.43], [94, 248.14]]
```
#### Task2.py

You would like to find a vendor close to Monash. Write a function SelectionSort_Distance that takes as input a list of distance/cost pairs and sorts the list in increasing order of distance using Selection Sort. Use this function to modify the program in Task 2, so that the list is printed in increasing order of distance.
```
For example: your program may do the following:
Enter name of file:  Tiny.txt
20 kms, $205.43
46 kms, $174.14
53 kms, $401.53
94 kms, $248.14
97 kms, $398.33
128 kms, $106.88
130 kms, $266.07
152 kms, $493.87
169 kms, $187.01
179 kms, $488.69
```
#### Task3.py
You would like to be able to sort by price so that you can easily compare the cheapest price of the item compared to the prices of vendors close to Monash. Write a function SelectionSort_Price that takes as input a list of distance/cost pairs and sorts the list in increasing order of price using Selection Sort. Use this function to modify the program in Task 2, so that the list is printed in increasing order of price.
```
For example: your program may do the following:
Enter name of file: Tiny.txt
128 kms, $106.88
46 kms, $174.14
169 kms, $187.01
20 kms, $205.43
94 kms, $248.14
130 kms, $266.07
97 kms, $398.33
53 kms, $401.53
179 kms, $488.69
152 kms, $493.87
```
#### Task4.py
Modify your program in Task 2, so that it repeatedly asks the user to select from the following options:  
• Print - prints the list in the order it is currently sorted (or unsorted order if it has not yet been sorted).  
• Sort1 - sorts the current list in ascending order of distance.  
• Sort2 - sorts the current list in ascending order of price.  
• Quit - program stops.

## Workshop 6
#### NQueens.py
In progress.

## Workshop 7
#### DP.py
In progress.


## Notice of plagiarism
Copying or plagiarising code is a serious offence and will result in a breach in the Academic Integrity Policy https://www.monash.edu/students/academic/policies/academic-integrity.
