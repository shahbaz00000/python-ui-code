from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>DevOps Dashboard</title>
    <style>
        body { background:#0f172a; color:white; font-family:Arial; }
        .card { background:#1e293b; padding:20px; margin:10px; border-radius:10px; display:inline-block; }
    </style>
</head>
<body>
    <h1>🚀 DevOps Dashboard</h1>
    <div class="card">Containers: 12</div>
    <div class="card">CPU Usage: 68%</div>
    <div class="card">Deployments: 5</div>
    <div class="card">Errors: 2</div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
