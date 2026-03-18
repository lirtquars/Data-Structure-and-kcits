from collections.abc import Sequence
from typing import Any
class set:
    def __init__(self,iterable:Sequence[Any]):
        self.iterable = iterable

    def delete(self,index_to_delete:int) -> list[Any]:
        length_of_iterable:int = len(self.iterable)
        
        for i in range(index_to_delete,length_of_iterable,1):
            self.iterable[i] = self.iterable[i+1]
        
        self.iterable[length_of_iterable] = ""

        return self.iterable
    
    def insert(self,element: Any,index_to_insert:int) -> list[Any]:
        length_of_iterable:int = len(self.iterable)
        self.iterable.append("")
        for i in range(length_of_iterable,index_to_insert,-1):
            self.iterable[i] = self.iterable[i-1]
        
        self.iterable[length_of_iterable] = element

        return self.iterable
    
    def search(self,element: Any,index_to_search:int) -> int:
        length_of_iterable:int = len(self.iterable)
        for i in range(0,length_of_iterable,1):
            if(self.iterable[i] == element):
                return index_to_search
        return -1