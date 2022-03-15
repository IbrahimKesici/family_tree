import pytest

from family_tree.member import Member, Gender

#!: should we test constructor 

@pytest.fixture(scope='class')
def member():
    member = Member(id=1, name='father', gender=Gender.MALE, father=None, mother=None) 
    yield member

class TestMember():
    
    def test_add_child(self, member):
        child = Member(id=2, name='child_1', gender=Gender.MALE, father=member, mother=None) #TODO: check
        member.add_child(child)
        
        assert child in member.children
    
    def test_added_child_is_unique(self, member): #TODO:check
        child = Member(id=3, name='child_1', gender=Gender.MALE, father=member, mother=None) #TODO: check
        member.add_child(child)
        
        number_of_same_children = [child for _child in member.children if _child == child]         
        assert len(number_of_same_children) == 1
    
        
    def test_set_spouse(self):
        pass
        