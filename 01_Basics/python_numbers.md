$ python
Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> x = 2
>>> y = 3
>>> z = 4
>>> x+y
5
>>> x**y
8
>>> x + y * z
14
>>> (x + y) * z
20
>>> 40 + 2.23
42.23
>>> int(2.23
... )
2
>>> int(2.89)
2
>>> float(40)
40.0
>>> 'chai' + 'code'
'chaicode'
>>> clear
Traceback (most recent call last):
NameError: name 'clear' is not defined
>>> x,y,z
(2, 3, 4)
>>> x + 1, y*7
(3, 21)
>>> y%2
1
>>> 2**1000
10715086071862673209484250490600018105614048117055336074437503883703510511249361224931983788156958581275946729175531468251871452856923140435984577574698574803934567774824230985421074605062371141877954182153046474983581941267398767559165543946077062914571196477686542167660429831652624386837205668069376
>>> result = 1/3.0
>>> result
0.3333333333333333
>>> ans = 1/3
>>> ans
0.3333333333333333
>>> x < y < z
True
>>> x < y and y < z
True
>>> x < y or y > z
True
>>> 1 == 2<3
False
>>> 1 == 2 and 2 < 3
False
>>> import math
>>> math.floor(3.5)
3
>>> math.floor(-3.5) 
-4
>>> math.trunc(2.8)
2
>>> math.trunc(-2.8) 
-2
>>> 2 + 1j
(2+1j)
>>> (2 + 1j)*3  
(6+3j)
>>> 0o20
16
>>> 0o8
  File "<stdin>", line 1
    0o8
      ^
SyntaxError: invalid digit '8' in octal literal
>>> 0o12
10
>>> 0b111
7
>>> oct(64)
'0o100'
>>> hex(64)
'0x40'
>>> bin(64)
'0b1000000'
>>> int('64',2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 2: '64'
>>> int('64',8) 
52
>>> int('64',16) 
100
>>> a = 1
>>> a << 2
4
>>> import random
>>> random.random()
0.12039657294098727
>>> random.random()
0.44212759311275873
>>> random.random()
0.32849037687407046
>>> random.random()
0.47032489305842906
>>> random.random()
0.280821848186127
>>> random.randint(1,10)
2
>>> random.randint(1,10)
4
>>> random.randint(1,10)
9
>>> random.randint(1,10)
10
>>> random.randint(1,10)
10
>>> l1 = ['lemon','masala','ginger','mint']
>>> random.choice(l1)
'masala'
>>> random.choice(l1)
'ginger'
>>> random.choice(l1)
'ginger'
>>> random.choice(l1)
'masala'
>>> random.choice(l1)
'mint'
>>> random.choice(l1)
'lemon'
>>> from decimal import Decimal
>>> Decimal('0.1') + Decimal('0.1')+Decimal('0.1')
Decimal('0.3')
>>> Decimal('0.1') + Decimal('0.1')+Decimal('0.1')-Decimal('0.3')
Decimal('0.0')
>>> from fractions import Fraction
>>> myFra = Fraction(2,7)
>>> myFra
Fraction(2, 7)
>>> setone = {1,2,3,4}  
>>> setone & {1,3}
{1, 3}
>>> setone | {1,3} 
{1, 2, 3, 4}
>>> setone | {1,3,7} 
{1, 2, 3, 4, 7}
>>> setone - {1,2,3,4}
set()
>>> type(True)
<class 'bool'>
>>>