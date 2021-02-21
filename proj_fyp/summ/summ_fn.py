from summa.summarizer import summarize
import os
def summariser(fname):
	fi=open('C:\\Users\\Vasanth\\Downloads\\'+f_name,'r',encoding='utf-8')
	tt=fi.readlines()
	ss=''
	for line in tt:
		ss=ss+line
	ip_text.append(ss)
	op=summarize(ss,ratio=0.5)
	fi.close()
	return op
		