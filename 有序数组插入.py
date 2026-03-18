from typing import Any
from collections.abc import Sequence
class the_order_list:
    def __init__(self,iterable:Sequence[Any]):
        self.iterable = iterable

    def insert(self,element: Any,index_to_insert:int) -> list[Any]:
        length_of_iterable:int = len(self.iterable)
        self.iterable.append("")
        for i in range(length_of_iterable,index_to_insert,-1):
            self.iterable[i] = self.iterable[i-1]
        self.iterable[length_of_iterable] = element
        return self.iterable

    def insert_element(element:int,iterable:list[int],index_to_insert:int):
        length_of_iterable:int = len(iterable)
        if (element <= iterable[0]):
            iterable.insert(element,0)
        elif(element >= iterable[length_of_iterable]):
            iterable.insert(element,length_of_iterable)
        else:
            left = 0
            right = length_of_iterable
            average = (left + right)/2
            if (element < iterable[average]):
                right = average
            elif (element == iterable[average] or average == right):
                iterable.insert(element,average)
            else:
                left = average

