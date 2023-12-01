from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('template.html')

@app.route('/metrics', methods=['POST'])
def metrics():
    try:
        data = request.get_json()
        # Assuming the JSON request has a key named 'metrics_data'
        metrics_data = data.get('distance_cm', {})

        # Do something with metrics_data
        # For demonstration purposes, let's just print it
        print("Received Metrics Data:", metrics_data)

        # You can process the data further and return a response if needed
        response = {'distance': metrics_data, 'status': 'success', 'message': 'Metrics data received successfully'}
        return jsonify(response), 200
    except Exception as e:
        error_message = f"Error processing metrics: {str(e)}"
        print(error_message)
        return jsonify({'status': 'error', 'message': error_message}), 500

if __name__ == '__main__':
    app.run(debug=True)
