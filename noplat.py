from flask import Flask, request, render_template_string
import csv
from datetime import datetime

app = Flask(__name__)

HTML_FORM = """
<!DOCTYPE html>
<html>
<head>
    <title>Makluman Kenderaan Murid Asrama</title>
    <style>
        body { font-family: Arial; background:#f2f2f2; padding:20px; }
        .box { background:white; padding:20px; border-radius:10px; }
        input, button { width:100%; padding:10px; margin-top:10px; }
        button { background:#4CAF50; color:white; border:none; }
    </style>
</head>
<body>
<div class="box">
<h2>Makluman Kenderaan Murid Asrama</h2>
<form method="post">
    <input name="nama" placeholder="Nama Murid" required>
    <input name="plat" placeholder="No Plat Kenderaan" required>
    <button type="submit">Hantar</button>
</form>
<p>{{ msg }}</p>
</div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def form():
    msg = ""
    if request.method == "POST":
        nama = request.form["nama"]
        plat = request.form["plat"]
        masa = datetime.now().strftime("%d/%m/%Y %H:%M")

        with open("data_murid.csv", "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([nama, plat, masa])

        msg = "Maklumat berjaya dihantar. Terima kasih."

    return render_template_string(HTML_FORM, msg=msg)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
