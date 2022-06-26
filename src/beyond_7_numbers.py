from decimal import Decimal

# decimal is like C# decimal
# gotta use the string ctor to work with numbers because otherwise the floats get converted to decimals

a = Decimal(0.8)
b = Decimal(0.7)

c = a-b # this is WRONG

k = Decimal('0.8')
l = Decimal('0.7')

m = k-l # this is CORRECT

# there are some odd quirks...
# don't use with flots, division works differently, math operations are on-class instead of called outside of it.

from fractions import Fraction

two_thirds = Fraction(2, 3)
four_fifths = Fraction(4, 5)

# incorrect with floats
nope = Fraction(0.1)
# but
ye = Fraction(Decimal(0.1)) # Fraction(1, 10)
s = Fraction('22/7') # also works

# complex numbers are also a thing

# python uses EE instead of maths, so it's j not i

complex = 2j

othercomplex = 3 + 4j

