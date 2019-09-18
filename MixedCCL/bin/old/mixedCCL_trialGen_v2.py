import numpy as np
import pandas as pd

#function trialSeq = trialGen(SbjId)
def gen(SbjId):

###### Could you use meaningful words..  I was using Matlab.. that's why I didn't use words
###### e.g. order_all = [['Low', 'Medium', 'High'], ['High', 'Medium', 'Low']]
###### do that wherever possible
##Hyun## I kept SRmapping & incompCat as it is because numbers seem to represent the variables easier

    order_all = [['Low', 'Med', 'High'], ['Low', 'Med', 'Hig']]
    SRmapping_all = [[1, 2, 1, 2], [1, 2, 2, 1], [2, 1, 1, 2], [2, 1, 2, 1]] # which key to press for [large small living nonliving]
    incompCat_all = [[2, 3], [1, 4], [1, 4], [2, 3]] # based on SR mapping, what are the categories that are resp incompatible in the two tasks

    LivLg = np.random.permutation(np.arange(1, 11))
    LivSm = np.random.permutation(np.arange(11, 21))
    NLvLg = np.random.permutation(np.arange(21, 31))
    NLvSm = np.random.permutation(np.arange(31, 41))

    SbjId = 13 # comment out later
    SRmapping = SRmapping_all[np.remainder(SbjId, 4)]
    order = order_all[np.remainder(round(np.random.rand()*10), 2)]
    incompCat = incompCat_all[np.remainder(SbjId, 4)]

    switch = 1
    repeat = 0

##### define pd.DataFrame's header with meaningful words, to index that column later
##### e.g., header = ['bk_id','trial_id','stim_id','stimCat','trialType','task',.....]
##### then E (or E_all) = pd.DataFrame(np.empty([0,len(header)], dtype=int),columns=header)
##### later on, one can index that column more easily, e.g., E.loc[:,'stim_id']=...
##### However, I am not sure we should assign dtype as int here.. ?? what's the correct thing to do here??
##Hyun## FYI, DataFrame is a very flexible data managing format.
##Hyun## We do not need to assign dtype at the beginning, because the types can be modified very easily (i.e., astype())

    trPerStim = 40 # trial per stimulus
    E_all = pd.DataFrame(columns=['stimLv', 'stimSz', 'stimCat', 'stimId', 'bkSwProb', 'itSwProb', 'trialType', 'task', 'response'])

    for bk in range(3):
        if order[bk] == 'Low': #low
#####  bkSwProb is an average of the item prob, 
#####  bkSwProb = int(np.mean(ItSwProbList))
##Hyun## bkSwProb has relocated outside if-statement for the convenience
            itSwProb = [20, 20, 50]  ##### I cut this in half because it's the same 3 prob in each stimCat
                                     ##Hyun## there is a reason why you had a duplicate.
                                     ##Hyun## in one example of stimCat, stimCat = [1, 1, 1, 4, 4, 4]
                                     ##Hyun## And you wanted to allocated each probability to each category.
                                     ##Hyun## I have modified the code to suit the truncation of the list.
        elif order[bk] == 'Med':
            itSwProb = [20, 50, 80]
        elif order[bk] == 'High':
            itSwProb = [80, 80, 50]
        bkSwProb = int(np.mean(itSwProb))
        NumItemPerCat = len(itSwProb) ##Hyun## Why? isn't the length of ItSwProbList always 3?
        stimSet = []
        stimCat = []
#        itSwProb = []  ##Hyun## stimProb is redundant of ItSwProbList, so I modified all occurrences of ItSwProbList with stimProb
                       ##Hyun## I changed 'stimProb' to 'itSwProb' for an easier understanding

##### Is there a python-equivalent of splice method (in Javascript array) 
##### https://www.w3schools.com/jsref/jsref_splice.asp
##### so that one doesn't have to do 'LivLg[0:3]   &   LivLg = LivLg[3:] kind of thing'
##Hyun## In python, there is no function that is equivalent to splice method in JS
	
        for i in range(len(incompCat)):
            if incompCat[i] == 1:				
                stimSet.extend(LivLg[0:NumItemPerCat]) ######### 
                LivLg = LivLg[3:] 
                stimCat.extend([1]*NumItemPerCat)  #########
            elif incompCat[i] == 2:
                stimSet.extend(LivSm[0:NumItemPerCat])
                LivSm = LivSm[3:]
                stimCat.extend([2]*NumItemPerCat)
            elif incompCat[i] == 3:
                stimSet.extend(NLvLg[0:NumItemPerCat])
                NLvLg = NLvLg[3:]
                stimCat.extend([3]*NumItemPerCat)
            elif incompCat[i] == 4:
                stimSet.extend(NLvSm[0:NumItemPerCat])
                NLvSm = NLvSm[3:]
                stimCat.extend([4]*NumItemPerCat)

        E = pd.DataFrame(columns=['stimLv', 'stimSz', 'stimCat', 'stimId', 'bkSwProb', 'itSwProb', 'trialType', 'task', 'response'])

        for i in range(len(stimSet)):
            NumSw = int(trPerStim*itSwProb[i//2]/100) ##Hyun## This causes an error becuse itSwProb has a length of 3, but stimSet's length is 6
            NumRp = int(trPerStim - NumSw)
            condE = pd.DataFrame(columns=['stimLv', 'stimSz', 'stimCat', 'stimId', 'bkSwProb', 'itSwProb', 'trialType', 'task', 'response'])
            condE.loc[:, 'stimId'] = [stimSet[i]]*trPerStim
            condE.loc[:, 'stimCat'] = stimCat[i]
            condE.loc[:, 'trialType'] = [switch]*NumSw+[repeat]*NumRp
            condE.loc[:, 'itSwProb'] = [itSwProb[i//2]]*trPerStim
            condE.loc[:, 'bkSwProb'] = bkSwProb
            E = pd.concat([E,condE], ignore_index=True)
            E.to_csv("./check" + str(SbjId) + ".csv",index=False)

        while 1:
            seq = np.random.permutation(len(E))
            E = E.loc[seq, :].reset_index(drop=True)
            currentTask = np.remainder(round(np.random.rand()*100), 2)+1

            for i in range(len(E)):
                if E.loc[i, 'trialType'] == 0:
                    E.loc[i, 'task'] = currentTask
                else:
                    currentTask = 3-currentTask
                    E.loc[i, 'task'] = currentTask

            cnt = []
            expVal = len(E)/len(stimSet)/2
            for s in stimSet:
                selection = E.loc[ (E['stimId'] == s) & (E['task'] == 1) ]
                cnt.append(len(selection))

            stimCheck = np.diff(E['stimId'])
            if (sum(x <= 1 for x in abs(np.subtract(cnt, expVal))) == len(stimSet)) & ((stimCheck == 0).sum() / len(E) <= 0.15):
                break
            
        E_all = pd.concat([E_all,E], ignore_index=True)
		
    print(E_all)

##### I think if we already have a category id (LivLg, etc..) these are redundant...
##### what do you think?
##Hyun## From the previous lines,
##Hyun## if 'stimCat' == 1, LivLg
##Hyun## if 'stimCat' == 2, LivSm
##Hyun## if 'stimCat' == 3, NLvLg
##Hyun## if 'stimCat' == 4, NLvSm
##Hyun## In such case, we don't need both 'stimLv' and 'stimSz' column
##Hyun## I commented the following codes for now
    E_all.loc[ E_all['stimCat'] <= 2, 'stimLv' ] = 1 # living
    E_all.loc[ E_all['stimCat'] >= 3, 'stimLv' ] = 0
    E_all.loc[ (E_all['stimCat'] == 1) | (E_all['stimCat'] == 3), 'stimSz' ] = 1  #large
    E_all.loc[ (E_all['stimCat'] == 2) | (E_all['stimCat'] == 4), 'stimSz' ] = 0  #small

##### Is there a smarter way to do this.. "dictionary" style in python
##Hyun## Since the mapping needs to meet 2 conditions from 2 columns(task & stimSz), there seems to be no smarter way to do this
##Hyun## However, I've modified to make it look simple than before
#    for i in range(len(E_all)):
#        if E_all.loc[i, 'task'] == 1: # size task
#            if E_all.loc[i, 'stimSz'] == 1:
#                E_all.loc[i, 'response'] = SRmapping[0]
#            else:
#                E_all.loc[i, 'response'] = SRmapping[1]    
#        else: # living nonlivint task
#            if E_all.loc[i, 'stimSz'] == 1:
#                E_all.loc[i, 'response'] = SRmapping[2]
#            else:
#                E_all.loc[i, 'response'] = SRmapping[3]
    E_all.loc[ (E_all.task == 1) & (E_all.stimSz == 1), 'response'] = SRmapping[0]
    E_all.loc[ (E_all.task == 1) & (E_all.stimSz == 0), 'response'] = SRmapping[1]
    E_all.loc[ (E_all.task == 2) & (E_all.stimSz == 1), 'response'] = SRmapping[2]
    E_all.loc[ (E_all.task == 2) & (E_all.stimSz == 0), 'response'] = SRmapping[3]

    
    E_all.task = E_all.task.map({1:'size', 2:'animacy'})

    # E_all.rename(columns={1:'stimLv',
    #                       2:'stimSz',
    #                       3:'stimCat',
    #                       4:'stimId',
    #                       5:'bkSwProb',
    #                       6:'itSwProb',
    #                       7:'trialType',
    #                       8:'task',
    #                       9:'response'}, inplace=True)
#    E_all.astype(int)
    E_all.to_csv("./MixedCCL_trial_sequence_" + str(SbjId) + ".csv",index=False)


if __name__ == '__main__':
    SbjId = int(input("Subject ID: "))
    gen(SbjId)
