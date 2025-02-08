# Operational research and optimization
![Python 3.11.5](https://img.shields.io/badge/Python-3.8.0-yellow?style=plastic)

## Name
Knapsack problem (with branch-and-bound algorithm).

## Description

This is an implementation of the branch-and-bound method for solving the knapsack problem, with the aim of maximizing the value of the (fractional) objects taken while respecting the associated subconditions.
The **0-1 Knapsack Problem** involves selecting a subset of items, each with a **value** and a **weight**, to **maximize** the total value while satisfying a **capacity constraint**.

Here we use the **Branch and Bound** technique to solve this problem efficiently.

## Branch and Bound Method Explanation

1. **Branching**: We divide the problem into subproblems by choosing whether or not to include an object in the bag.
2. **Bounding**: We calculate an upper bound of the best possible solution for a given subproblem.
3. **Pruning**: If a branch cannot yield a better solution than the one found so far, it is ignored.

## Mathematical Formulation

Let:

- \( n \) : the total number of items
- \( w_i \) : the weight of item \( i \)
- \( v_i \) : the value of item \( i \)
- \( W \) : the maximum capacity of the knapsack
- \( x_i \) : a binary decision variable indicating whether item \( i \) is selected (\( x_i = 1 \)) or not (\( x_i = 0 \))

### **Objective: Maximize the total value**

\$
\max \sum_{i=1}^{n} v_i x_i
\$

### **Subject to the capacity constraint:**

\$
\sum_{i=1}^{n} w_i x_i \leq W
\$

### **Binary decision constraints:**

\$
x_i \in \{0,1\}, \quad \forall i \in \{1, ..., n\}
\$

This formulation represents a **classic combinatorial optimization problem**, 
which can be solved using methods such as **Branch and Bound, Dynamic Programming, or Greedy Algorithms**, depending on the context.

## Author
- [Brahim Haroun Hassan]

## License
Academic Free License ("AFL") v. 3.0

## Project Status
Finished

## References
- [Network Project](https://pageperso.lis-lab.fr/~basile.couetoux/enseignement.html)

