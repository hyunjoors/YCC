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
        self.col_names_block = ['bid', 'tid', 'nid', 'fid', 'face_path', 'congruency', 'corrResp']
        self.col_names = ['bid', 'tid', 'nid', 'fid', 'face_path', 'congruency', 'corrResp', 'sbjResp', 'sbjCorr', 'sbjRT']
    
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
        sequences = []
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
                    current_row = [nid, fid, face_path, congruency, corrResp]
                    sequences.append(current_row)
    
        for bid in range(data['bid']):
            tid = 1
            shuffled_sequence = []
            r = list(range(len(sequences)))
            random.shuffle(r)
            for row in r:
                current_row = [bid+1, tid] + sequences[row]
                tid = tid + 1
                shuffled_sequence.append(current_row)
            block = pd.DataFrame(shuffled_sequence, columns=self.col_names_block)
            df = df.append(block)
            
        return df, list(data["corrResp"].items())
    
    
    def exp(self):
        # record all the column names, type (integer, text, etc)
        data = {
            "bid": 5,
            "tid": 9,
            "fid": ["Clooney", "Cruise", "Damon"],
            "nid": ["Clooney", "Cruise", "Damon"],
            "corrResp": {}
        }
        M = np.array([[0, 0, 0, 0],
                      [0, 1, 1, 1],
                      [0, 1, 1, 1],
                      [0, 1, 1, 1]], dtype = object)
    
        for i in range(3):
            M[0, i+1] = data["fid"][i]
        for i in range(3):
            M[i+1, 0] = data["nid"][i]
    
        for item in range(len(data["fid"])):
            data["corrResp"].update({data["fid"][item]: self.SRmapping[item]})
    
        df = pd.DataFrame(columns=self.col_names)
        sequences = []

        for i in range(3): # for each name
            for j in range(3): # for each face
                fid = M[0, j+1]
                nid = M[i+1, 0]
                face_path = "./images/" + fid + ".jpg"
                congruency = 'incongruent'
                if fid == nid:
                    congruency = 'congruent'
                corrResp = data["corrResp"].get(fid)
                for tid in range(M[i+1, j+1]):
                    current_row = [nid, fid, face_path, congruency, corrResp]
                    sequences.append(current_row)
    
        for bid in range(data['bid']):
            tid = 1
            shuffled_sequence = []
            r = list(range(len(sequences)))
            random.shuffle(r)
            for row in r:
                current_row = [bid+1, tid] + sequences[row]
                tid = tid + 1
                shuffled_sequence.append(current_row)
            block = pd.DataFrame(shuffled_sequence, columns=self.col_names_block)
            df = df.append(block)

        return df, list(data["corrResp"].items())
