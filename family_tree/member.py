from dataclasses import dataclass, field
from enum import Enum, auto
from typing import List


class Gender(Enum):
    MALE = auto()
    FEMALE = auto()

@dataclass(repr=True)
class Member():
    
    name: str
    gender: Gender
    father: object
    mother: object
    spouse: object = None
    children: List[object] = field(default_factory=list)
    _id: int = 0
    
    @property
    def id(self) -> int:
        return self._id 
       
    def __post_init__(self) -> None:
        self._id += 1
        if self.father is not None and self.father.gender != Gender.MALE:
            raise ValueError(f'Invalid gender: {self.father.gender.name} for father!')
        
        if self.mother is not None and self.mother.gender != Gender.FEMALE:
            raise ValueError(f'Invalid gender: {self.mother.gender.name} for mother!')
            
    def set_spouse(self, spouse: object) -> None:
        if spouse.gender == self.gender:
            raise ValueError('Spouses cannot have same genders!')
        
        self.spouse = spouse
    
    def add_child(self, child: object) -> None:
        if child in self.children:
            raise Exception('Child {child} already exist!')
        self.children.append(child)