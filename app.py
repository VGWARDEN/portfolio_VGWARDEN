from flask import Flask, request, render_template

app = Flask(__name__)

# Function to get the real IP address of the user
def get_real_ip():
    if 'X-Forwarded-For' in request.headers:
        ip = request.headers['X-Forwarded-For'].split(',')[0]
    else:
        ip = request.remote_addr
    return ip

@app.route('/')
def index():
    ip = get_real_ip()
    return render_template('index.html', ip=ip)

@app.route('/Discord')
def Discord():
    return render_template('Discord.html')



if __name__ == '__main__':
    app.run(debug=True)
