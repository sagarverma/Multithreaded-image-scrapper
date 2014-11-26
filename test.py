import simplejson
fin = open('BX-Books.csv','r')
fouts = open('img-s.txt','w')
foutm = open('img-m.txt','w')
foutl = open('img-l.txt','w')
strs = ""
strm = ""
strl = ""
for line in fin:
	temp = line.split('";"')
	strs+=temp[5]
	strs+='\n'
	strm+=temp[6]
	strm+='\n'
	strl+=temp[7]
foutl.write(strl)
foutm.write(strm)
fouts.write(strs)