class CountFromBy:
    def __init__(self, v: int = 0, i: int = 1) -> None:
        self.val = v
        self.incr = i
    def increase(self) -> None:
        self.val += self.incr
    def __repr__(self) -> str:
        return str(self.val)
    
i = CountFromBy(100,10)
print(i.val)
i.increase()
print(i.val)
print(i)
