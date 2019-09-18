import numpy as np
import pandas as pd
import sys
import os
sys.path.append('../')
sys.path.append('./data')
print(os.getcwd())

col_names = ['episode', 'trial_id', 'stimCat', 'stimId', 'stimImage', 'imagePath', 'bkSwProb', 'itSwProb', 'trialType', 'task', 'color', 'colorPath', 'response', 'sbjResp', 'sbjCorr', 'sbjRT']

def practice(SbjId):
    
    print('subjectID: ' + str(SbjId))
    order_all = [['Low', 'Med', 'High'], ['High', 'Med', 'Low']]
    SRmapping_all = [['v','n', 'v', 'n'], ['v', 'n', 'n', 'v'], ['n', 'v', 'v', 'n'], ['n', 'v', 'n', 'v']] # which key to press for [large small living nonliving]
    incompCat_all = [['LivSm', 'NLvLg'], ['LivLg', 'NLvSm'], ['LivLg', 'NLvSm'], ['LivSm', 'NLvLg']] # based on SR mapping, what are the categories that are resp incompatible in the two tasks
    
    LivLg = np.random.permutation(np.arange(1, 11))
    LivSm = np.random.permutation(np.arange(11, 21))
    NLvLg = np.random.permutation(np.arange(21, 31))
    NLvSm = np.random.permutation(np.arange(31, 41))
    LivLg_img = np.random.permutation(['LL__5', 'LL__7', 'LL__9', 'LL__10', 'LL__23', 'LL__24', 'LL__29', 'LL__37', 'LL__38', 'LL__53'])
    LivSm_img = np.random.permutation(['LS__34', 'LS__35', 'LS__36', 'LS__37', 'LS__39', 'LS__40', 'LS__41', 'LS__43', 'LS__44', 'LS__45'])
    NLvLg_img = np.random.permutation(['NL__2', 'NL__10', 'NL__12', 'NL__17', 'NL__20', 'NL__36', 'NL__51', 'NL__52', 'NL__55', 'NL__57'])
    NLvSm_img = np.random.permutation(['NS__1', 'NS__4', 'NS__25', 'NS__33', 'NS__36', 'NS__43', 'NS__45', 'NS__46', 'NS__50', 'NS__55'])
    
    SRmapping = SRmapping_all[np.remainder(SbjId, 4)]
#    order = order_all[np.remainder(round(np.random.rand()*10), 2)]
    incompCat = incompCat_all[np.remainder(SbjId, 4)]
    
    trPerStim = 48 # trial per stimulus
    E_all = pd.DataFrame(columns=col_names)
    
    for bk in range(1,2):
        itSwProb = [25, 50, 75]
        bkSwProb = int(np.mean(itSwProb))
        NumItemPerCat = len(itSwProb) #3
        
        stimSet = []
        stimCat = []
        stimSwProb=[]
        stimImage = []
        
        for i in range(len(incompCat)):       
            if incompCat[i] == 'LivLg':
                stimSet.extend(LivLg[0:NumItemPerCat])
                stimImage.extend(LivLg_img[0:NumItemPerCat])
                LivLg = LivLg[3:]
                LivLg_img = LivLg_img[3:]
            elif incompCat[i] == 'LivSm':
                stimSet.extend(LivSm[0:NumItemPerCat])
                stimImage.extend(LivSm_img[0:NumItemPerCat])
                LivSm = LivSm[3:]
                LivSm_img = LivSm_img[3:]
            elif incompCat[i] == 'NLvLg':
                stimSet.extend(NLvLg[0:NumItemPerCat])
                stimImage.extend(NLvLg_img[0:NumItemPerCat])
                NLvLg = NLvLg[3:]
                NLvLg_img = NLvLg_img[3:]
            elif incompCat[i] =='NLvSm':
                stimSet.extend(NLvSm[0:NumItemPerCat])
                stimImage.extend(NLvSm_img[0:NumItemPerCat])
                NLvSm = NLvSm[3:]
                NLvSm_img = NLvSm_img[3:]
            stimCat.extend([incompCat[i]]*NumItemPerCat)
            stimSwProb.extend(itSwProb)

        E = pd.DataFrame(columns=col_names)
    
        for i in range(len(stimSet)):
            NumSw = int(trPerStim*stimSwProb[i]/100)         
            NumRp = int(trPerStim - NumSw)
            condE = pd.DataFrame(columns=col_names)
            condE.at[:, 'stimId'] = [stimSet[i]]*trPerStim
            condE.at[:, 'stimImage'] = [stimImage[i]]*trPerStim
            condE.at[:, 'imagePath'] = './image/' + stimImage[i] + '.jpg'
            condE.at[:, 'stimCat'] = stimCat[i]
            condE.at[:, 'itSwProb'] = stimSwProb[i]
            condE.at[:, 'bkSwProb'] = bkSwProb      
            condE.at[:, 'trialType'] = ['switch']*NumSw+['repeat']*NumRp
            E = pd.concat([E,condE], ignore_index=True, sort=False) ##HYUN## unfort the list

        E.at[:, 'episode'] = 'Med'
    
        while 1:
            seq = np.random.permutation(len(E))
            E = E.loc[seq, :].reset_index(drop=True)
            currentTask = np.remainder(round(np.random.rand()*100), 2)+1
   
            for i in range(len(E)):
                if E.at[i, 'trialType'] == 'repeat':
                    E.at[i, 'task'] = currentTask
                    E.at[i, 'color'] = currentTask
                    E.at[i, 'colorPath'] = currentTask
                else:
                    currentTask = 3-currentTask
                    E.at[i, 'task'] = currentTask
                    E.at[i, 'color'] = currentTask
                    E.at[i, 'colorPath'] = currentTask
   
            cnt = []
            expVal = len(E)/len(stimSet)/2
            for s in stimSet:
                selection = E.loc[ (E['stimId'] == s) & (E['task'] == 1) ]
                cnt.append(len(selection))
   
            stimCheck = np.diff(E['stimId'])
            if (sum(x <= 1 for x in abs(np.subtract(cnt, expVal))) == len(stimSet)) & ((stimCheck == 0).sum() / len(E) <= 0.5):
                break

        E.at[:, 'trial_id'] = np.arange(1,289)
        E_all = pd.concat([E_all,E], ignore_index=True, sort=False)

    #SRmapping  = [large small living nonliving]
    E_all.at[ (E_all.task == 1) & (E_all.stimCat == 'LivLg'), 'response'] = SRmapping[0]
    E_all.at[ (E_all.task == 1) & (E_all.stimCat == 'NLvLg'), 'response'] = SRmapping[0]
    E_all.at[ (E_all.task == 1) & (E_all.stimCat == 'LivSm'), 'response'] = SRmapping[1]
    E_all.at[ (E_all.task == 1) & (E_all.stimCat == 'NLvSm'), 'response'] = SRmapping[1]
    
    E_all.at[ (E_all.task == 2) & (E_all.stimCat == 'LivLg'), 'response'] = SRmapping[2]
    E_all.at[ (E_all.task == 2) & (E_all.stimCat == 'LivSm'), 'response'] = SRmapping[2]
    E_all.at[ (E_all.task == 2) & (E_all.stimCat == 'NLvLg'), 'response'] = SRmapping[3]
    E_all.at[ (E_all.task == 2) & (E_all.stimCat == 'NLvSm'), 'response'] = SRmapping[3]
    
    
    E_all.task = E_all.task.map({1:'size', 2:'animacy'})
    E_all.color = E_all.color.map({1:'red', 2:'blue'})
    E_all.colorPath = E_all.colorPath.map({1:'./image/color/red.jpg', 2:'./image/color/blue.jpg'})
    E_all.to_csv("../data/MixedCCL_practice_" + str(SbjId) + ".csv",index=False)
    

def main(SbjId):

    print('subjectID: ' + str(SbjId))
    order_all = [['Low', 'Med', 'High'], ['High', 'Med', 'Low']]
    SRmapping_all = [['v','n', 'v', 'n'], ['v', 'n', 'n', 'v'], ['n', 'v', 'v', 'n'], ['n', 'v', 'n', 'v']] # which key to press for [large small living nonliving]
    incompCat_all = [['LivSm', 'NLvLg'], ['LivLg', 'NLvSm'], ['LivLg', 'NLvSm'], ['LivSm', 'NLvLg']] # based on SR mapping, what are the categories that are resp incompatible in the two tasks
    
    LivLg = np.random.permutation(np.arange(1, 11))
    LivSm = np.random.permutation(np.arange(11, 21))
    NLvLg = np.random.permutation(np.arange(21, 31))
    NLvSm = np.random.permutation(np.arange(31, 41))
    LivLg_img = np.random.permutation(['LL__5', 'LL__7', 'LL__9', 'LL__10', 'LL__23', 'LL__24', 'LL__29', 'LL__37', 'LL__38', 'LL__53'])
    LivSm_img = np.random.permutation(['LS__34', 'LS__35', 'LS__36', 'LS__37', 'LS__39', 'LS__40', 'LS__41', 'LS__43', 'LS__44', 'LS__45'])
    NLvLg_img = np.random.permutation(['NL__2', 'NL__10', 'NL__12', 'NL__17', 'NL__20', 'NL__36', 'NL__51', 'NL__52', 'NL__55', 'NL__57'])
    NLvSm_img = np.random.permutation(['NS__1', 'NS__4', 'NS__25', 'NS__33', 'NS__36', 'NS__43', 'NS__45', 'NS__46', 'NS__50', 'NS__55'])
    
    SRmapping = SRmapping_all[np.remainder(SbjId, 4)]
    order = order_all[np.remainder(round(np.random.rand()*10), 2)]
    incompCat = incompCat_all[np.remainder(SbjId, 4)]

    trPerStim = 48 # trial per stimulus
    E_all = pd.DataFrame(columns=col_names)
    
    for bk in range(3):
        if order[bk] == 'Low':
            itSwProb = [0, 25, 50]
        elif order[bk] == 'Med':
            itSwProb = [25, 50, 75]
        elif order[bk] == 'High':
            itSwProb = [50, 75, 100]
        bkSwProb = int(np.mean(itSwProb))
        NumItemPerCat = len(itSwProb) #3
        
        stimSet = []
        stimCat = []
        stimSwProb=[]
        stimImage = []
        
        for i in range(len(incompCat)):       
            if incompCat[i] == 'LivLg':
                stimSet.extend(LivLg[0:NumItemPerCat])
                stimImage.extend(LivLg_img[0:NumItemPerCat])
                LivLg = LivLg[3:]
                LivLg_img = LivLg_img[3:]
            elif incompCat[i] == 'LivSm':
                stimSet.extend(LivSm[0:NumItemPerCat])
                stimImage.extend(LivSm_img[0:NumItemPerCat])
                LivSm = LivSm[3:]
                LivSm_img = LivSm_img[3:]
            elif incompCat[i] == 'NLvLg':
                stimSet.extend(NLvLg[0:NumItemPerCat])
                stimImage.extend(NLvLg_img[0:NumItemPerCat])
                NLvLg = NLvLg[3:]
                NLvLg_img = NLvLg_img[3:]
            elif incompCat[i] =='NLvSm':
                stimSet.extend(NLvSm[0:NumItemPerCat])
                stimImage.extend(NLvSm_img[0:NumItemPerCat])
                NLvSm = NLvSm[3:]
                NLvSm_img = NLvSm_img[3:]
            stimCat.extend([incompCat[i]]*NumItemPerCat)
            stimSwProb.extend(itSwProb)

        E = pd.DataFrame(columns=col_names)
    
        for i in range(len(stimSet)):
            NumSw = int(trPerStim*stimSwProb[i]/100)         
            NumRp = int(trPerStim - NumSw)
            condE = pd.DataFrame(columns=col_names)
            condE.at[:, 'stimId'] = [stimSet[i]]*trPerStim
            condE.at[:, 'stimImage'] = [stimImage[i]]*trPerStim
            condE.at[:, 'imagePath'] = './image/' + stimImage[i] + '.jpg'
            condE.at[:, 'stimCat'] = stimCat[i]
            condE.at[:, 'itSwProb'] = stimSwProb[i]
            condE.at[:, 'bkSwProb'] = bkSwProb      
            condE.at[:, 'trialType'] = ['switch']*NumSw+['repeat']*NumRp
            E = pd.concat([E,condE], ignore_index=True, sort=False) ##HYUN## unfort the list

        E.at[:, 'episode'] = order[bk]
    
        while 1:
            seq = np.random.permutation(len(E))
            E = E.loc[seq, :].reset_index(drop=True)
            currentTask = np.remainder(round(np.random.rand()*100), 2)+1
   
            for i in range(len(E)):
                if E.at[i, 'trialType'] == 'repeat':
                    E.at[i, 'task'] = currentTask
                    E.at[i, 'color'] = currentTask
                    E.at[i, 'colorPath'] = currentTask
                else:
                    currentTask = 3-currentTask
                    E.at[i, 'task'] = currentTask
                    E.at[i, 'color'] = currentTask
                    E.at[i, 'colorPath'] = currentTask
                    
            cnt = []
            expVal = len(E)/len(stimSet)/2
            for s in stimSet:
                selection = E.loc[ (E['stimId'] == s) & (E['task'] == 1) ]
                cnt.append(len(selection))
   
            stimCheck = np.diff(E['stimId'])
            if (sum(x <= 1 for x in abs(np.subtract(cnt, expVal))) == len(stimSet)) & ((stimCheck == 0).sum() / len(E) <= 0.5):
                break

        E.at[:, 'trial_id'] = np.arange(1,289)
        E_all = pd.concat([E_all,E], ignore_index=True, sort=False)

    #SRmapping  = [large small living nonliving]
    # task == size
    E_all.at[ (E_all.task == 1) & (E_all.stimCat == 'LivLg'), 'response'] = SRmapping[0]    # large
    E_all.at[ (E_all.task == 1) & (E_all.stimCat == 'NLvLg'), 'response'] = SRmapping[0]    # large
    E_all.at[ (E_all.task == 1) & (E_all.stimCat == 'LivSm'), 'response'] = SRmapping[1]    # small
    E_all.at[ (E_all.task == 1) & (E_all.stimCat == 'NLvSm'), 'response'] = SRmapping[1]    # small
    # task == animacy
    E_all.at[ (E_all.task == 2) & (E_all.stimCat == 'LivLg'), 'response'] = SRmapping[2]    # living
    E_all.at[ (E_all.task == 2) & (E_all.stimCat == 'LivSm'), 'response'] = SRmapping[2]    # living
    E_all.at[ (E_all.task == 2) & (E_all.stimCat == 'NLvLg'), 'response'] = SRmapping[3]    # nonliving
    E_all.at[ (E_all.task == 2) & (E_all.stimCat == 'NLvSm'), 'response'] = SRmapping[3]    # nonliving
    
    

    E_all.task = E_all.task.map({1:'size', 2:'animacy'})
    E_all.color = E_all.color.map({1:'red', 2:'blue'})
    E_all.colorPath = E_all.colorPath.map({1:'./image/color/red.jpg', 2:'./image/color/blue.jpg'})
    E_all.to_csv("../data/MixedCCL_" + str(SbjId) + ".csv",index=False)
    

if __name__ == '__main__':
    for i in range(1,4): # range(startIndex, endIndex) --> change the indices
#        practice(i)
        main(i)
