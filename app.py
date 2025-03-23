from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/parent-child', methods=['POST'])
def parent_child():
    
    # Retrieves the JSON payload sent in the POST request body
    request_data = request.get_json()

    # Process each parent object and assign parentId to children
    for key, value in request_data.items():
        if isinstance(value, dict) and 'parentId' in value and 'children' in value:
            for child in value['children']:
                child['parentId'] = value['parentId']  # Assign parentId to child

    return jsonify({
        'message': "Parent and children data processed successfully",
        **request_data  # Return the modified data structure directly
    }), 201

if __name__ == '__main__':
    app.run(port=5001, debug=True)
