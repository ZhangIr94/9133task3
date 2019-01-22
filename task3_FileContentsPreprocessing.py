class FileContentsPreprocessing:

    '''set allCotent as the process data '''
    def preprocessing(self,allContent):

        '''set list for storing data of each step'''
        tempList = []
        aList = []
        bList = []
        cList = []
        dList = []
        self.allContent = allContent
        allList = list(self.allContent.split())

        '''
        1. Take out each statement start with *CHI: 
        2. store in tempList
        '''
        for i in range(len(allList)):
            if allList[i] == '*CHI:':
                i += 1
                while not (allList[i] == '.' or allList[i] == '?' or allList[i] == '!'):
                    tempList.append(allList[i])
                    i += 1
                tempList.append(allList[i])
                tempList.append('\n')

        '''
        1. delete the [] except [/][//][* m:+ed]
        2. store in aList
        '''
        for i in range(len(tempList)):
            if tempList[i].startswith('[') or tempList[i].endswith(']'):
                if tempList[i] == '[//]' or tempList[i] == '[/]' or tempList[i] == '[*' or tempList[i] == 'm:+ed]':
                    aList.append(tempList[i])
                else:
                    pass
            else:
                aList.append(tempList[i])

        '''
        1. delete the <> in around of word
        2. store in bList
        '''
        for i in range(len(aList)):
            if aList[i].startswith('<') or aList[i].endswith('>'):
                aList[i] = aList[i].strip('<')
                aList[i] = aList[i].strip('>')
                bList.append(aList[i])
            else:
                bList.append(aList[i])

        '''
        1. remove word with & or +
        2. store in cList
        '''
        for i in range(len(bList)):
            if bList[i].startswith('&') or bList[i].startswith('+'):
                pass
            else:
                cList.append(bList[i])

        '''
        1. remove () in around of letter and leave (.)
        2.store in dList
        '''
        for i in range(len(cList)):
            if (cList[i].startswith('(') or cList[i].endswith(')')) and (cList[i] != '(.)'):
                cList[i] = cList[i].replace('(', '')
                cList[i] = cList[i].replace(')', '')
                dList.append(cList[i])
            else:
                dList.append(cList[i])

        self.dList = dList
        return (dList)