import numpy as np
import pandas as pd
import random

class ISPC_v2_trialGen:

    def __init__(self, subjectID):
        self.subjectID = int(subjectID)
        self.subjectHashID = np.remainder(self.subjectID, 6)
        self.SRmapping_all = [
            ["v", "b", "n"],
            ["v", "n", "b"],
            ["b", "v", "n"],
            ["b", "n", "v"],
            ["n", "v", "b"],
            ["n", "b", "v"]
        ]
        self.SRmapping = self.SRmapping_all[self.subjectHashID]
        self.col_names = ['bid', 'tid', 'nid', 'fid', 'face_path', 'congruency', 'PC', 'frequency','corrResp', 'sbjResp', 'sbjCorr', 'sbjRT']
    
    def practice(self):
        # record all the column names, type (integer, text, etc)
        data = {
            "bid": 1,
            "tid": 30,
            "fid": ["Clooney", "Cruise", "Damon"],
            "nid": ["XXXXX"],
            "corrResp": {}
        }
        M = np.array([[0, 0, 0, 0],
                      [0, 10, 10, 10]], dtype=object)
        
        for i in range(3):
            M[0,i+1] = data["fid"][i]
        for i in range(1):
            M[i+1, 0] = data["nid"][i]

        for item in range(len(data["fid"])):
            data["corrResp"].update({data["fid"][item] : self.SRmapping[item]})
    
        df = pd.DataFrame(columns=self.col_names)
        sequences = pd.DataFrame(columns=self.col_names)
        index = 0
        for i in range(1):
            for j in range(3):
                fid = M[0, j+1]
                nid = M[i+1, 0]
                face_path = "./images/" + fid + ".jpg"
                congruency = 'incongruent'
                if fid == nid:
                    congruency = 'congruent'
                corrResp = data["corrResp"].get(fid)
                for tid in range(M[i+1, j+1]):
                    # ['bid', 'tid', 'nid', 'fid', 'face_path', 'congruency', 'PC', 'frequency','corrResp', 'sbjResp', 'sbjCorr', 'sbjRT']
                    sequences.at[index, 'nid'] = nid
                    sequences.at[index, 'fid'] = fid
                    sequences.at[index, 'face_path'] = face_path
                    sequences.at[index, 'congruency'] = congruency
                    sequences.at[index, 'corrResp'] = corrResp
                    index += 1

        r = list(range(len(sequences)))
        random.shuffle(r)
        block = sequences.loc[r, ]
        block.tid = np.arange(1,len(sequences)+1)
        block.bid = 1
        df = df.append(block)#, sort=False)
        
        return df, list(data["corrResp"].items())
    
    
    def exp(self):
        # record all the column names, type (integer, text, etc)
        data = {
            "bid": 5,
            "tid": 72,
            "fid": ["Clooney", "Cruise", "Damon"],
            "nid": ["Clooney", "Cruise", "Damon"],
            "corrResp": {}
        }
        M = np.array([[0, 0, 0, 0],
                      [0, 18, 18, 18],
                      [0, 3, 3, 3],
                      [0, 3, 3, 3]], dtype = object)
        M_PC = np.array([[0, 0, 0, 0],
                         [0, 'MC-C', 'MIC-IC', 'MIC-IC'],
                         [0, 'MC-IC', 'MIC-C', 'MC-C'],
                         [0, 'MC-IC', 'MC-C', 'MIC-C']], dtype=object)
        M_FREQ = np.array([[0, 0, 0, 0],
                           [0, 'freq', 'freq', 'freq'],
                           [0, 'infreq', 'infreq', 'infreq'],
                           [0, 'infreq', 'infreq', 'infreq']], dtype=object)
    
        for i in range(3):
            M[0, i+1] = data["fid"][i]
        for i in range(3):
            M[i+1, 0] = data["nid"][i]
    
        for item in range(len(data["fid"])):
            data["corrResp"].update({data["fid"][item]: self.SRmapping[item]})
    
        df = pd.DataFrame(columns=self.col_names)
        sequences = pd.DataFrame(columns=self.col_names)
        index = 0
        for i in range(1):
            for j in range(3):
                fid = M[0, j+1]
                nid = M[i+1, 0]
                face_path = "./images/" + fid + ".jpg"
                congruency = 'incongruent'
                if fid == nid:
                    congruency = 'congruent'
                corrResp = data["corrResp"].get(fid)
                for tid in range(M[i+1, j+1]):
                    # ['bid', 'tid', 'nid', 'fid', 'face_path', 'congruency', 'PC', 'frequency','corrResp', 'sbjResp', 'sbjCorr', 'sbjRT']
                    sequences.at[index, 'nid'] = nid
                    sequences.at[index, 'fid'] = fid
                    sequences.at[index, 'face_path'] = face_path
                    sequences.at[index, 'congruency'] = congruency
                    sequences.at[index, 'corrResp'] = corrResp
                    index += 1

        for bid in range(data['bid']):
            r = list(range(len(sequences)))
            random.shuffle(r)
            block = sequences.loc[r, ]
            block.tid = np.arange(1,len(sequences)+1)
            block.bid = bid+1
            df = df.append(block)#, sort=False)

        return df, list(data["corrResp"].items())
