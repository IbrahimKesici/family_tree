from dataclasses import dataclass, field
from enum import Enum, auto
from typing import List


class Gender(Enum):
    MALE = auto()
    FEMALE = auto()

@dataclass(repr=True)
class Member():
    
    id: int
    name: str
    gender: Gender
    father: object
    mother: object
    spouse: object = None
    children: List[object] = field(default_factory=list)
    
    def add_child(self, child: object) -> None:
        self.children.append(child)
    
    def set_spouse(self, spouse: object) -> None:
        self.spouse = spouse    