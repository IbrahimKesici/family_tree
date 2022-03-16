from hashlib import new
import pytest

from family_tree.member import Member, Gender

#!: should we test constructor 
#! should we test private variables
#! dunder methods shoudl be tested
#! shoudl we test the python types
#! multiple assertion in one test


@pytest.fixture(scope='class')
def member():
    member = Member(name='father', gender=Gender.MALE, father=None, mother=None) 
    yield member

class TestMember():
    
    def test_init_invalid_father_gender(self) -> None:
        father = Member(name='father', gender=Gender.FEMALE, father=None, mother=None)
        with pytest.raises(ValueError):
            new_member = Member(name='member', gender=Gender.FEMALE, father=father, mother=None)
            
    def test_init_invalid_mother_gender(self) -> None:
        mother = Member(name='mother', gender=Gender.MALE, father=None, mother=None)
        with pytest.raises(ValueError):
            new_member = Member(name='member', gender=Gender.FEMALE, father=None, mother=mother)
        
    def test_set_spouse(self) -> None:
        male_member = Member(name='member1', gender=Gender.MALE, father=None, mother=None)
        female_member = Member(name='member2', gender=Gender.FEMALE, father=None, mother=None)
        
        male_member.set_spouse(female_member)
        assert male_member.spouse == female_member
        
    def test_set_spouse_same_gender(self) -> None:
        male_member_1 = Member(name='member1', gender=Gender.MALE, father=None, mother=None)
        male_member_2 = Member(name='member2', gender=Gender.MALE, father=None, mother=None)
        
        with pytest.raises(ValueError):
            male_member_1.set_spouse(male_member_2)
            
    def test_add_child(self) -> None:
        child = Member(name='child', gender=Gender.MALE, father=None, mother=None)
        father = Member(name='father', gender=Gender.MALE, father=None, mother=None)
        
        father.add_child(child)
        assert child in father.children

        with pytest.raises(Exception):
            father.add_child(child)        