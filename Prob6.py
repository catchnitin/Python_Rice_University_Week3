import sys
charct_cnt = 0
infilename = sys.argv[1]
outfilename = sys.argv[2]
infile = open(infilename)
opfile = open(outfilename,'w')
for line in (infile):
    line = line.strip("\n")
    print (line,end="")
    charct_cnt = len(line)
    opfile.write(str(charct_cnt))
    opfile.write("\n")
    print("\n\nThere are",charct_cnt,"letters in the line.")
infile.close()
opfile.close()
print("\n\nThere are",charct_cnt,"letters in the file.")