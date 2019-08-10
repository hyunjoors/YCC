import csv
import numpy as np
import pandas as pd
import random

SRmapping = [
    ["v", "b", "n"],
    ["v", "n", "b"],
    ["b", "v", "n"],
    ["b", "n", "v"],
    ["n", "v", "b"],
    ["n", "b", "v"]
]
col_names = ['bid', 'tid', 'nid', 'fid', 'face_path', 'congruency', 'corrResp']

def practice(int subjectHashID):
    # record all the column names, type (integer, text, etc)
    data = {
        "bid": 1,
        "tid": 30,
        "fid": ["Clooney", "Cruise", "Damon"],
        "nid": ["XXXXX"],
        "corrResp": {}
    }
    M = np.array([[0,0,0,0], [0, 10, 10, 10], dtype = object)
    
    file_path = "../images/"
    for i in range(3):
        M[0,i+1] = data["fid"][i]
    for i in range(1):
        M[i+1, 0] = data["nid"][i]

    for item in data["fid"]:
        data["corrResp"][item] = SRmapping[subjectHashID][item]

    print(data)
    print(M)

    df = pd.DataFrame(columns=col_names)
    sequences = []
    for i in range(nname):
        for j in range(nface):
            fid = M[i+1, 0]
            nid = M[0, j+1]
            face_path = "../images/" + fid + ".jpg"
            congruency = 'incongruent'
            if fid == nid:
                congruency = 'congruent'
            corrResp = data["corrResp"].get(fid)
            for tid in range(M[i+1, j+1]):
                current_row = [nid, fid, face_path, congruency, corrResp]
                sequences.append(current_row)

    for bid in range(nblock):
        tid = 1
        shuffled_sequence = []
        r = list(range(len(sequences)))
        random.shuffle(r)
        for row in r:
            current_row = [bid+1, tid] + sequences[row]
            tid = tid + 1
            shuffled_sequence.append(current_row)
        block = pd.DataFrame(shuffled_sequence, columns=col_names)
        df = df.append(block)
            
    fileName = "../data/ISPC_squence_" + fileName + ".csv"
    print(fileName)
    df.to_csv(fileName, index=False)


def exp():
    # record all the column names, type (integer, text, etc)
    data = {
        "bid": 5,
        "tid": 72,
        "fid": ["Clooney", "Cruise", "Damon"],
        "nid": ["Clooney", "Cruise", "Damon"],
        "corrResp": {}
    }
    M = np.array([[0, 0, 0, 0], [0, 18, 18, 18], [0, 3, 3, 3], [0, 3, 3, 3]], dtype = object)

    file_path = "../images/"
    for i in range(3):
        M[0, i+1] = data["fid"][i]
    for i in range(1):
        M[i+1, 0] = data["nid"][i]

    for item in data["fid"]:
        data["corrResp"][item] = SRmapping[subjectHashID][item]

    print(data)
    print(M)

    df = pd.DataFrame(columns=col_names)
    sequences = []
    for i in range(nname):
        for j in range(nface):
            fid = M[i+1, 0]
            nid = M[0, j+1]
            face_path = "../images/" + fid + ".jpg"
            congruency = 'incongruent'
            if fid == nid:
                congruency = 'congruent'
            corrResp = data["corrResp"].get(fid)
            for tid in range(M[i+1, j+1]):
                current_row = [nid, fid, face_path, congruency, corrResp]
                sequences.append(current_row)

    for bid in range(nblock):
        tid = 1
        shuffled_sequence = []
        r = list(range(len(sequences)))
        random.shuffle(r)
        for row in r:
            current_row = [bid+1, tid] + sequences[row]
            tid = tid + 1
            shuffled_sequence.append(current_row)
        block = pd.DataFrame(shuffled_sequence, columns=col_names)
        df = df.append(block)

    fileName = "../data/ISPC_squence_" + fileName + "_practice.csv"
    print(fileName)
    df.to_csv(fileName, index=False)

if __name__ == "__main__":
    practice()
    exp()
