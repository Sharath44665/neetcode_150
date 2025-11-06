# Store frequency in Dictionary

## What is store.get(nums[idx],0) + 1 from the code?

lets break one by one

assume: 

**store** = { 1: 3, 2: 3}
**nums** = [1, 2, 3]

``` py
store.get(nums[idx],0) # idx = 1
```

**explanation:**

- if idx=1, then `store.get(nums[idx],0)`, returns 2
- 🔥 if idx = 2, then `store.get(nums[idx],0)`, returns 0

lets evaluate all:

- store.get(nums[idx],0) + 1
> - store <ins>*didn't had*</ins> any nums (that is `store.get(nums[idx],0) + 1`), then it returs zero, after that it adds 1
> 
> - store **had any nums** (that is `store.get(nums[idx],0) + 1`), assume if the idx = 1, in that case, store already got value (that is `store[2] =3`, and <ins>**zero**</ins> won't return ), so 3+1 = 4