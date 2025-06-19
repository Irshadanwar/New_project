from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def details():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        id = request.form['id_value']
        if id == '':
            return render_template('wrong.html')
        id = int(id)
        data = []
        with open('data.csv', 'r') as file:
            file.readline()
            for row in file:
                row = list(map(int, row.strip().split(',')))
                if row[0] == id:
                    data.append(row)
        if not data:
            return render_template('wrong.html')
        total_marks = sum(x[2] for x in data)
        return render_template('student_details.html', data=data, total_marks=total_marks)

app.run(debug=True, port=5001)