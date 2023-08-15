from flask import Flask, jsonify, request

app = Flask(__name__)

# Define a route for the API
@app.route('/')
def index():
    return 'Welcome to the api'

# Define a route for retrieving a list of resources
@app.route('/resources')
def get_resources():
    resources = ['resource1', 'resource2', 'resource3']
    return jsonify(resources)

# Define a route of retrieving a single resource by ID
@app.route('/resources/<int:id>')
def get_resource(id):
    resources = r'Resource with ID {id}'
    return resources

# Define route for creating a new resource
@app.route('/resources', methods=['POST'])
def creating_resource():
    data = request.json
    print("Receive data: ", data)
    return 'Resource created successfully'

# Define a route for updating an existing resource
@app.route('/resources /<int:id>', methods=['PUT'])
def update_resource(id):
    data = request.json
    print(f'Updating resource with ID {id} and data', data)
    return f"Resource with ID {id} updated successfully"

# Define a route for deleting a resource by ID
@app.route('/resources/<int:id>', methods=['DELETE'])
def delete_resource(id):
    print(f"Deleting resources with ID {id}")
    return f"Resource with ID {id} deleted successfully"

# Start the server and listens for incoming requests
if __name__ == '__main__':
    app.run(debug=True)