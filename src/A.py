
class A:
    def __init__(self, number: int):
        print("A Ctor")
        self.mInt = number

    def get_info(self):
        print(f"{str(self.mInt)}")

    def get_int(self):
        return self.mInt

    def __repr__(self):
        return str("A: " + str(self.mInt))

    def __del__(self):
        print("~A Dtor")

    def __add__(self, other):
        return self.mInt + other.mInt

