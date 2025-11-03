**Time complexity**: rate of increase in time with respect to input size

**rules to calculate time complexity**:
- Always calculate TC in terms of worst case `TC = testcase`
- avoid the constant values
- Avoid lower bound

**Space complexity**: 
- **Auxillary space**: the extra space used to solve the problem
- **input space**: space used for storing the input

**Python Time complexity:** https://wiki.python.org/moin/TimeComplexity

example1 
![example1](./img/example1.png)

example 2

**Time complexity**: o(log_10 (N))
``` py
def countLength(num):
    n = num
    count = 0
    while n > 0:
        count += 1
        n = n//10
    return count

num=42673
print(countLength(num))
```
**explanation:**

> from the above code, while loop is ending at n = n//10, thats why its o(log_10 (N))
> where N is input number

---

**Time complexity**: o(log_5 (N))

> dummy example for o(log_5 (N))

``` py
def dummyFn:
    # some code
    while(someCondition):
        # some code
        # some code
        n = n//5 # o(log_5 (N))
    # some code

```
---

