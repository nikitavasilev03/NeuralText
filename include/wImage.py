import numpy
import random

class DataImage():
    def __init__(self, name, image):
        self.name = name #тип - string, имя буквы
        self.image = image #тип - image, изображение буквы
        pass

class ListDataImage():
    def __init__(self):
        self.list = []
        pass

    def Add(self, dImage):
        self.list.append(dImage)
        pass
    
    def Delete(self, dImage):
        self.list.remove(dImage)
        pass
    
    def GetCharCount(self, char):
        count = 0
        for i in self.list:
            if i.name == char:
                count += 1
        return count
    
    def GetCharWithCount(self):
        ls = []
        for i in self.list:
            if (ls.count(i.name) == 0):
                ls.append(i.name)
        ls.sort()
        res = []
        for i in ls:
            res.append([i, self.GetCharCount(i)])
        return res

    def GetChatPos(self, char):
        ls = []
        for i in self.list:
            if (ls.count(i.name) == 0):
                ls.append(i.name)
        ls.sort()
        for i in range(0, len(ls)):
            if char == ls[i]:
                return i
        pass
    
    def GetAllChar(self):
        ls = []
        for i in self.list:
            if (ls.count(i.name) == 0):
                ls.append(i.name)
        ls.sort()
        return ls
    
    def Mix(self):
        for i in range(len(self.list) * 2):
            i = random.randint(0, len(self.list) - 1)
            j = random.randint(0, len(self.list) - 1)
            temp = self.list[i]
            self.list[i] = self.list[j]
            self.list[j] = temp 
        pass

def ImageToArray(image):
    n_arr = numpy.array(image) #Преобразовываем изображение в двухмерный массив
    N = len(n_arr) #Количество строк
    M = len(n_arr[0]) #Количество столбцов
    res_arr = numpy.empty(N * M) #Новый пустой одномерный массив N*M
    x = 0
    for i in range(N):
        for j in range(M):
			#Преобразовываем двухмерный массив в одномерный с конвертацией цветов из RGB в одноканальный цвет
            res_arr[i * N + j] = (x + (255 - n_arr[i, j, 0]) + (255 - n_arr[i, j, 1]) + (255 - n_arr[i, j, 2])) / 3 
    return res_arr #Возвращаем получившийся массив