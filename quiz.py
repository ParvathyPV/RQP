from flask import Flask, render_template, request
import random, copy

app = Flask(__name__)

@app.route('/student', methods = ['POST', 'GET'])
def student():
    if request.method == 'POST':
        code = request.form['password']
        if code == 'admin':
            return render_template('qgen.html')
        else:
            return render_template('error.html')
original_questions = {
 #Format is 'question':[options]
 'Which of the following is not a valid variable name declaration?':
 ['None of the mentioned;',' int __a3;','int __A3;','int 3__a'],
 'All keywords in C are in ____________':
 ['Lowercase','Uppercase','Camelcase','None of the mentioned'],
 ' What is the size of an int data type?':
 ['Depends on the system/compiler','8 Bytes','4 Bytes','Cannot be determined'],
 'The format identifier ‘%i’ is also used for _____ data type.':
 ['int','char','float','double'],
 'Which data type is most suitable for storing a number 65000 in a 32-bit system?':
 ['unsigned short','signed short','long','int']
 #'Colosseum':['Rome','Milan','Bari','Bologna'],
 #'Christ the Redeemer':['Rio de Janeiro','Natal','Olinda','Betim']
}

questions = copy.deepcopy(original_questions)

def shuffle(q):
 """
 This function is for shuffling 
 the dictionary elements.
 """
 selected_keys = []
 i = 0
 while i < len(q):
  current_selection = random.choice(list(q.keys()))
  if current_selection not in selected_keys:
   selected_keys.append(current_selection)
   i = i+1
 return selected_keys

@app.route('/qu', methods=['POST'])
def quiz():
 questions_shuffled = shuffle(questions)
 for i in questions.keys():
  random.shuffle(questions[i])
 return render_template('main.html', q = questions_shuffled, o = questions)


@app.route('/quiz', methods=['POST'])
def quiz_answers():
 correct = 0
 for i in questions.keys():
  answered = request.form[i]
  if original_questions[i][0] == answered:
   correct = correct+1
 return '<h1>Correct Answers: <u>'+str(correct)+'</u></h1>'

if __name__ == '__main__':
  app.run(debug=True)