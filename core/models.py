from dataclasses import dataclass


@dataclass
class Student:
    username: str
    xp: int = 0
    level: int = 1

    def add_xp(self, amount: int):
        self.xp += amount
        self.level = (self.xp // 100) + 1