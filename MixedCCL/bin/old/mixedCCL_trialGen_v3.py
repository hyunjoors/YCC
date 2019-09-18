import sys
import numpy as np
import pandas as pd
sys.path.insert(0, '../')

def gen(SbjId):

    col_names = ['bk_id', 'trial_id', 'stimCat', 'stimId', 'bkSwProb', 'itSwProb', 'trialType', 'task', 'response']
    order_all = [['Low', 'Med', 'High'], ['Low', 'Med', 'High']]
    SRmapping_all = [['v','n', 'v', 'n'], ['v', 'n', 'n', 'v'], ['n', 'v', 'v', 'n'], ['n', 'v', 'n', 'v']] # which key to press for [large small living nonliving]
    incompCat_all = [['LivSm', 'NLvLg'], ['LivLg', 'NLvSm'], ['LivLg', 'NLvSm'], ['LivSm', 'NLvLg']] # based on SR mapping, what are the categories that are resp incompatible in the two tasks
    
    LivLg = np.random.permutation(np.arange( 1, 11))
    LivSm = np.random.permutation(np.arange(11, 21))
    NLvLg = np.random.permutation(np.arange(21, 31))
    NLvSm = np.random.permutation(np.arange(31, 41))
    
    SRmapping = SRmapping_all[np.remainder(SbjId, 4)]
    order = order_all[np.remainder(round(np.random.rand()*10), 2)]
    incompCat = incompCat_all[np.remainder(SbjId, 4)]
    
    trPerStim = 40 # trial per stimulus
    E_all = pd.DataFrame(columns=col_names)
    
    for bk in range(3):
        if order[bk] == 'Low':
            itSwProb = [0, 20, 50]
        elif order[bk] == 'Med':
            itSwProb = [20, 50, 80]
        elif order[bk] == 'High':
            itSwProb = [50, 80, 100]
        bkSwProb = int(np.mean(itSwProb))
        NumItemPerCat = len(itSwProb)
        
        stimSet = []
        stimCat = []	
        stimSwProb=[]
        
        for i in range(len(incompCat)):       
            if incompCat[i] == 'LivLg':
                stimSet.extend(LivLg[0:NumItemPerCat])
                LivLg = LivLg[3:] 
            elif incompCat[i] == 'LivSm':
                stimSet.extend(LivSm[0:NumItemPerCat])
                LivSm = LivSm[3:]
            elif incompCat[i] == 'NLvLg':
                stimSet.extend(NLvLg[0:NumItemPerCat])
                NLvLg = NLvLg[3:]
            elif incompCat[i] =='NLvSm':
                stimSet.extend(NLvSm[0:NumItemPerCat])
                NLvSm = NLvSm[3:]
            stimCat.extend([incompCat[i]]*NumItemPerCat)
            stimSwProb.extend(itSwProb)
                
        E = pd.DataFrame(columns=col_names)

        for i in range(len(stimSet)):
            NumSw = int(trPerStim*stimSwProb[i]/100)         
            NumRp = int(trPerStim - NumSw)
            condE = pd.DataFrame(columns=['bk_id', 'trial_id', 'stimCat', 'stimId', 'bkSwProb', 'itSwProb', 'trialType', 'task', 'response'])
            condE.loc[:, 'stimId'] = [stimSet[i]]*trPerStim
            condE.loc[:, 'stimCat'] = stimCat[i]
            condE.loc[:, 'itSwProb'] = stimSwProb[i]
            condE.loc[:, 'bkSwProb'] = bkSwProb      
            condE.loc[:, 'trialType'] = ['switch']*NumSw+['repeat']*NumRp
            E = pd.concat([E,condE], ignore_index=True)
    
        while 1:
            seq = np.random.permutation(len(E))
            E = E.loc[seq, :].reset_index(drop=True)
            currentTask = np.remainder(round(np.random.rand()*100), 2)+1
    
            E.loc[E.trialType == 1, 'task'] = currentTask
            E.loc[E.trialType != 1, 'task'] = 3-currentTask
    
            cnt = []
            expVal = len(E)/len(stimSet)/2
            for s in stimSet:
                selection = E.loc[ (E['stimId'] == s) & (E['task'] == 1) ]
                cnt.append(len(selection))
    
            stimCheck = np.diff(E['stimId'])
            if (sum(x <= 1 for x in abs(np.subtract(cnt, expVal))) == len(stimSet)) & ((stimCheck == 0).sum() / len(E) <= 0.5):
                break
            
        E_all = pd.concat([E_all,E], ignore_index=True)
    
    #SRmapping  = [large small living nonliving]
    E_all.loc[ (E_all.task == 1) & (E_all.stimCat == 'LivLg'), 'response'] = SRmapping[0]
    E_all.loc[ (E_all.task == 1) & (E_all.stimCat == 'NLvLg'), 'response'] = SRmapping[0]
    E_all.loc[ (E_all.task == 1) & (E_all.stimCat == 'LivSm'), 'response'] = SRmapping[1]
    E_all.loc[ (E_all.task == 1) & (E_all.stimCat == 'NLvSm'), 'response'] = SRmapping[1]
    
    E_all.loc[ (E_all.task == 2) & (E_all.stimCat == 'LivLg'), 'response'] = SRmapping[2]
    E_all.loc[ (E_all.task == 2) & (E_all.stimCat == 'LivSm'), 'response'] = SRmapping[2]
    E_all.loc[ (E_all.task == 2) & (E_all.stimCat == 'NLvLg'), 'response'] = SRmapping[3]
    E_all.loc[ (E_all.task == 2) & (E_all.stimCat == 'NLvSm'), 'response'] = SRmapping[3]
    
    E_all.task = E_all.task.map({1:'size', 2:'animacy'})
    E_all.to_csv("../data/mixedCCL_trial_sequence_" + str(SbjId) + ".csv",index=False)
    

if __name__ == '__main__':
    SbjId = int(input("Subject ID: "))
    gen(SbjId)
