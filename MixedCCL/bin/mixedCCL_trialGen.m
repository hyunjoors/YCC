function trialSeq = trialGen(SbjId)	
order_all     = [1 2 3;3 2 1];
SRmapping_all = [1 2 1 2;1 2 2 1;2 1 1 2; 2 1 2 1]; % which key to press for [large small living nonliving]
incompCat_all = [2 3;1 4;1 4;2 3]; % based on SR mapping, what are the categories that are resp incompatible in the two tasks

LivLg = Shuffle([1:10]);   % cat =1
LivSm = Shuffle([11:20]);  % cat =2
NLvLg = Shuffle([21:30]);  % cat =3
NLvSm = Shuffle([31:40]);  % cat =4

%
%SbjId =1;
SRmapping = SRmapping_all(rem(SbjId,4)+1,:);
order     = order_all(rem(round(rand()*10),2)+1,:);
incompCat = incompCat_all(rem(SbjId,4)+1,:);

idx.stimLv   = 1; % living/nonliving
idx.stimSz   = 2; % size 
idx.stimCat  = 3;
idx.stimId   = 4; % unique id for each stimulus/object (e.g., apple, banana)
idx.bkSwProb = 5;
idx.itSwProb = 6;
idx.trialType= 7;  % switch(1) vs. repeat(0)
idx.task     = 8;
idx.response = 9;

trPerStim=40;

E_all=[];
for bk=1:3
    switch order(bk)
        case 1 % low
            BkSwProb=30;
            ItSwProbList=[20,20,50,20,20,50];
        case 2
            BkSwProb=50;
            ItSwProbList=[20,50,80,20,50,80];
        case 3
            BkSwProb=70;
            ItSwProbList=[80,80,50,80,80,50];
    end
    stimSet=[];
    stimCat=[];
    for i=1:length(incompCat)
        switch incompCat(i)
            case 1
                stimSet = [stimSet LivLg(1:3)];
                LivLg = LivLg(4:end);
                stimCat =[stimCat 1 1 1];
            case 2
                stimSet = [stimSet LivSm(1:3)];
                LivSm = LivSm(4:end);
                stimCat =[stimCat 2 2 2];
            case 3
                stimSet = [stimSet NLvLg(1:3)];
                NLvLg = NLvLg(4:end);
                stimCat =[stimCat 3 3 3];
            case 4
                stimSet = [stimSet NLvSm(1:3)];
                NLvSm = NLvSm(4:end);
                stimCat =[stimCat 4 4 4];
        end
    end
    
    E = [];
    for i=1:length(stimSet)
        
        NrSw = trPerStim*ItSwProbList(i)/100;
        NrRp = trPerStim - NrSw;
        condE(:,idx.stimId)  = ones(trPerStim,1)*stimSet(i);
        condE(:,idx.stimCat) = stimCat(i);
        condE(:,idx.trialType) = [ones(NrSw,1);zeros(NrRp,1)];
        condE(:,idx.itSwProb)  = ItSwProbList(i);
        condE(:,idx.bkSwProb)  = BkSwProb;
        E = [E;condE];     
        
    end
    
    
    while 1,
        seq = Shuffle(1:length(E));
        E = E(seq,:);
        currentTask = rem(round(rand*100),2)+1;
        
        for i=1:length(E)
            if E(i,idx.trialType)==0
                E(i,idx.task)=currentTask;            
            else
                currentTask=3-currentTask;
                E(i,idx.task)=currentTask;
            end
        end

        cnt=[];
        expVal = length(E)/length(stimSet)/2;
        for s=stimSet
            cnt = [cnt;size(find(E(:,idx.stimId)==s & E(:,idx.task)==1),1)];        
        end
        
        
        
        if size(find(abs(cnt-expVal)<=1),1)==length(stimSet) && ... % make sure each stim appears in each task roughly the same frequency
                length(find(diff(E(:,idx.stimId))==0))/length(E)<=.10 % make sure to not have too many same stim in two trials
            break
        end
    
    end
    E_all=[E_all;E];
    
end

E_all(E_all(:,idx.stimCat)<=2,idx.stimLv)=1; % living
E_all(E_all(:,idx.stimCat)>=3,idx.stimLv)=0;
E_all(E_all(:,idx.stimCat)==1|E_all(:,idx.stimCat)==3,idx.stimSz)=1;  %large
E_all(E_all(:,idx.stimCat)==2|E_all(:,idx.stimCat)==4,idx.stimSz)=0;  %small

for i=1:length(E_all)
    if E_all(i,idx.task)==1 % size task  
        if E_all(i,idx.stimSz)==1
            E_all(i,idx.response)=SRmapping(1);  % [large small living nonliving]
        else
            E_all(i,idx.response)=SRmapping(2);
        end        
    else % living nonlivint task
        if E_all(i,idx.stimLv)==1 
            E_all(i,idx.response)=SRmapping(3);
        else
            E_all(i,idx.response)=SRmapping(4);
        end 
    end
end

trialSeq=E_all;
