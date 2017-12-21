# [2017-12-13] Challenge #344 [Intermediate] Banker's Algorithm
Create a program that will solve the banker’s algorithm. This algorithm stops deadlocks from happening by not allowing processes to start if they don’t have access to the resources necessary to finish. A process is allocated certain resources from the start, and there are other available resources. In order for the process to end, it has to have the maximum resources in each slot.

## Source
https://www.reddit.com/r/dailyprogrammer/comments/7jkfu5/20171213_challenge_344_intermediate_bankers/

## Notes
I learned about this recently in my operating systems class, so the solution was conceptually very simple. My solution may seem very difficult to understand since my attempt to "pythonize" it generally involves making as many things into list comprehension one-liners and using as many Python idioms as possible.
