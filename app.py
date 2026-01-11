from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

# Import functions from your existing calculator.py
try:
    from calculator import add, subtract, multiply, divide, power, log
except ImportError:
    print("Error: calculator.py not found!")
    print("Make sure calculator.py is in the same directory as app.py")
    exit(1)

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/')
def index():
    """Serve the HTML calculator"""
    return send_from_directory('.', 'calculator.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    """Handle calculator operations using functions from calculator.py"""
    try:
        data = request.get_json()
        operation = data.get('operation')
        num1 = float(data.get('num1'))
        num2 = float(data.get('num2'))
        
        # Call the appropriate function from calculator.py
        if operation == 'add':
            result = add(num1, num2)
        elif operation == 'subtract':
            result = subtract(num1, num2)
        elif operation == 'multiply':
            result = multiply(num1, num2)
        elif operation == 'divide':
            result = divide(num1, num2)
        elif operation == 'power':
            result = power(num1, num2)
        elif operation == 'log':
            result = log(num1, num2)
        else:
            return jsonify({'error': 'Invalid operation'}), 400
        
        # Handle error strings returned from calculator.py
        if isinstance(result, str) and result.startswith("Error"):
            return jsonify({'error': result}), 400
        
        # Round to avoid floating point errors
        if isinstance(result, (int, float)):
            result = round(result, 9)
        
        return jsonify({'result': result})
    
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

if __name__ == '__main__':
    print("\n" + "="*50)
    print("🚀 Calculator Backend Server")
    print("="*50)
    print("📁 Using functions from: calculator.py")
    print("🌐 Server running at: http://localhost:5000")
    print("💡 Press Ctrl+C to stop the server")
    print("="*50 + "\n")
    app.run(debug=True, port=5000)