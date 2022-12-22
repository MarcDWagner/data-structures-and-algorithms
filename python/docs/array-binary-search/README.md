# Binary Search of Sorted Array
<!-- Description of the challenge -->
Given a sorted list, use binary search to return the index of a given value, if the value is not present in the list return -1

## Whiteboard Process

![code challenge 3 whiteboard](https://user-images.githubusercontent.com/110312640/209140672-bbd389b4-0c3b-4a31-bb17-78893b647a02.jpg)

## Approach & Efficiency
<!-- What approach did you take? Discuss Why. What is the Big O space/time for this approach? -->
I took the binary search approach.  The value is compared against the middle element in the list, if it's less than the middle value, the upper half is discarded and the lower half is searched in the same manner until the value is found and index returned or values are exhausted and -1 is returned; it is reversed if the value is bigger than the middle element.  Big O for this O(n) because it is depenedent on the starting list size for both space and time.
