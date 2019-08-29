import numpy as np
import pandas as pd
import random

def prompt():
    # ask for the name of the file
    fileName = input("What is the name of the file? ")

    # ask for number of blocks
    nblock = int(input("How many blocks? "))

    # ask for number of trials
    ntrial = int(input("How many trials? "))

    ## ask for number of faces
    nface = int(input("How many faces? "))

    # ask for number of names
    nname = int(input("How many names? "))

    M = np.zeros(shape=(nface+1, nname+1), dtype=object)

    # record all the column names, type (integer, text, etc)
    data = {
        "bid": nblock,
        "tid": ntrial,
        "fid": list(),
        "nid": list(),
        "corrResp": {}
    }
    file_path = "../images/"
    for i in range(nface):
        temp_name = input("Put a name for fid " + str(i+1) + ": ")
        data["fid"].append(temp_name)
        M[0,i+1] = temp_name
    for i in range(nname):
        temp_name = input("Put a name for nid" + str(i+1) + ": ")
        data["nid"].append(temp_name)
        M[i+1, 0] = temp_name

    while True:
        sum = 0
        for i in range(nname):
            for j in range(nface):
                n = int(input("How many trials for " + M[i+1, 0] + " & " + M[0, j+1] + "? "))
                M[i+1,j+1] = n
                sum += n
        print("Result Matrix from the input")
        print(M)
        if (sum != ntrial):
            print("the number of trials and the sum of each stimulus is different")
            print("number of trials: " + str(ntrial))
            print("sum of stimuli: " + str(sum))
            print("Please enter the numbers correctly.")
        else:
            break

    for item in data["fid"]:
        temp = input("What is a correct response for " + item + "? ")
        data["corrResp"][item] = temp

    print(data)

    col_names = ['bid', 'tid', 'nid', 'fid', 'face_path', 'congruency', 'corrResp']
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
        # print(block)
        # print(df)
            
    # random_sequence = block.sample(frac=1).reset_index(drop=True)
    # random_sequence.index = np.arange(1, len(block) + 1)
    # print(random_sequence)
    fileName = "../data/ISPC_squence_" + fileName + ".csv"
    print(fileName)
    df.to_csv(fileName, index=False)

if __name__ == "__main__":
    prompt()
