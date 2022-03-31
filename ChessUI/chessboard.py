from flask import Flask,render_template,request,flash
from  algorithms import backtracking, hillclimbing, genetic_algorithm
 

app = Flask(__name__)


@app.route('/')
def home_page():
    positions = [100,100,100,100,100]
    return render_template("ChessBoard.html", size = 7,new_positions = positions)

@app.route('/algos', methods=['POST'])
def result_page():
    algo = int(request.form.get("algos"))
    board_size = int(request.form.get("board_size"))
    #if size <= 3:
        #flash(u'Solution does not exist', 'Warning')
    if algo == 1:
        positions = backtracking.main(board_size)
    elif algo == 2:
        positions = hillclimbing.main(board_size)
    else:
        positions = genetic_algorithm.main(board_size)
    new_pos =[]
    n= len(positions)
    for i,item in enumerate(positions):
        new_pos.append(item+i*n)
    return render_template("ChessBoard.html", size = board_size ,new_positions = new_pos)

if __name__ == "__main__":
    app.run()