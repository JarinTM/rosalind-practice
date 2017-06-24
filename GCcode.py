


infile = open("alzheimer.txt","r")
name = infile.readline()
raw_data = infile.read(5000)
seq = raw_data.replace('\n','')
#print name
#print raw_data

#seq="ABCdEFdKSd"
#seq.replace('d','n')
#print seq.replace('d','n')
# 
countG = seq.count("G") 
 
countC= seq.count("C")
 
seqlen=len(seq)
 
GCcontent=(( float(countG)+(countC))/seqlen)*100
 
print GCcontent
 
 

