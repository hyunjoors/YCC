import numpy as np
import pandas as pd
import random

# two swProb for each 2x2 category =8 uniqu stim

#idx.stimLv = 1 # living/nonliving
#idx.stimSz = 2 # size 
#idx.stimCat =3
#idx.stimId = 4 # unique id for each stimulus/object (e.g., apple, banana)
#idx.swProb = 5 
#idx.task    = 6
#idx.trialType=7  # switch vs. repeat

col_names = ['stimLv', 'stimSz', 'stimCat', 'stimId', 'swProb', 'task', 'trialType']

itemRep = 40
# stim = [1:8]
conM = pd.DataFrame(np.zeros((8,7), dtype=int), columns=col_names)
conM["stimLv"] = np.transpose(np.ones((4,1), dtype=int)*[1,2]).reshape(-1)
conM["stimSz"] = np.transpose(np.ones((2,1), dtype=int)*[1, 2, 1, 2]).reshape(-1)
conM["swProb"] = np.transpose(np.ones((4,1), dtype=int)*[25, 75]).reshape(-1)
conM["stimId"] = np.arange(1,9)
conM["stimCat"]= np.transpose(np.ones((2,1), dtype=int)*[1, 2, 3, 4]).reshape(-1)

M = pd.DataFrame(columns=col_names)

for i in range(len(conM.index)):
    sw = itemRep*(conM.loc[i,"swProb"])/100
    rep  = itemRep - sw
    T = pd.DataFrame(np.ones((itemRep,1), dtype=int)*conM.loc[i,:].values, columns=col_names)
    ones = np.ones((int(sw),1), dtype=int)
    zeros = np.zeros((int(rep),1), dtype=int)
    T.loc[:,"trialType"] = np.concatenate((ones, zeros))
    M = pd.concat([M,T], ignore_index=True)

while True:
#    seq = random.randint(0, len(M.index))
#    M1 = M.loc[seq,:]
    # shuffle M
    M1 = M.sample(frac=1).reset_index(drop=True)

#    t=Shuffle([1 2]);
#    currentTask=t(1);
    currentTask = random.randint(1, 2)

#    for i=1:size(M1,1)
#        if M1(i,idx.trialType)==1
#            currentTask=3-currentTask;
#        end
#        M1(i, idx.task)=currentTask;
#    end
    for i in range(len(M1.index)):
        if M1.loc[i, "trialType"] == 1:
            currentTask = 3 - currentTask
        M1.loc[i, "task"] = currentTask

#    for stimId=1:8
#        nrT1(stimId,1) = size(find(M1(:,idx.task)==1 & M1(:,idx.stimId)==stimId),1)
#    end
    nrT1 = np.zeros((8,1))
    for stimId in range(1,9):
        nrT1[stimId-1] = len(M1.loc[(M1.task == 1) & (M1.stimId == stimId)])
        
    exp = itemRep / 2 # where does exp used?

    # if size(find(abs(nrT1-itemRep/2)<=1),1)==8
    # abs(nrT1-itemRep/2) <= 1 --> the abs value is always larger than 1
    if sum(x <= 1 for x in abs(nrT1 - itemRep/2)) == 8:
        M1.to_csv("./MixedCCL_sequence.csv",index=False)
        break
