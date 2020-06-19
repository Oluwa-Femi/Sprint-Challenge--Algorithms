#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)  Runtime complexity is `O(n)` because n increases linearly with each step
        <!-- O(1 + (n * 1))
        O(1 + n) 
        O(n) -->
        
<!-- `O(n^3)` The `while` loop seems to run depending on how big `n^3` is -->

b)  Runtime complexity is `O(n log n)` divided into half and each half is processed again independently.


c)  Runtime complexity is `O(n)` It is still linear, the amount of bunnies doesn't change

## Exercise II

U   - Number of floors is unknown, n
    - Eggs will only break if thrown off floor >= F
    - If egg is dropped off floor < F, eggs will not break
    - Find F such that every floor beneath it doesn't break our eggs

S   - Create a binary search tree from n
    - The root node is the highest floor
    - Check if the egg breaks when dropped on each left node
    - If the egg breaks, continue to the left node
    - else if the egg doesn't break continue to the right node
    - When the egg eventually breaks on a node, save and return that value

The runtime depends on which floor the egg breaks, if it breaks on the first floor that means we have to transverse the entire tree before a value is returned which will mean a runtime of O(n) at the maximum else runtime should be 0(log(n))


