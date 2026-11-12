from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    success = False
    error = None

    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        message = request.form.get("message", "").strip()

        if not name or not email or not message:
            error = "Semua field wajib diisi."
        else:
            # Form ini hanya menampilkan konfirmasi; data tidak disimpan.
            success = True

    return render_template("contact.html", success=success, error=error)


if __name__ == "__main__":
    app.run(debug=True)
