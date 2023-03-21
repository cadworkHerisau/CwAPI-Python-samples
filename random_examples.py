# Description: Python random examples
# Author: Michael Brunner

class TestClass:
    """ Test Class
    Operator Overloading
    """

    def __init__(self, aInt: int, aStr: str = ""):
        """ Constructor
        :param aInt: integer value
        """
        self.mInt = aInt
        self.mStr = aStr

    def __str__(self):
        return str(self.mInt) + " " + self.mStr

    def __repr__(self):
        return str(self.mInt) + " " + self.mStr

    def __eq__(self, other):
        return self.mInt == other.mInt

    def __ne__(self, other):
        return self.mInt != other.mInt

    def __lt__(self, other):
        return self.mInt < other.mInt

    def __le__(self, other):
        return self.mInt <= other.mInt

    def __gt__(self, other):
        return self.mInt > other.mInt

    def __ge__(self, other):
        return self.mInt >= other.mInt

    def __add__(self, other):
        return self.mInt + other.mInt

    def __sub__(self, other):
        return self.mInt - other.mInt

    def __mul__(self, other):
        return self.mInt * other.mInt

    def __truediv__(self, other):
        return self.mInt / other.mInt

    def __floordiv__(self, other):
        return self.mInt // other.mInt

    def __mod__(self, other):
        return self.mInt % other.mInt


class A:
    def __init__(self, aInt: int):
        print("A Ctor")
        self.mInt = aInt

    def get_info(self):
        print(f"A: {str(self.mInt):>3}")

    def __repr__(self):
        return str("A: " + str(self.mInt))

    def __del__(self):
        print("A Dtor")


class B(A):
    def __init__(self, aInt: int):
        super().__init__(aInt)
        print("B Ctor")

    def get_info(self):
        print(f"B: {str(self.mInt):>6}")

    def __repr__(self):
        return str("B: " + str(self.mInt))

    def __del__(self):
        print("B Dtor")


class C(B):
    def __init__(self, aInt: int):
        super().__init__(aInt)
        print("C Ctor")

    def get_info(self):
        print(f"C: {str(self.mInt):>9}")

    def __repr__(self):
        return str("C: " + str(self.mInt))

    def __del__(self):
        print("C Dtor")


def test_function(aInt: int):
    return aInt % 2 == 0


def do_something(aCount: int):
    return [TestClass(i) for i in range(aCount)]


def polymorph_test(aInt: int):
    C(aInt)
    local_list = [A(aInt), B(aInt), C(aInt)]
    for il in local_list:
        il.get_info()


if __name__ == '__main__':
    lInt_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    lFiltered_list = list(filter(test_function, lInt_list))
    print(lFiltered_list)

    # filter even numbers
    lInt_list = list(filter(lambda x: x % 2 != 0, lInt_list))
    print(lInt_list)

    print(list(zip([1, 2, 3], ['a', 'b', 'c'])))

    simple_list = [1, 2, 3, 4]
    lIter = iter(simple_list)
    print(lIter.__next__())
    print(lIter.__next__())
    print(lIter.__next__())

    # reset iterator
    print("reset iterator")
    lIter = iter([1, 2, 3, 4])
    i = 0
    while i < len(simple_list):
        print(lIter.__next__())
        i += 1

    print("map")
    lList = list(map(lambda x: x * 2, [1, 2, 3, 4]))
    print(lList)

    print(do_something(20))

    my_class = TestClass(10, "Hello World")
    print(my_class.__class__)
    print(my_class.__dict__)
    print(my_class.__dir__())
    print(my_class.__doc__)

    # get member attribute
    print(my_class.__getattribute__('mInt'))

    # set member attribute
    my_class.__setattr__('mInt', 20)

    print(my_class.__eq__(TestClass(10, "Hello World")))

    # polymorph test
    polymorph_test(10)
