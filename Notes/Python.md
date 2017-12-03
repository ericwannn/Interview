# Notes on Python learning

## Read input from users

```python
# Python2 style
a = raw_input()

# Python3:
a = input()

# Read multiple variables
import sys
a = sys.stdin.readline().split() # Split by white space

a, b, c = map(int, input().split())

```

## Python Set

```python
a = set(“hello”) # Created a set storing non duplicated elements where a = set([‘H’, ‘e’, ‘l’, ‘o’])

x = set('spam')
y = set(['h','a','m'])
x, y
(set(['a', 'p', 's', 'm']), set(['a', 'h', 'm']))

# Basic operations
a.add(‘element’)    # Add a new single entry
a.update([12,3,5])  # Add new multiple entries
a.remove(‘element’) # Delete a specific entry
a.remove(‘x’)       # Delete x if x exists

# Logical operations

# 交集
x & y
x.intersection(y)

# 并集
x | y
x.union(y)

# 差集
x - y
x.difference(y)
```

## Format control in print()

1. % Control in Python2

    %[(name)][flag][width][.][precision]type

    * name: Optional.
    * flag: Could be +/-/#. + for right alignment, - for left alingment and # fill the blank left trilling space with '0' when base 10, '0x' when base 16 and '0b' when base2
    * width: Minimum width that the output has.
    * [.][precision] Defines the precision of the number.
    * type: %s for string; %d for signed interger(base 10); %f for float

```python
# Python2
# Use % mark to control output format
print %.2f %5
# >> 5.00
print %10.2f %5
# >>        5.00
print %010.2f %5
# >>000000005.00
```

2. % Format control in Python3

    {[name][:][[fill]align][sign][#][0][width][,][.precision][type]}

    * fill: Could be any character
    * align: Could be </^/> where '<' for left; '>' for right and '^' for middle
    * ,: Show Thousandth.

```python

# Use location parameters
li = ['Eric',18]
print('my name is {} ,aged {}'.format('Eric',18))
# >>> 'my name is Eric ,aged 18'
print('my name is {1} ,aged {0}'.format(10,'Eric'))
# >>> 'my name is Eric ,aged 10'
print('my name is {1} ,aged {0} {1}'.format(10,'Eric'))
# >>>'my name is Eric ,aged 10 Eric'
print('my name is {} ,aged {}'.format(*li))
# >>>'my name is Eric ,aged 18'

# Use keyword arguments
print('My name is {name}, aged {age}.'.format(name = 'Eric', age = 18))

# Fill with characters 
print('{0:*>10}'.format(10)) # Right alignment
# >>> ********10
print('{0:*<10}'.format(10)) # Left alignment
# >>> 10********
print('{0:*^10}'.format(10))  # Mid alignment
# >>> ****10****

# Precision and base

'{0:.2f}'.format(1/3)
# >>> '0.33'
'{0:b}'.format(10)    # binary
# >>> '1010'
'{0:o}'.format(10)    # Oct
# >>> '12'
'{0:x}'.format(10)    # Hex
# >>> 'a'
'{:,}'.format(12369132698)  # Thousandth
# >>> '12,369,132,698'
```