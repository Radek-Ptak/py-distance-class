class Distance:

    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: object) -> "Distance":

        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        if isinstance(other, (int, float)):
            return Distance(self.km + other)
        raise TypeError("unsupported type for addition")

    def __iadd__(self, other: object) -> "Distance":

        if isinstance(other, Distance):
            self.km += other.km
            return self
        if isinstance(other, (int, float)):
            self.km += other
            return self
        raise TypeError("unsupported type for addition")

    def __mul__(self, other: object) -> "Distance":

        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        else:
            raise TypeError("unsupported type for multiplication")

    def __truediv__(self, other: object) -> "Distance":

        if isinstance(other, (int, float)):
            if other == 0:
                raise ZeroDivisionError("division by zero")
            return Distance(round(self.km / other, 2))
        else:
            raise TypeError("unsupported type for division")

    def __lt__(self, other: object) -> bool:

        if isinstance(other, (int, float)):
            return self.km < other
        if isinstance(other, Distance):
            return self.km < other.km
        else:
            raise TypeError("unsupported type for comparison")

    def __le__(self, other: object) -> bool:

        if isinstance(other, (int, float)):
            return self.km <= other
        if isinstance(other, Distance):
            return self.km <= other.km
        else:
            raise TypeError("unsupported type for comparison")

    def __gt__(self, other: object) -> bool:

        if isinstance(other, (int, float)):
            return self.km > other
        if isinstance(other, Distance):
            return self.km > other.km
        else:
            raise TypeError("unsupported type for comparison")

    def __ge__(self, other: object) -> bool:

        if isinstance(other, (int, float)):
            return self.km >= other
        if isinstance(other, Distance):
            return self.km >= other.km
        else:
            raise TypeError("unsupported type for comparison")

    def __eq__(self, other: object) -> bool:

        if isinstance(other, (int, float)):
            return self.km == other
        if isinstance(other, Distance):
            return self.km == other.km
        else:
            raise TypeError("unsupported type for comparison")
