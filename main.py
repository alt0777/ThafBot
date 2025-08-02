from flask import Flask, request, render_template
from datetime import datetime

app = Flask(__name__)

nama1 = ""

def contains(text, keywords):
    return any(word in text.lower() for word in keywords)

@app.route("/", methods=["GET", "POST"])
def home():
    global nama1
    response = ""
    if request.method == "POST":
        input_user = request.form["input_user"]

        if contains(input_user, ["siapa"]) and contains(input_user, ["kamu", "kau", "anda", "you", "lu", "loe", "lo"]):
            response = "Aku ThafBot, Chatbot yang sedang dikembangkan oleh Althaf. Salam kenal ya!"
        elif contains(input_user, ["halo", "helo", "hello", "hallo"]):
            response = "Halo juga! Senang bisa disapa olehmu ^_^."
        elif contains(input_user, ["hai", "hi", "hei", "hey", "hay"]):
            response = "Hai juga! Disapa oleh mu membuatku senang ^_^."
        elif contains(input_user, ["namaku", "nama saya", "nama ku", "nama aku", "namaku adalah", "nama ku adalah", "nama saya adalah"]):
            nama1 = input_user.split()[-1]
            response = f"{nama1}, Wah... Nama yang keren. Aku akan mengingatnya."
        elif contains(input_user, ["siapa"]) and contains(input_user, ["aku", "diriku", "saya"]):
            if nama1:
                response = f"Namamu adalah {nama1}, aku tidak akan melupakannya."
            else:
                response = "Aku belum mengetahui namamu. Oh... bisakah kamu katakan namamu kepada ku?"
        elif contains(input_user, ["cuaca"]) and contains(input_user, ["perkiraan", "hari ini", "saat ini", "sekarang"]):
            response = "Aku tidak bisa mengakses internet, tapi aku bisa katakan bahwa cuacanya akan selalu cerah untuk mu ^_^"
        elif contains(input_user, ["jam", "waktu"]) and contains(input_user, ["saat ini", "sekarang", "kini", "tunjukkan", "tampilkan"]):
            response = "Waktu sekarang adalah " + datetime.now().strftime("%H:%M:%S")
        elif contains(input_user, ["tanggal", "kalender"]) and contains(input_user, ["hari ini", "saat ini", "sekarang", "berapa sekarang", "berapa"]):
            response = "Tanggal sekarang adalah " + datetime.now().strftime("%d-%m-%Y")
        elif contains(input_user, ["bantuan"]):
            response = "Aku dapat mengerti soal: Nama, halo, cuaca, waktu, tanggal. Aku akan terus dikembangkan."
        else:
            response = "Maaf... aku tidak mengerti. Ketik 'Bantuan' untuk melihat perintah yang bisa kupahami."

    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)