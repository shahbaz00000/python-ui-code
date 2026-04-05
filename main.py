from flask import Flask, render_template_string

app = Flask(__name__)

# Single-file HTML UI
HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>DevOps Dashboard</title>
<link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
</head>
<body class="bg-gray-900 text-white">

<div class="flex">
    <!-- Sidebar -->
    <div class="w-64 h-screen bg-gray-800 p-5">
        <h2 class="text-2xl font-bold mb-6 text-blue-400">⚙️ DevOps</h2>
        <ul>
            <li class="mb-4 hover:text-blue-400 cursor-pointer">CI/CD</li>
            <li class="mb-4 hover:text-blue-400 cursor-pointer">Docker</li>
            <li class="mb-4 hover:text-blue-400 cursor-pointer">Kubernetes</li>
            <li class="mb-4 hover:text-blue-400 cursor-pointer">Monitoring</li>
            <li class="mb-4 hover:text-blue-400 cursor-pointer">Logs</li>
        </ul>
    </div>

    <!-- Main Content -->
    <div class="flex-1 p-10">
        <h1 class="text-3xl font-bold text-blue-400 mb-6">🚀 DevOps Dashboard</h1>

        <!-- Cards -->
        <div class="grid grid-cols-4 gap-6">
            <div class="bg-gray-800 p-5 rounded-xl shadow">
                <p class="text-gray-400">Containers</p>
                <h2 class="text-2xl">12</h2>
            </div>
            <div class="bg-gray-800 p-5 rounded-xl shadow">
                <p class="text-gray-400">Deployments</p>
                <h2 class="text-2xl">5</h2>
            </div>
            <div class="bg-gray-800 p-5 rounded-xl shadow">
                <p class="text-gray-400">CPU Usage</p>
                <h2 class="text-2xl">68%</h2>
            </div>
            <div class="bg-gray-800 p-5 rounded-xl shadow">
                <p class="text-gray-400">Errors</p>
                <h2 class="text-2xl text-red-400">2</h2>
            </div>
        </div>

        <!-- Section -->
        <div class="mt-10 bg-gray-800 p-6 rounded-xl">
            <h2 class="text-xl mb-4">System Status</h2>
            <p class="text-green-400">✔ All systems operational</p>
        </div>
    </div>
</div>

</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
