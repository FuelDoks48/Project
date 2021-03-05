import os       # Модуль для работы с операционной системой,не зависит от ОС
import tempfile # Модуль Временных файлов,позволит сделать временный хэш данных
import heapq    # Модуль по Поиску самых больших и маленьких предметов в коллекции  
import sys      # Модуль обеспечивает доступ к некоторым переменным и функциям,взаимодействующими с интерпретатором


class heapnode:
    #  Класс поиска  ( минимальный массив Здесь) Фактическое значение, подлежащее хранению в коллекции  FileHandler Файл, который хранит номер
    
    def __init__(self, item, fileHandler):
        self.item = item
        self.fileHandler = fileHandler

class externamMergeSort:
    # разбивает большой файл на маленькие файлы,сортирует маленькие файлы и использует python 
    # Модуль heap объеденяет разных мелких отсортированных файлов.Каждый сортированный файл как генератор,и не даёт загрузить всю инфформацию в файл.


# sortedTempFileHandlerList - список файлов для временных файлов что бы не перегружать память,путем разбиаения больших файлов.
    def __init__(self):
        self.sortedTempFileHandlerList = []
        self.getCurrentDir()

    def getCurrentDir(self):
        self.cwd = os.getcwd()


# Итерирует генератор сортировки
    def iterateSortedData(self, sortedCompleteData):
        for no in sortedCompleteData:
            print(no)


# Высокий уровень Python-способа всех чисел в списке файлов,на которые указывают сортировочный список
    def mergeSortedtempFiles(self):
        # mergedNo - генератор,который харанит все отсортированные числа в формате ((1,3,4), (1,2,3))
        mergedNo = (map(int, tempFileHandler) for tempFileHandler in self.sortedTempFileHandlerList)
        sortedCompleteData = heapq.merge(*mergedNo)
        # использует модуль python heapq который берет список сортированных итераторов и сортирует его и генерит отсортированный итератор.Никакого хранения данных в памяти,возвращает returnComleteData.
        return sortedCompleteData

        # Имитация массы
    def heapify(self, arr, i, n):
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[left].item < arr[i].item:
            smallest = left
        else:
            smallest = i 
        
        if right < n and arr[right].item < arr[smallest].item:
            smallest = right
        
        if i != smallest:
            (arr[i], arr[smallest]) = (arr[smallest], arr[i])
            self.heapify(arr, smallest, n)


# Конструкция коллекции 
    def construct_heap(self, arr):
        l = len(arr) - 1
        mid = l / 2
        while mid > 0:
            self.heapify(arr, mid, l)
            mid -= 1

    # Реализация низкого уровня,для объединения от отсортированного малого файла к большему файлу.Перемещение первого элемента всех файлов в одну минуту.В общей сумме самый малый элемент. 
    # Перемещает этот элемент из общей массы в файл.Получить этого элемента.Читает следующий элемент с использованием того же файлового файла.Если следующий элемент файла пуст,то помечается INT_MAX
    # Перемещает его в heap.Повторяет то же действие.Продолжать до тех пор пока все элементы heap не станут INT_MAX или пока все файлы поменьше не будут прочитаны полностью. 
    def mergeSortTempFiles_low_level(self):
        low_list = []
        sorted_output = []
        for tempFileHandler in self.sortedTempFileHandlerList:
            item = int(tempFileHandler.readline().strip())
            low_list.append(heapnode(item, tempFileHandler))


        self.construct_heap(low_list)
        while True:
            min = low_list[0]
            if min.item == sys.maxint:
                break
            
            sorted_output.append(min.item)
            fileHandler = min.fileHandler
            item = fileHandler.readline().strip()

            if not item:
                item =sys.maxint
            else:
                item = int(item)
            low_list[0] = heapnode(item, fileHandler)
            self.heapify(low_list, 0, len(low_list))

        return sorted_output


        # Функция Разбивает большие файлы на маленькие части,сортировует и хранит файлы на диске

    def splitFiles(self, largeFileName, smallFileSize):
        largeFileHandler = open(largeFileName)
        tempBuffer = []
        size = 0
        while True:
            nubmer = largeFileHandler.readline()
            if not nubmer:
                break
            tempBuffer.append(nubmer)
            size += 1
            if size % smallFileSize == 0:
                tempBuffer = sorted(tempBuffer, key=lambda no : int(no.strip()))
                tempFile = tempfile.NamedTemporaryFile(dir = self.cwd + "/temp", delete=False)
                tempFile.writelines(tempBuffer)
                tempFile.seek(0)
                self.sortedTempFileHandlerList.append(tempFile)
                tempBuffer = []


if __name__ == '__main__':
    largeFileName = 'largefile'
    smallFileSize = 10
    obj = externamMergeSort()
    obj.splitFiles(largeFileName, smallFileSize)
    print(obj.mergeSortTempFiles_low_level())

# sortedCompleteData = obj.mergeSortedtempFiles()
# obj.iterateSortedData(sortedCompleteData)