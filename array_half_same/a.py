### Solution for the following problem:
### given an array of integers or length n, it is known that one integer repeats at least n/2 times
### find that value with one pass over the array and using no more than 2 variables

### http://stackoverflow.com/questions/744981/array-of-size-n-with-one-element-n-2-times

EXAMPLE = (1,1,1,1,2,1,4,1,5,1,4,1,6,6,8,1,9,1,2,1,1,1,5,5,5,1,1)

def solve(arr):
    # can't do anything with empty arrays
    if not arr:
        return None
    
    # initialize the two variables
    guess, recur = None, 0
    
    # interesting part:
    # keep count of the best guess so far
    # once count is zeroed choose the next item as the guess
    for i in arr:
        if recur == 0:
            guess = i
        recur += 1 if i == guess else -1
    
    # that's it
    return guess

print solve(EXAMPLE)
