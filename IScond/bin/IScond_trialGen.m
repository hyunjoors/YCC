import numpy as np
import pandas as pd

idx.bk_id     =1
idx.trial_id  = 2
idx.stimCat   = 3
idx.stimId    = 4
idx.SRP       = 5
idx.trialType = 6
idx.Rw        = 7  % Rw = Reward amount
idx.response  = 8

MH = Shuffle([1:10]); % stimCat =1
MS = Shuffle([1:10]); % stimCat =2
FH = Shuffle([1:10]); % sitmCat =3
FS = Shuffle([1:10]); % stimCat =4

%switchRewrd 
switchRewardProb = [20];
NrTrialPerItem = 60;

M=[];
for stimCat =[1:4]
    NrItem = length(switchRewardProb);
    switch stimCat
        case 1
            stimSet = MH(1:NrItem);
        case 2
            stimSet = MS(1:NrItem);
        case 3
            stimSet = FH(1:NrItem);
        case 4
            stimSet = MS(1:NrItem);
    end
    
    for i=1:length(stimSet)
        condM=[];
        condM(:,idx.stimId)    = ones(NrTrialPerItem,1)*stimSet(i);
        condM(:,idx.SRP)       = ones(NrTrialPerItem,1)*switchRewardProb(i);
        condM(:,idx.trialType) = reshape(repmat([0 1],NrTrialPerItem/2,1),[],1);
        condM(:,idx.stimCat)   = stimCat;                        
        HR=10;
        LR=1;
        condM(condM(:,idx.trialType)==1,idx.Rw)=[ones(NrTrialPerItem/2*switchRewardProb(i)/100,1)*HR;ones(NrTrialPerItem/2*(100-switchRewardProb(i))/100,1)*LR];
        condM(condM(:,idx.trialType)==0,idx.Rw)=[ones(NrTrialPerItem/2*switchRewardProb(i)/100,1)*LR;ones(NrTrialPerItem/2*(100-switchRewardProb(i))/100,1)*HR];
        M=[M;condM];
    end
end    

return


while 1
    seq = Shuffle(1:length(M));
    M1 = M(seq,:);
    
    
    %%% assign task like you did in the mixedCCL 
    % check there's roughly equal number of each task for each unique stimulus   (see if that's possible to exit the while   
    % check to see if there's too many exact stimulus repetitoin (like in mixedCCL)
    % finally check to see if each task is associated with equal amount of reward 
    % e.g  mean(M1(M1(:,idx.task) ==1,idx.Rw)) = mean(M1(M1(:,idx.task)==2,idx.Rw))  [or diff is <5]
    
    
    
end

