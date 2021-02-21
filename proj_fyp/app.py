from flask import Flask, render_template
#from summa.summarizer import summarize
import os
from summ_fn import *
app=Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')
	
@app.route('/summarise/')
def my_link():
    #print('this works')
    op=summariser('trans.txt')
    write_to_file(op,'summ_trans.txt')
    return op
	
if __name__=='__main__':
	app.run(debug=True)