from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')  # definir les routes en l'occurence la route principale
def page1():  # definir la fonction
    return render_template("index1.html")


@app.route('/Acceuil')
def page2():
    return render_template("index2.html")


@app.route('/base')
def page_base():
    return render_template("base.html")


@app.route('/Liste_Mag')
def page3():
    return render_template("index3.html")


@app.route('/Ajout_Mag')
def page4():
    return render_template("index4.html")


@app.route('/Save_Mag')
def page5():
    return render_template("index5.html")


@app.route('/Modif_Mag')
def page6():
    return render_template("index6.html")


@app.route('/List_Mod')
def page7():
    return render_template("index7.html")


@app.route('/Sup_Mag')
def page8():
    return render_template("index8.html")


@app.route('/List_Sup')
def page9():
    return render_template("index9.html")


if __name__ == "__main__":  # Pour que la methode créée puisse s'éxécutée
    app.run(debug=True)
