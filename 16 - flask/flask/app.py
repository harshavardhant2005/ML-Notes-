from flask import Flask,render_template,request,redirect,url_for
app = Flask(__name__)

@ app.route("/")
def welcome():
    return render_template("index.html")



@ app.route("/form",methods =["GET","POST"])
def form():
    if request.method == "POST":    
        name = request.form['username']
        return f"hello {name}"
    return render_template("form.html")


# variable rule as something that using a value in a url like result/60

@ app.route("/result/<int:score>")
def result(score):
    res=""
    if score >=50:
        res ="passed"
    else:
        res="FAILED"
    return render_template("result.html",score=score,result=res)

#jinga 2 template example:

@app.route("/result1/<int:score>")
def result1(score):
    res=""
    if score >=50:
        res ="passed"
    else:
        res="FAILED"
    exp ={
        "score":score,
        "res":res
    }
    return render_template("result1.html",result =exp)


@app.route("/resultif/<int:score>")
def resultif(score):
    return render_template("resultiff.html",score = score)

## dynamic url
@app.route("/finalresult",methods=["POST","GET"])
def evaluate():
    if request.method =="POST":
        science = float(request.form["science"])
        c = float(request.form["c"])
        ds = float(request.form["data science"])
        total=(science+c+ds)/3
        return redirect(url_for("result",score=total))
    else:
        return render_template("finalresult.html")

if __name__ == "__main__":
    app.run(debug= True)