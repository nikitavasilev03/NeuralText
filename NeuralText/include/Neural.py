# -*- coding: utf-8 -*-
#pylint: disable=no-member

import numpy
import scipy.special

# определение класса нейронной сети 
class neuralNetwork:
    @property
    def Name(self):
        return self.__name
    @property
    def InputNodes(self):
        return self.__inodes
    @property
    def HiddenNodes(self):
        return self.__hnodes
    @property
    def OutputNodes(self):
        return self.__onodes
    @property
    def HiddenSloys(self):
        return self.__hsloys
    @property
    def LearninGrate(self):
        return self.__lr

    # инициализировать нейронную сеть 
    def __init__(self, name, inputnodes, hiddennodes, outputnodes, hiddensloys, learningrate): 
        # задать имя сети
        self.__name = name
        # задать количество узлов во входном, скрытом и выходном слое 
        self.__inodes = inputnodes
        self.__hnodes = hiddennodes 
        self.__onodes = outputnodes
        # количество скрытых слоев
        self.__hsloys = hiddensloys
        # коэффициент обучения 
        self.__lr = learningrate
        # Инициализация весовых матриц. wih - входной слой => скрытый слой, who => скрытый слой в выходной слой
        # Диапозон значений от -0,5 до 0,5 
        self.__wih = numpy.random.normal(0.0, pow(self.__hnodes, -0.5), (self.__hnodes, self.__inodes))
        self.__who = numpy.random.normal(0.0, pow(self.__onodes, -0.5), (self.__onodes, self.__hnodes))
        # Список всех слоев
        self.__sloys = []
        self.__sloys.append(numpy.random.normal(0.0, pow(self.__hnodes, -0.5), (self.__hnodes, self.__inodes)))
        if hiddensloys > 1:
            #pylint: disable=unused-variable
            for i in range(hiddensloys):
                self.__sloys.append(numpy.random.normal(0.0, pow(self.__hnodes, -0.5), (self.__hnodes, self.__hnodes)))
            pass
        self.__sloys.append(numpy.random.normal(0.0, pow(self.__onodes, -0.5), (self.__onodes, self.__hnodes)))
        # Словарь сети
        self.dc = None
        # Количество примеров обучения
        self.examples = 0
        pass
    
    def __Activation_function(self, x):
        return scipy.special.expit(x)

    # тренировка нейронной сети 
    def Train(self, inputs_list, targets_list):
        # преобразовать список входных значений в двухмерный массив 
        targets = numpy.array(targets_list, ndmin=2).T
        # преобразовать список входных значений в двухмерный массив 
        inputs = numpy.array(inputs_list, ndmin = 2).T
        outputs = inputs
        sloys_outputs = []
        for sloy in self.__sloys:
            # рассчитать входящие сигналы
            outputs = numpy.dot(sloy, outputs)
            # рассчитать исходящие сигналы
            outputs = self.__Activation_function(outputs)
			# добавить слой ко всем слоям
            sloys_outputs.append(outputs)
            pass    
        # ошибка = целевое значение - фактическое значение 
        errors = targets - outputs
        i = len(self.__sloys) - 1
        while (i > 0):
            # обновить весовые коэффициенты связей
            self.__sloys[i] += self.__lr * numpy.dot((errors * sloys_outputs[i] * (1.0 - sloys_outputs[i])), numpy.transpose(sloys_outputs[i - 1]))
            # обновить ошибки для следующего слоя
            errors = numpy.dot(self.__sloys[i].T, errors)
            i -= 1
            pass
		# обновить весовые коэффициенты связей последнего слоя
        self.__sloys[0] += self.__lr * numpy.dot((errors * sloys_outputs[0] * (1.0 - sloys_outputs[0])), numpy.transpose(inputs))
        # увеличиваем количество примеров обучения
        self.examples += 1
        pass

    # опрос нейронной сети 
    def Query(self, inputs_list):
        # преобразовать список входных значений в двухмерный массив 
        inputs = numpy.array(inputs_list, ndmin = 2).T
        outputs = inputs
        for sloy in self.__sloys:
            # рассчитать входящие сигналы
            outputs = numpy.dot(sloy, outputs)
            # рассчитать исходящие сигналы
            outputs = self.__Activation_function(outputs)
            pass
        # венуть результат
        return outputs
