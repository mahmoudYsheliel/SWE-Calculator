from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/')
def calculator():
  return render_template('calc.html')
@app.route('/calculate',methods=['POST'])
def calculate():
    num1=float(request.form['num1'])
    num2=float(request.form['num2'])
    opration=request.form['oprations']
    result=0
    if opration=='add':
        result=num1+num2
    elif opration=='sub':
        result=num1-num2
    elif opration=='mul':
        result=num1*num2
    elif opration=='div' and num2!=0:
        result=num1/num2
    else:
        result='not good inputs'
    return render_template('calc.html',result=result)

if __name__ == '__main__':
  app.run(debug=True)