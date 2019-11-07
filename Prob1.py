#%%
def problem3_1(txtfilename):
    infile = open(txtfilename)
    charct_cnt = 0
    for line in (infile):
        print (line,end="")
        charct_cnt = charct_cnt + len(line)
    infile.close()
    print("\n\nThere are",charct_cnt,"letters in the file.")