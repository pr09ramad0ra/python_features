class Screen(TypedDict):
'''Creating the class with particular keys and thire types'''
    name: NotRequired[str]
    width: Required[int]
    height: int
    
#Creating the instances of object
Screen1 = {'name': 'A4', 'width': 210, 'height': 297} # created
Screen2 = {'width': 210, 'height': 297} # created
Screen3 = {'name': 'A4', 'height': 297} # not created - width is required
Screen4 = {'name': 'A4', 'width': 210} # not created - height is require

https://docs.python.org/3/whatsnew/3.11.html#pep-655-marking-individual-typeddict-items-as-required-or-not-required
