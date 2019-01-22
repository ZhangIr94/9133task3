import numpy as np
import matplotlib.pyplot as plt

class DataVisualisation:

    '''set two variable as the process data'''
    def __init__(self, sliTuple, tdTuple):

        self.sliTuple = sliTuple
        self.tdTuple = tdTuple

    '''compute the average data and transform the data type to tuple'''
    def compute_average(self):

        self.arrary_SLIAverage = (np.array(self.sliTuple)/10)
        self.arrary_TDAverage = (np.array(self.tdTuple)/10)

        self.averageSLITuple = tuple(self.arrary_SLIAverage)
        self.averageTDTuple =  tuple(self.arrary_TDAverage)

    '''build a bar chart by average data'''
    def visualise_statistics(self):

        '''set the tick list'''
        nameList = ('statements', 'vocabulary', 'repetition', 'retracing', 'errors', 'pauses')
        index = list(range(max(len(self.averageSLITuple),len(self.averageTDTuple))))
        '''set each bar width'''
        barWidth = 0.4
        '''draw the SLI group'''
        rectsSLI = plt.bar(index,self.averageSLITuple, width=barWidth, label='SLI', color='#EF8536')
        '''control the bar order'''
        for i in range(len(index)):
            index[i] = index[i] + barWidth
        '''draw the TD group'''
        rectsTD = plt.bar(index,self.averageTDTuple, width= barWidth, label = 'TD', color='#547CAF')
        '''set tick in x'''
        plt.xticks(np.array(range(max(len(self.averageSLITuple),len(self.averageTDTuple))))+ barWidth/2 , nameList)

        '''write the data on the top of bar'''
        for rect in rectsSLI:
            height = rect.get_height()
            plt.text(rect.get_x() + rect.get_width() / 2, height, height, ha='center', va='bottom', size = 8)
            rect.set_edgecolor('white')

        for rect in rectsTD:
            height = rect.get_height()
            plt.text(rect.get_x() + rect.get_width() / 2, height, height, ha='center', va='bottom', size = 8)
            rect.set_edgecolor('white')

        '''write a tips'''
        plt.legend()
        '''save image'''
        plt.savefig('result.png')
        '''show to user'''
        plt.show()

