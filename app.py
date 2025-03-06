from flask import Flask, send_file, render_template

app = Flask(__name__, template_folder="templates")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/robots.txt')
def robots():
    return send_file("robots.txt")

@app.route('/tvasecrets/')
def secret_file():
    return "<pre style='color: white; font-weight: bold;'>byteme{1t_w4s_r1ght_th3r3_1n_pl4in_s1ght}</pre>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
