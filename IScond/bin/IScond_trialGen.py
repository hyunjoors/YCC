import numpy as np
import pandas as pd

def gen(SbjId=0): ##Hyun## a default SbjId is 0
    # idx.bk_id     =1
    # idx.trial_id = 2
    # idx.stimCat = 3
    # idx.stimId = 4
    # idx.SRP = 5
    # idx.trialType = 6
    # idx.Rw = 7 # Rw = Reward amount
    # idx.response = 8
    col_names = ['block_id', 'trial_id', 'stimCat', 'stimId', 'SRP', 'trialType', 'Rw', 'response']

    # MH = Shuffle([1:10])
    # # stimCat = 1
    # MS = Shuffle([1:10])
    # # stimCat = 2
    # FH = Shuffle([1:10])
    # # sitmCat = 3
    # FS = Shuffle([1:10])
    # stimCat = 4
    MH = np.random.permutation(np.arange(1, 11))
    MS = np.random.permutation(np.arange(1, 11))
    FH = np.random.permutation(np.arange(1, 11))
    FS = np.random.permutation(np.arange(1, 11))

    #switchRewrd
    switchRewardProb = [20] ##Hyun## why there is only one probability in the list?
    NumTrialPerItem = 60

    M = pd.DataFrame(columns=col_names)
    for stimCat in range (1,5):
        NumItem = len(switchRewardProb)
        if stimCat == 1:   stimSet = MH[0: NumItem]
        elif stimCat == 2: stimSet = MS[0: NumItem]
        elif stimCat == 3: stimSet = FH[0: NumItem]
        elif stimCat == 4: stimSet = MS[0: NumItem]

        for i in range(len(stimSet)):
            condM = pd.DataFrame(columns=col_names)
            condM.stimId = np.ones(NumTrialPerItem)*stimSet[i]
            condM.SRP = np.ones(NumTrialPerItem)*switchRewardProb[i]
            #condM.trialType = reshape(repmat([0 1], NumTrialPerItem/2, 1), [], 1)
            ##Hyun## Please correct my translation is wrong for the code above
            condM.trialType = [0] * (NumTrialPerItem//2) + [1] * (NumTrialPerItem//2)
            condM.stimCat = stimCat                      
            HR = 10
            LR = 1
            ones = NumTrialPerItem//2 * switchRewardProb[i]//100
            zeros = NumTrialPerItem//2 * (100-switchRewardProb[i])//100
            #condM.loc[condM.trialType == 1, 'Rw'] = [np.ones(NumTrialPerItem/2 * switchRewardProb(i)/100)* HR; ones(NumTrialPerItem/2*(100-switchRewardProb(i))/100, 1) * LR]
            condM.loc[condM.trialType == 1, 'Rw'] = np.concatenate((np.ones(ones) * HR, np.ones(zeros) * LR))
            #condM.loc[condM.trialType == 0, 'Rw'] = [np.ones(NumTrialPerItem/2 * switchRewardProb(i)/100)* LR; ones(NumTrialPerItem/2*(100-switchRewardProb(i))/100, 1) * HR]
            condM.loc[condM.trialType == 0, 'Rw'] = np.concatenate((np.ones(ones) * LR, np.ones(zeros) * HR))
            M = pd.concat([M, condM], ignore_index=True)

    M.to_csv("../data/IScond_trial_sequence_" + str(SbjId) + ".csv", index=False)
    return

    while 1:
        seq = np.random.permutation(len(M))
        MM = M.loc[seq, :].reset_index(drop=True)

        ### assign task like you did in the mixedCCL
        # check there's roughly equal number of each task for each unique stimulus   (see if that's possible to exit the while
        # check to see if there's too many exact stimulus repetitoin(like in mixedCCL)
        # finally check to see if each task is associated with equal amount of reward
        # e.g  mean(M1(M1(:,idx.task) == 1,idx.Rw)) = mean(M1(M1(:,idx.task)==2,idx.Rw))  [or diff is <5]

        for i in range(len(M)):
            if E.loc[i, 'trialType'] == 'repeat':
                E.loc[i, 'task'] = currentTask
            else:
                currentTask = 3-currentTask
                E.loc[i, 'task'] = currentTask

        cnt = []
        expVal = len(M)/len(stimSet)/2
        for s in stimSet:
            selection = M.loc[(M['stimId'] == s) & (M['task'] == 1)]
            cnt.append(len(selection))

        stimCheck = np.diff(E['stimId'])
        if (sum(x <= 1 for x in abs(np.subtract(cnt, expVal))) == len(stimSet)) & ((stimCheck == 0).sum() / len(E) <= 0.5):
            break

    M.to_csv("../data/IScond_trial_sequence_" + str(SbjId) + ".csv",index=False)

if __name__ == '__main__':
    SbjId = int(input("Subject ID: "))
    gen(SbjId)
