from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

trading_data = []

@app.route('/')
def index():
    return render_template('investment.html')

@app.route('/api/trading_data', methods=['GET'])
def det_trading_data():
    return jsonify(trading_data)

@app.route('/api/update_trading_data', methods=['POST'])
def update_trading_data():
    global trading_data
    new_data = jsonify(request.data)
    trading_data.append(new_data)
    return jsonify({'status', 'success'})

if __name__ == '__main__':
    app.run(debug=True)