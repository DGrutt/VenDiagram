#!flask/bin/python
import flask, flask.views
import os


app = flask.Flask(__name__)
app.secret_key = "44asdfkhsdfkj1s1h3w45254235423"

class View(flask.views.MethodView):
    def get(self):
        return flask.render_template('index.html')
        
    def post(self):
        A = unicode(flask.request.form['A'])
        B = unicode(flask.request.form['B'])
        C = A.split()
        D = B.split()
        Both = []
        for x in C:
            if x in D:
                Both.append(x)
        for x in range(len(Both)):
            Both[x]=str(Both[x])
        Final = []
        for x in set(Both):
            Final.append(x)
        MissingA = []
        for x in C:
            if x not in Final and x not in MissingA:
                MissingA.append(x)
        for x in range(len(MissingA)):
            MissingA[x]=str(MissingA[x])
        MissingB = []
        for x in D:
            if x not in Final and x not in MissingB:
                MissingB.append(x)
        for x in range(len(MissingB)):
            MissingB[x]=str(MissingB[x])
        #flask.flash("A:")
        #flask.flash(A)
        #flask.flash("B:")
        #flask.flash(B)
        #flask.flash("C:")
        #flask.flash(C)
        #flask.flash("D:")
        #flask.flash(D)
        flask.flash("Words in Both:")
        flask.flash(Final)
        flask.flash("Words in First Box Only:")
        flask.flash(MissingA)
        flask.flash("Words in Second Box Only:")
        flask.flash(MissingB)
        return self.get()
    
app.add_url_rule('/', view_func=View.as_view('main'), methods=['GET', 'POST'])

app.debug = True
if __name__ == "__main__":
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
