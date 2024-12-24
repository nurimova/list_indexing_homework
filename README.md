# Xush kelibsiz
# RO'YXAT Indeksatsiya

Uy vazifalari va test topshiriqlarini avtomatik baholash
- ushbu repository'ni fork qiling
- vazifani bajaring
- tegishli xabar bilan commit qiling

# Muammolar
## List01

  Natijaga bo'sh ro'yxat qaytaring.

**Misol 1:**

```Python
Input:
Output: []

```

## List02

  Bir nechta elementlardan iborat ro'yxat berilgan. Birinchi elementni qaytaring.

**Misol 1:**

```Python
Input: list1=[1,2,3,4,5]
Output: 1

```

**Misol 2:**

```Python
Input: list1=["x", 1, "y", 2, "z", 3]
Output: "x"

```
**Cheklovlar:**

  - 1 <= length(list1) <= 10^5

## List03

  `list1` va `list2` ro'yxatlari berilgan. Ularni qo'shib (birlashtirib) qaytaring.

**Misol 1:**

```Python
Input: list1=[1, 2, 3, 4, 5]  list2=[6, 7, 8, 9, 10]  
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

```

**Misol 2:**

```Python
Input: list1=["x", 1] list2=["y", 2, "z", 3]
Output: ["x", 1, "y", 2, "z", 3]

```
**Cheklovlar:**

  - 1 <= length(list1) <= 10^5
  - 1 <= length(list2) <= 10^5

## List04

  Bir nechta elementlardan iborat ro'yxat berilgan. Oxirgi elementni qaytaring.

**Misol 1:**

```Python
Input: list1=[1, 2, 3, 4, 5]
Output: 5

```

**Misol 2:**

```Python
Input: list1=[5,3,'a',1,2]
Output: 2

```
**Cheklovlar:**

  - 1 <= length(list1) <= 10^5

## List05

  Bir nechta elementlardan iborat ro'yxat berilgan. `i` indeksdagi elementni qaytaring.

**Misol 1:**

```Python
Input: list1=[1, 2, 3, 4, 5] i=1
Output: 2

```

**Misol 2:**

```Python
Input: list1=[5,3,'a',1,2] i=3
Output: 1

```
**Cheklovlar:**

  - 1 <= length(list1) <= 10^5
  - 0 <= i < length(list1)

## List06

  Uzunligi beshta bo'lgan birliklar va nolalardan iborat ro'yxat berilgan. `1` ni `True` ga o'zgartiring.

**Misol 1:**

```Python
Input: list1=[1, 0, 0, 0, 0]
Output: [True, 0, 0, 0, 0]

```

**Misol 2:**

```Python
Input: list1=[1, 0, 1, 1, 0]
Output: [True, 0, True, True, 0]

```
**Cheklovlar:**

  - length(list1) == 5

## List07

  Uzunligi beshta bo'lgan birliklar va nolalardan iborat ro'yxat berilgan. `0` ni `False` ga o'zgartiring.

**Misol 1:**

```Python
Input: list1=[1, 0, 0, 0, 0]
Output: [1, False, False, False, False]

```

**Misol 2:**

```Python
Input: list1=[1, 0, 1, 1, 0]
Output: [1, False, 1, 1, False]

```
**Cheklovlar:**

  - length(list1) == 5

## List08

  Uzunligi beshta bo'lgan birliklar va nolalardan iborat ro'yxat berilgan. `1` ni `True` ga, `0` ni esa `False` ga o'zgartiring.

**Misol 1:**

```Python
Input: list1=[1, 0, 0, 0, 0]
Output: [True, False, False, False, False]

```

**Misol 2:**

```Python
Input: list1=[1, 0, 1, 1, 0]
Output: [True, False, True, True, False]

```
**Cheklovlar:**

  - length(list1) == 5

## List09

  Bir nechta elementlardan iborat ro'yxat berilgan. Agar barcha elementlar bir xil bo'lsa `True`, aks holda `False` qaytaring.

**Misol 1:**

```Python
Input: list1=[0, 0, 0, 0, 0]
Output: True

```

**Misol 2:**

```Python
Input: list1=['x', 'x', 'y', 'y', 'z']
Output: False

```
**Cheklovlar:**

  - 1 <= length(list1) <= 10^5

## List10

  Bir nechta elementlardan iborat sonli ro'yxat berilgan. Birinchi va oxirgi element orasidan eng kattasini qaytaring.

**Misol 1:**

```Python
Input: list1=[5, 32, 1, 4, 3]
Output: 5

```

**Misol 2:**

```Python
Input: list1=[12, 2, 5, 2, 7, 9, 1]
Output: 12

```
**Cheklovlar:**

  - 1 <= length(list1) <= 10^5

# Ogohlantirish
- boshqa yechimlarni yoki har qanday yechimni nusxa ko‘chirmang
- sharhlarni o‘chirib tashlamang
```
