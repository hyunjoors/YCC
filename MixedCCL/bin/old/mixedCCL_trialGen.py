import numpy as np
import pandas as pd

#function trialSeq = trialGen(SbjId)
def gen(SbjId):
    order_all = [[1, 2, 3], [3, 2, 1]]
    SRmapping_all = [[1, 2, 1, 2], [1, 2, 2, 1], [2, 1, 1, 2], [2, 1, 2, 1]] # which key to press for [large small living nonliving]
    incompCat_all = [[2, 3], [1, 4], [1, 4], [2, 3]] # based on SR mapping, what are the categories that are resp incompatible in the two tasks

    #LivLg = Shuffle([1:10]) # cat = 1
    LivLg = np.random.permutation(np.arange(1, 11))
    #LivSm = Shuffle([11:20]); # cat = 2
    LivSm = np.random.permutation(np.arange(11, 21))
    #NLvLg = Shuffle([21:30]); # cat = 3
    NLvLg = np.random.permutation(np.arange(21, 31))
    #NLvSm = Shuffle([31:40]); # cat = 4
    NLvSm = np.random.permutation(np.arange(31, 41))

    #SbjId = 13 # comment out later
    SRmapping = SRmapping_all[np.remainder(SbjId, 4)]
    order = order_all[np.remainder(round(np.random.rand()*10), 2)]
    incompCat = incompCat_all[np.remainder(SbjId, 4)]

    idx_stimLv = 1 # living/nonliving
    idx_stimSz = 2 # size
    idx_stimCat = 3
    idx_stimId = 4 # unique id for each stimulus/object(e.g., apple, banana)
    idx_bkSwProb = 5
    idx_itSwProb = 6
    idx_trialType = 7 # switch(1) vs. repeat(0)
    idx_task = 8
    idx_response = 9

    trPerStim = 40

    E_all = pd.DataFrame()
    for bk in range(3):
        if order[bk] == 1: #low
            BkSwProb = 30
            ItSwProbList = [20, 20, 50, 20, 20, 50]
        elif order[bk] == 2:
            BkSwProb = 50
            ItSwProbList = [20, 50, 80, 20, 50, 80]
        elif order[bk] == 3:
            BkSwProb = 70
            ItSwProbList = [80, 80, 50, 80, 80, 50]

        stimSet = []
        stimCat = []
        for i in range(len(incompCat)):
            if incompCat[i] == 1:
                stimSet.extend(LivLg[0:3])
                LivLg = LivLg[3:]
                stimCat.extend([1, 1, 1])
            elif incompCat[i] == 2:
                stimSet.extend(LivSm[0:3])
                LivSm = LivSm[3:]
                stimCat.extend([2, 2, 2])
            elif incompCat[i] == 3:
                stimSet.extend(NLvLg[0:3])
                NLvLg = NLvLg[4:]
                stimCat.extend([3, 3, 3])
            elif incompCat[i] == 4:
                stimSet.extend(NLvSm[0:3])
                NLvSm = NLvSm[4:]
                stimCat.extend([4, 4, 4])

        E = pd.DataFrame()
        for i in range(len(stimSet)):
            NrSw = int(trPerStim*ItSwProbList[i]/100)
            NrRp = int(trPerStim - NrSw)
            condE = pd.DataFrame()
            condE.loc[:, idx_stimId] = np.transpose(np.ones((trPerStim, 1))*stimSet[i]).reshape(-1)
            condE.loc[:, idx_stimCat] = stimCat[i]
            condE.loc[:, idx_trialType] = np.concatenate((np.ones((NrSw, 1)), np.zeros((NrRp, 1))))
            condE.loc[:, idx_itSwProb] = ItSwProbList[i]
            condE.loc[:, idx_bkSwProb] = BkSwProb
            E = pd.concat([E,condE], ignore_index=True)

        while 1:
            seq = np.random.permutation(len(E))
            E = E.loc[seq, :].reset_index(drop=True)
            currentTask = np.remainder(round(np.random.rand()*100), 2)+1

            for i in range(len(E)):
                if E.loc[i, idx_trialType] == 0:
                    E.loc[i, idx_task] = currentTask
                else:
                    currentTask = 3-currentTask
                    E.loc[i, idx_task] = currentTask

            cnt = []
            expVal = len(E)/len(stimSet)/2
            for s in stimSet:
                selection = E.loc[ (E[idx_stimId] == s) & (E[idx_task] == 1) ]
                cnt.append(len(selection))

            stimCheck = np.diff(E[idx_stimId])
            if (sum(x <= 1 for x in abs(np.subtract(cnt, expVal))) == len(stimSet)) & ((stimCheck == 0).sum() / len(E) <= 0.15):
                break
            
        E_all = pd.concat([E_all,E], ignore_index=True)

    E_all.loc[ E_all[idx_stimCat] <= 2, idx_stimLv ] = 1 # living
    E_all.loc[ E_all[idx_stimCat] >= 3, idx_stimLv ] = 0
    E_all.loc[ (E_all[idx_stimCat] == 1) | (E_all[idx_stimCat] == 3), idx_stimSz ] = 1  #large
    E_all.loc[ (E_all[idx_stimCat] == 2) | (E_all[idx_stimCat] == 4), idx_stimSz ] = 0  #small

    for i in range(len(E_all)):
        if E_all.loc[i,idx_task] == 1: # size task  
            if E_all.loc[i,idx_stimSz] == 1:
                E_all.loc[i,idx_response] = SRmapping[0]  # [large small living nonliving]
            else:
                E_all.loc[i,idx_response] = SRmapping[1]     
        else: # living nonlivint task
            if E_all.loc[i,idx_stimLv] == 1:
                E_all.loc[i,idx_response] = SRmapping[2]
            else:
                E_all.loc[i,idx_response] = SRmapping[3]

    E_all.rename(columns={1:'stimLv',
                          2:'stimSz',
                          3:'stimCat',
                          4:'stimId',
                          5:'bkSwProb',
                          6:'itSwProb',
                          7:'trialType',
                          8:'task',
                          9:'response'}, inplace=True)
    E_all.astype(int)
    E_all.to_csv("./MixedCCL_trial_sequence_" + str(SbjId) + ".csv",index=False)


if __name__ == '__main__':
    SbjId = int(input("Subject ID: "))
    gen(SbjId)
