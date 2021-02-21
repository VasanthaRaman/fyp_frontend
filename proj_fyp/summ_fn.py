from summa.summarizer import summarize
import os

def write_to_file(op,ofname):
    fo=open('C:\\Users\\Vasanth\\Downloads\\'+ofname,'w',encoding='utf-8')
    fo.write(op)
    fo.close()
    
def summariser(fname):
	fi=open('C:\\Users\\Vasanth\\Downloads\\'+fname,'r',encoding='utf-8')
	tt=fi.readlines()
	ss=''
	for line in tt:
		ss=ss+line
	op=summarize(ss,ratio=0.5)
	return op