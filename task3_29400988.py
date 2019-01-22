#import library and class
from task3_FileContentsPreprocessing import FileContentsPreprocessing as fcp
from task3_ScriptAnalyser import ScriptAnalyser as sa
from task3_DataVisualisation import DataVisualisation as dv
import numpy as np

'''***************SLI part***************'''

'''set a null arrary used to add data of report'''
array_SLI = np.array((0,0,0,0,0,0))

''' 
1. i is used to control the times of running and print the right file number
2. run i 10 times
'''
i = 1
while i <= 10:

    '''
    1. set the path and file name
    2. open the file
    3. store all contents in allSLIContents as string type
    '''
    openSLIFile = 'SLI/SLI-'+str(i)+'.txt'
    file = open(openSLIFile,'r')
    allSLIContents = file.read()

    '''----------use the class of fcp to process the contents----------'''
    sliFile = fcp()
    sliFile.preprocessing(allSLIContents)
    sliList = sliFile.preprocessing(allSLIContents)

    '''
    1. set the path and file name
    2. write the contents after preprocessing into a new file
    3. show the contents 
    '''
    closedSLIPath = 'SLI_cleaned/'
    fileSLIName ='cleaned_SLI-'+str(i)+'.txt'
    closedSLIFile = closedSLIPath+fileSLIName
    newSLIFile = open(closedSLIFile,'w')
    newSLIFile.write(' '.join(sliList))
    print('Your cleaned file already in '+closedSLIPath+' named as ',fileSLIName,'\n')

    '''close the origin file and new file'''
    newSLIFile.close()
    file.close()

    '''
    1. open a cleaned file
    2. use ScriptAnalyser class to process the contents
    '''
    newSLIOpenFile = open(closedSLIFile,'r')
    cleaned_file = newSLIOpenFile.read().split()
    sli = sa(fileSLIName)
    sli.analyse_script(cleaned_file)

    '''
    1. transform every analyse report data type to arrary
    2. add each file's data into a arrary
    '''
    array_1 = np.array(sli.dataTuple)
    array_SLI = array_SLI +array_1

    '''
    1. show the contents that after preprocessing
    2. show the analyse report
    3. close the cleaned file
    '''
    print(' '.join(sliList))
    print(sli) #report
    newSLIOpenFile.close()

    '''
    to next run
    '''
    i += 1

'''***************TD part***************'''

'''set a null arrary used to add data of report'''
array_TD = np.array((0,0,0,0,0,0))

''' 
1. i is used to control the times of running and print the right file number
2. run i 10 times
'''
i = 1
while i <= 10:

    '''
    1. set the path and file name
    2. open the file
    3. store all contents in allTDContents as string type
    '''
    openTDFile = 'TD/TD-'+str(i)+'.txt'
    file = open(openTDFile,'r')
    allTDContents = file.read()

    '''----------use the class of fcp to process the contents----------'''
    tdFile = fcp()
    tdFile.preprocessing(allTDContents)
    tdList = tdFile.preprocessing(allTDContents)

    '''
    1. set the path and file name
    2. write the contents after preprocessing into a new file
    3. show the contents 
    '''
    closedTDPath = 'TD_cleaned/'
    fileTDName ='cleaned_TD-'+str(i)+'.txt'
    closedTDFile = closedTDPath+fileTDName
    newTDFile = open(closedTDFile,'w')
    newTDFile.write(' '.join(tdList))
    print('Your cleaned file already in '+closedTDPath+' named as ',fileTDName,'\n')

    '''close the origin file and new file'''
    newTDFile.close()
    file.close()

    '''
    1. open a cleaned file
    2. use ScriptAnalyser class to process the contents
    '''
    newTDOpenFile = open(closedTDFile,'r')
    cleaned_file = newTDOpenFile.read().split()
    td = sa(fileTDName)
    td.analyse_script(cleaned_file) #run

    '''
    1. transform every analyse report data type to arrary
    2. add each file's data into a arrary
    '''
    array_1 = np.array(td.dataTuple)
    array_TD = array_TD + array_1

    '''
    1. show the contents that after preprocessing
    2. show the analyse report
    3. close the cleaned file
    '''
    print(' '.join(tdList))
    print(td) #report
    newTDOpenFile.close()

    '''
    to next run
    '''
    i += 1


'''**********Visualisation part***********'''

'''
1. use the dv class
2. compute average
3. output a picture
'''
dv = dv(tuple(array_SLI),tuple(array_TD))
dv.compute_average()
dv.visualise_statistics()