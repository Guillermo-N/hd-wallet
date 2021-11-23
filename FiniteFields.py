# %% [markdown]
# # Finite fields
# 
# ## TOC:
# * [Finite field](#finite-fields)
# * [Addition && Subtraction](#field-add-sub)
# * [Multiplication && Exponentiation](#field-mul-expo)
# * [Division](#division)

# %% [markdown]
# ## Finite field <a class="anchor" id="finite-fields"></a>

# %%
class FieldElement:

    def __init__(self, num, prime):
        if num >= prime or num < 0:
            error = 'Num {} not in field range 0 to {}'.format(num, prime - 1)
            raise ValueError(error)
        self.num = num 
        self.prime = prime

    def __repr__(self):
        return 'FieldElement_{}({})'.format(self.prime, self.num)

    def __eq__(self, other):
        if other is None:
            return False
        return self.num == other.num and self.prime == other.prime

    def __ne__(self, other):
        if other is None:
            return False
        return self.num != other.num or self.prime != other.prime

a = FieldElement(7, 13)
b = FieldElement(6, 13)
print(a == b)
print(a == a)
print(a != a)
print(a != b)

# %% [markdown]
# ## Adition && Subtraction<a class="anchor" id="field-add-sub"></a>

# %%

def __add__(self, other):
    if self.prime != other.prime:
        raise TypeError('Cannot add two numbers in different Fields')
    num = (self.num + other.num) % self.prime
    return self.__class__(num, self.prime)


def __sub__(self, other):
    if self.prime != other.prime:
        raise TypeError('Cannot subtract two numbers in different Fields')
    num = (self.num - other.num) % self.prime
    return self.__class__(num, self.prime)

setattr(FieldElement, '__add__', __add__)
setattr(FieldElement, '__sub__', __sub__)

print(a+b)
print(a-b)


# %% [markdown]
# ## Multiplication && Exponentiation <a class="anchor" id="field-mul-expo"></a>

# %%
def __mul__(self, other):
    if self.prime != other.prime:
        raise TypeError('Cannot multiply two numbers in different Fields')
    num = (self.num * other.num) % self.prime
    return self.__class__(num, self.prime)

def __pow__(self, exponent):
    n = exponent % (self.prime - 1)
    num = pow(self.num, n, self.prime)
    return self.__class__(num, self.prime)

setattr(FieldElement, '__mul__', __mul__)
setattr(FieldElement, '__pow__', __pow__)

a = FieldElement(3, 13)
b = FieldElement(12, 13)
c = FieldElement(10, 13)
print(a*b==c)
print(a**4)

a = FieldElement(7, 13)
b = FieldElement(8, 13)
print(a**-3==b)


# %% [markdown]
# ## Division <a class="anchor" id="division"></a>

# %%
def __truediv__(self, other):
    if self.prime != other.prime:
        raise TypeError('Cannot divide two numbers in different Fields')
    num = self.num * pow(other.num, self.prime - 2, self.prime) % self.prime
    return self.__class__(num, self.prime)

setattr(FieldElement, '__truediv__', __truediv__)

a = FieldElement(7, 13)
b = FieldElement(8, 13)
print(a/b)


