import csv

# two swProb for each 2x2 category =8 uniqu stim

idx.stimLv = 1 # living/nonliving
idx.stimSz = 2 # size 
idx.stimCat =3
idx.stimId = 4 # unique id for each stimulus/object (e.g., apple, banana)
idx.swProb = 5 
idx.task    = 6
idx.trialType=7  # switch vs. repeat

col_names = ['stimLv', 'stimSz', 'stimCat', 'stimId', 'swProb', 'task', 'trialType']
# stimLv: living & non-living
# stimSz: size
# stimCat:
# stimId: unique id for each stimulus/object (e.g., apple, banana)
# swProb:
# task:
# tiralType: switch vs. repeat

itemRep = 40
stim = [1:8]

conM (:,idx.stimLv) = reshape(ones(4,1)*[1 2],[],1)
conM (:,idx.stimSz) = reshape(ones(2,1)*[1 2 1 2],[],1)
conM (:,idx.swProb) = reshape((ones(4,1)*[25 75]),[],1)
conM (:,idx.stimId) = [1:8]
conM (:,idx.stimCat)= reshape(ones(2,1)*[1 2 3 4],[],1)
M=[]

for i = 1:size(conM,1)
    sw = itemRep*(conM(i,idx.swProb))/100
    rep  = itemRep - sw
    T = ones(itemRep,1)*conM(i,:)
    T(:,idx.trialType)=[ones(sw,1);zeros(rep,1)]
    M=[M;T]

while true:
    seq = Shuffle([1:size(M,1)])
    M1=M(seq,:)

    t=Shuffle([1 2])
    currentTask=t(1)

    for i=1:size(M1,1)
        if M1(i,idx.trialType)==1
            currentTask=3-currentTask
        M1(i, idx.task)=currentTask

    for stimId=1:8
        nrT1(stimId,1) = size(find(M1(:,idx.task)==1 & M1(:,idx.stimId)==stimId),1)

    exp=itemRep/2

    if size(find(abs(nrT1-itemRep/2)<=1),1)==8
        break
