class ScriptAnalyser:

    '''set 6 variable to store data and filename is used to show in __str__ part'''
    def __init__(self,fileName):
        self.count_statements = 0
        self.count_vocabulary = 0
        self.count_repetition = 0
        self.count_retracing = 0
        self.count_errors = 0
        self.count_pauses = 0
        self.fileName = fileName

    '''return the data as readable format'''
    def __str__(self):
        return 'Analyse Report of %s\nNumber of statements:%d\nNumber of vocabulary:%d\nNumber of repetition:%d\nNumber of retracing:%d\n'\
               'Number of errors:%d\nNumber of pauses:%d\n'%(self.fileName,self.count_statements,self.count_vocabulary,self.count_repetition,\
                                                             self.count_retracing,self.count_errors,self.count_pauses)

    '''processing script analyse'''
    def analyse_script(self, cleaned_file):

        '''
        1. count the statements number
        2. the statement end is . or ? or !
        '''
        for each in cleaned_file:
            if each == '.' or each == '?' or each == '!':
                self.count_statements += 1

        '''
        1. set a list to store the contents
        2. count the length of set, it is the number of word
        '''
        vocaList=[]
        for each in cleaned_file:
            if each.isalpha():
                vocaList.append(each.lower())

        self.count_vocabulary = len(set(vocaList))

        '''count the number of [/]'''
        for each in cleaned_file:
            if each == '[/]':
                self.count_repetition += 1

        '''count the number of [//]'''
        for each in cleaned_file:
            if each == '[//]':
                self.count_retracing += 1

        '''count the number of [* m:+ed]'''
        for each in cleaned_file:
            if each.startswith('[') or each.endswith(']'):
                if each == '[*' or each == 'm:+ed':
                    self.count_errors += 1

        '''count the number of (.)'''
        for each in cleaned_file:
            if each == '(.)':
                self.count_pauses += 1

        '''settle all data in one tuple'''
        self.dataTuple = (self.count_statements, self.count_vocabulary, self.count_repetition, self.count_retracing,
                         self.count_errors, self.count_pauses)
