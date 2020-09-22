from flask import Flask, render_template, request
def sortstr(Y):
    for i in range(1, len(Y)):
        b = Y[i]
        j = i - 1
        while (j >= 0) and (b < Y[j]):
            Y[j + 1] = Y[j]
            j -= 1
        Y[j + 1] = b
    return Y
app = Flask(__name__)

@app.route("/")
def go():
    filename = 'programm.csv'
    with open(filename, 'w') as file_object:
        file_object.write('name')
        file_object.write(',')
        file_object.write('email')
        file_object.write(',')
        file_object.write('answer')
        file_object.write("\n")
    return render_template("testing1.html")


@app.route('/answer', methods=['POST'])
def nn():
    name = request.form['name']
    email = request.form['email']
    answer = request.form['message']
    filename = 'programm.csv'

    with open(filename, 'a') as file_object:
        file_object.write(name)
        file_object.write(',')
        file_object.write(email)
        file_object.write(',')
        file_object.write(answer)
        file_object.write("\n")

    return render_template("testing1.html")

@app.route('/answer2', methods=['POST'])
def sortsting():
    string = list(map(int,request.form['string'].split()))
    string = sortstr(string)
    string = " ".join(map(str,string))
    return render_template('my_pril.html', ans=string)

if __name__ == "__main__":
     app.run(debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/я
