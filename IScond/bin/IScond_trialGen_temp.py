import sys
import numpy as np
import pandas as pd
sys.path.insert(0, '../')

def gen(SbjId=0): ##Hyun## a default SbjId is 0
    SbjId = 13
    # idx.bk_id     =1
    # idx.trial_id = 2
    # idx.stimCat = 3
    # idx.stimId = 4
    # idx.SRP = 5
    # idx.trialType = 6
    # idx.Rw = 7 # Rw = Reward amount
    # idx.response = 8
    col_names = ['block_id', 'trial_id', 'stimCat', 'stimId', 'SRP', 'trialType', 'task', 'Rw', 'response']

    # MH = Shuffle([1:10])
    # # stimCat = 1
    # MS = Shuffle([1:10])
    # # stimCat = 2
    # FH = Shuffle([1:10])
    # # sitmCat = 3
    # FS = Shuffle([1:10])
    # stimCat = 4
    MH = np.random.permutation(np.arange(1, 11, dtype=int))
    MS = np.random.permutation(np.arange(1, 11, dtype=int))
    FH = np.random.permutation(np.arange(1, 11, dtype=int))
    FS = np.random.permutation(np.arange(1, 11, dtype=int))

    #switchRewrd
    switchRewardProb = [20, 50] ##Hyun## why there is only one probability in the list?
    NumTrialPerItem = 60
    HR = 10
    LR = 1

    M = pd.DataFrame(columns=col_names)
    stimSetTotal = []
    for stimCat in range (1,5):
        NumItem = len(switchRewardProb)
        if stimCat == 1:   stimSet = MH[0: NumItem]
        elif stimCat == 2: stimSet = MS[0: NumItem]
        elif stimCat == 3: stimSet = FH[0: NumItem]
        elif stimCat == 4: stimSet = FS[0: NumItem]
        stimSetTotal.extend(stimSet)
        print(stimSet)
        for i in range(len(stimSet)):
            condM = pd.DataFrame(columns=col_names)
            condM.stimId = np.ones(NumTrialPerItem, dtype=int)*stimSet[i]
            condM.SRP = np.ones(NumTrialPerItem, dtype=int)*switchRewardProb[i]
            #condM.trialType = reshape(repmat([0 1], NumTrialPerItem/2, 1), [], 1)
            ##Hyun## Please correct my translation is wrong for the code above
            condM.trialType = [0] * (NumTrialPerItem//2) + [1] * (NumTrialPerItem//2)
            condM.stimCat = stimCat                      

            ones = NumTrialPerItem//2 * switchRewardProb[i]//100
            zeros = NumTrialPerItem//2 * (100-switchRewardProb[i])//100
            #condM.loc[condM.trialType == 1, 'Rw'] = [np.ones(NumTrialPerItem/2 * switchRewardProb(i)/100)* HR; ones(NumTrialPerItem/2*(100-switchRewardProb(i))/100, 1) * LR]
            condM.loc[condM.trialType == 1, 'Rw'] = np.concatenate((np.ones(ones) * HR, np.ones(zeros) * LR))
            #condM.loc[condM.trialType == 0, 'Rw'] = [np.ones(NumTrialPerItem/2 * switchRewardProb(i)/100)* LR; ones(NumTrialPerItem/2*(100-switchRewardProb(i))/100, 1) * HR]
            condM.loc[condM.trialType == 0, 'Rw'] = np.concatenate((np.ones(ones) * LR, np.ones(zeros) * HR))
            M = pd.concat([M, condM], ignore_index=True)
    print(stimSetTotal)

    while 1:
        seq = np.random.permutation(len(M))
        M1 = M.loc[seq, :].reset_index(drop=True)
        currentTask = np.remainder(round(np.random.rand()*100), 2)+1

        ### assign task like you did in the mixedCCL
        # 1. check there's roughly equal number of each task for each unique stimulus (see if that's possible to exit the while
        ##Hyun##
        # there are 4 unique stimuls (1, 2, 3, 4)
        # there are 2 unique tasks/trialType (0, 1) <-- Please let me know if those are still 'switch' & 'repeat'
        
        # for i in range(len(M)):
        #     if M.loc[i, 'trialType'] == 1:
        #         M.loc[i, 'task'] = currentTask
        #     else:
        #         currentTask = 3-currentTask
        #         M.loc[i, 'task'] = currentTask
        M.loc[M.trialType == 1, 'task'] = currentTask
        M.loc[M.trialType != 1, 'task'] = 3-currentTask

        # 2. check to see if there's too many exact stimulus repetitoin(like in mixedCCL)
        cnt = []
        expVal = len(M)/len(stimSetTotal)/2
        for s in stimSetTotal:
            selection = M.loc[(M['stimId'] == s) & (M['task'] == 1)]
            cnt.append(len(selection))
        # 3. finally check to see if each task is associated with equal amount of reward
        # e.g  mean(M1(M1(:,idx.task) == 1,idx.Rw)) = mean(M1(M1(:,idx.task)==2,idx.Rw))  [or diff is <5]
        ##Hyun##
        # when you say each task for each amount of reward, do you mean
        # 1. number of task ==1
        # 2. number of task ==2
        # OR
        # 1. number of (task == 1 && reward == LR)
        # 2. number of (task == 2 && reward == HR)
        # 3. number of (task == 1 && reward == LR)
        # 4. number of (task == 2 && reward == HR)
        mean_task1 = M1.loc[(M1.task == 1) & (M1.Rw == LR), 'Rw'].mean()
        mean_task2 = M1.loc[(M1.task == 1) & (M1.Rw == HR), 'Rw'].mean()
        mean_task3 = M1.loc[(M1.task == 2) & (M1.Rw == LR), 'Rw'].mean()
        mean_task4 = M1.loc[(M1.task == 2) & (M1.Rw == HR), 'Rw'].mean()
        mean_task5 = M1.loc[(M1.task == 1), 'Rw'].mean()
        mean_task6 = M1.loc[(M1.task == 2), 'Rw'].mean()
        # check1 = (sum(x <= 1 for x in abs(np.subtract(cnt, expVal))) == len(stimSetTotal))
        check1 = sum(x <= 1 for x in abs(np.subtract(cnt, expVal)))
        check2 = mean_task1 - mean_task2
        print('{}\t{}'.format( check1, check2 ))
        if (sum(x <= 1 for x in abs(np.subtract(cnt, expVal))) == len(stimSetTotal)) & (mean_task1 - mean_task2 <= 5):
            M = M1
            break

    M.task = M.task.map({1:'size', 2:'animacy'})
    M.to_csv('../data/IScond_trial_sequence_' + str(SbjId) + ".csv", index=False)

if __name__ == '__main__':
    SbjId = int(input("Subject ID: "))
    gen(SbjId)
