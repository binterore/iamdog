from flask import Flask, request, jsonify
import flask
from flask_cors import CORS
app = flask.Flask(__name__)
CORS(app)

# 示例数据 - 用于演示目的
data = {
    'items': [
        {'id': 1, 'name': 'Item 1'},
        {'id': 2, 'name': 'Item 2'},
        {'id': 3, 'name': 'Item 3'},
    ]
}

# 获取所有项目
@app.route('/api/items', methods=['GET'])
def get_items():
    return jsonify(data)

# 获取特定项目
@app.route('/api/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in data['items'] if item['id'] == item_id), None)
    if item is None:
        return jsonify({'error': 'Item not found'}), 404
    return jsonify(item)

if __name__ == '__main__':
    app.run(debug=True)
