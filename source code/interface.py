from flask import Flask, render_template_string, request
import os

app = Flask(__name__)
LOG_FILE = "anomalies.log"

TEMPLATE = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>🛡️ IDS - Logs d'anomalies</title>
    <meta http-equiv="refresh" content="10">
    <style>
        body {
            background-color: #1e1e2f;
            color: #c5c6c7;
            font-family: 'Courier New', monospace;
            margin: 0;
            padding: 0;
        }
        .header {
            background-color: #0b0c10;
            padding: 20px;
            text-align: center;
            color: #66fcf1;
            font-size: 28px;
            border-bottom: 2px solid #45a29e;
        }
        .content {
            padding: 20px;
        }
        pre {
            background-color: #0b0c10;
            border: 1px solid #45a29e;
            border-radius: 8px;
            padding: 15px;
            overflow-x: auto;
            white-space: pre-wrap;
        }
        .search-bar {
            width: 100%;
            padding: 10px;
            margin-bottom: 10px;
            border: 2px solid #45a29e;
            background-color: #0b0c10;
            color: #66fcf1;
            border-radius: 5px;
            font-size: 16px;
        }
    </style>
</head>
<body>
    <div class="header">🧾 Journal des Anomalies - IDS</div>
    <div class="content">
        <form method="GET">
            <input type="text" name="search" class="search-bar" placeholder="Rechercher dans les logs..." value="{{ search_query }}">
        </form>
        <pre>{{ logs }}</pre>
    </div>
</body>
</html>
"""

@app.route('/', methods=['GET'])
def view_logs():
    search_query = request.args.get('search', '').lower()  # récupérer la recherche de l'utilisateur
    logs = ""
    
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, 'r') as f:
            all_logs = f.read()
            if search_query:  # filtrer les logs si une recherche est effectuée
                logs = '\n'.join([line for line in all_logs.split('\n') if search_query in line.lower()])
            else:
                logs = all_logs
    else:
        logs = "Aucune anomalie détectée pour le moment."

    return render_template_string(TEMPLATE, logs=logs, search_query=search_query)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

