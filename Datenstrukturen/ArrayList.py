import numpy as np

class ArrayList(): 
    def __init__(self) -> None:
        self.array = np.empty(5, dtype=object)
        self.index = 0

    def add(self, value):
        if self.index >= len(self.array): 
            arr = np.empty(self.index+10, dtype=object)
            np.put(arr, range(self.index), self.array)
            self.array = arr
        self.array[self.index] = value
        self.index += 1

    def remove_at_index(self, remove_index):
        remove_index += 1
        for index, i in enumerate(self.array[remove_index:]): 
            if not i or not self.array[remove_index + index]: 
                self.array[remove_index + index -1] = None
                break
            self.array[remove_index + index-1] = self.array[remove_index + index] 
        self.index -= 1

    def __len__(self): 
        return self.index

    def __str__(self) -> str:
        s = "["
        for value in self.array:
            if not value:
                break 
            s += str(value) + ", "
        s = s[:-2] + "]"
        return s