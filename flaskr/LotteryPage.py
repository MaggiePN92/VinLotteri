from flask import Flask, render_template, request
app = Flask(__name__)
from flaskr.Lottery import Lottery
lotto = Lottery()

@app.route('/form')
def form():
    return render_template('form.html')


@app.route('/data', methods=['POST', 'GET'])
def data():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        form_data = request.form
        lotto.handle_form_data(form_data)
        lottery_dict = lotto.get_lottery_dict()
        #return render_template('data.html', form_data=form_data)
        return render_template('data_table.html', lottery_dict=lottery_dict)

if __name__ == "__main__":
    app.run()#host='localhost', port=5000, debug=True)