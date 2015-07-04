"""
Creates furniture classes to be put in rooms and stored in a list.
"""

class Furnishing:
    def __init__(self, room):
        self.room = room
        
class Sofa(Furnishing):
    def __init__(self, room):
        super().__init__(room)

class Bookshelf(Furnishing):
    def __init__(self, room):
        super().__init__(room)

class Bed(Furnishing):
    def __init__(self, room):
        super().__init__(room)

class Table(Furnishing):
    def __init__(self, room):
        super().__init__(room)

def map_the_home(lst):
    _map = {}
    rooms = set()
    for i in lst:
        rooms.add(i.room)
    for room in rooms:
        for i in lst:
            if i.room == room:
                if _map.get(room):
                    value = _map.get(room)
                    value.append(i)
                    _map.update({room:value})
                else:
                    _map.update({room:[i]})
    return _map

def counter(lst):
    bed_ct = 0
    bookshelf_ct = 0
    sofa_ct = 0
    table_ct = 0
    for i in lst:
        if isinstance(i,Bed):
            bed_ct += 1
        elif isinstance(i,Bookshelf):
            bookshelf_ct += 1
        elif isinstance(i, Sofa):
            sofa_ct += 1
        elif isinstance(i,Table):
            table_ct += 1
    result = ('Beds: {}\n'.format(bed_ct)+
            'Bookshelves: {}\n'.format(bookshelf_ct)+
            'Sofas: {}\n'.format(sofa_ct)+
            'Tables: {}'.format(table_ct))
    print(result)
