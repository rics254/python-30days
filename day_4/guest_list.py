guest = ['munene', 'wambura', 'wakariru','wanjiku']
print(f'hello there {guest[0].title()}, please accept my invitation to dinner')
print(f'hello there {guest[1].title()}, please accept my invitation to dinner')
print(f'hello there {guest[2].title()}, please accept my invitation to dinner')
print(f'hello there {guest[3].title()}, please accept my invitation to dinner')
print({guest[0].title()})
guest[0] = 'waruguru'
print(guest)

print(f'hello there {guest[0].title()}, please accept my invitation to dinner')
print(f'hello there {guest[1].title()}, please accept my invitation to dinner')
print(f'hello there {guest[2].title()}, please accept my invitation to dinner')
print(f'hello there {guest[3].title()}, please accept my invitation to dinner')

print(f'Hello there guys i just found a bigger table for the dinner set')
guest.insert(0, 'kamau')
print(guest)
guest.insert(3, 'daudi')
print(guest)

guest.append('wangechi')
print(guest)

print(f'hello there {guest[0].title()}, please accept my invitation to dinner')
print(f'hello there {guest[1].title()}, please accept my invitation to dinner')
print(f'hello there {guest[2].title()}, please accept my invitation to dinner')
print(f'hello there {guest[3].title()}, please accept my invitation to dinner')
print(f'hello there {guest[4].title()}, please accept my invitation to dinner')
print(f'hello there {guest[5].title()}, please accept my invitation to dinner')
print(f'hello there {guest[6].title()}, please accept my invitation to dinner')

#shrinking the guest list
print('hello there good people , Im sorry but I can only invite two people')
      

popped_person = guest.pop(0)
print(f'hello there {popped_person.title()}, the invite is not there for you')

popped_person = guest.pop(0)
print(f'hello there {popped_person.title()}, the invite is not there for you')

popped_person = guest.pop(0)
print(f'hello there {popped_person.title()}, the invite is not there for you')

popped_person = guest.pop(0)
print(f'hello there {popped_person.title()}, the invite is not there for you')

popped_person = guest.pop(0)
print(f'hello there {popped_person.title()}, the invite is not there for you')
print(guest)

print(f'hello there {guest[0].title()}, please accept my invitation to dinner')
print(f'hello there {guest[1].title()}, please accept my invitation to dinner')

del guest[0]
del guest[0]

print(guest)