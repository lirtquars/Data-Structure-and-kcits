
from typing import Any, Iterable
class DeleteItem:
    """
    删除列表中指定的元素
    """
    def __init__(self,iterable:Iterable[Any]):
        self.iterable = list(iterable)
    
    def delete(self,index_to_delete:int) -> list[Any]:
        length_of_iterable:int = len(self.iterable)
        
        for i in range(index_to_delete,length_of_iterable,1):
            self.iterable[i] = self.iterable[i+1]
        
        self.iterable[length_of_iterable] = ""

        return self.iterable