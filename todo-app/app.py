from flask import Flask, render_template, request, redirect, url_for, session
from flask_graphql import GraphQLView
from flask_sqlalchemy import SQLAlchemy
from keycloak import KeycloakOpenID
from schema import schema
import config

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)

keycloak_openid = KeycloakOpenID(
    server_url=config.KEYCLOAK_SERVER_URL,
    client_id=config.KEYCLOAK_CLIENT_ID,
    realm_name=config.KEYCLOAK_REALM_NAME,
    client_secret_key=config.KEYCLOAK_CLIENT_SECRET,
)

@app.route('/')
def home():
    if 'token' not in session:
        return redirect(url_for('login'))
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        try:
            token = keycloak_openid.token(username, password)
            session['token'] = token
            return redirect(url_for('home'))
        except:
            return 'Login Failed'
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('token', None)
    return redirect(url_for('login'))

app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

if __name__ == '__main__':
    app.run(debug=True)
