#pip install flask
from flask import Flask,render_template, request
import matplotlib.pyplot as plt
app = Flask(__name__)#variable and module name can be anything

@app.route('/',methods=['GET', 'POST']) 
#the methods that can be used to access the URL
#binds the URL with the def written below it

def details():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        type = request.form['ID']
        id = request.form['id_value']
        if id == '':
            return render_template('wrong.html')
        id = int(id)
        data= []
        with open('data.csv', 'r') as file:
            file.readline()
            if type == 'student_id':
                for row in file:
                    row = list(map(int,row.strip().split(',')))
                    if row[0] == id:
                        data.append(row)
            
            elif type == 'course_id':
                for row in file:
                    row = list(map(int,row.strip().split(',')))
                    if row[1] == id:
                        data.append(row)
            
            else:
                pass           
        if len(data) == 0:
            return render_template('wrong.html')
        elif type == 'student_id':
            tm =0
            for x in data:
                tm += x[2]
            return render_template('student_details.html', data=data, total_marks=tm)
        else:
            marks=[x[2] for x in data if x[1] == id]
            a = sum(marks)/len(marks)
            m = max(marks)
            plt.hist(marks)
            plt.xlabel('Marks')
            plt.ylabel('Frequency')
            plt.savefig('static/plot.png')
            return render_template('course_details.html', average_marks=a, maximum_marks=m, img='static/plot.png')





app.run(debug=True, port=5001)
#app.run()

