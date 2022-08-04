from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
# Used to encrypt passwords etc
app.config["SECRET_KEY"] = "password"
# Create instance of SocketIO class with argument of app instance
socketio = SocketIO(app)

print(__name__)

@app.route("/")
def root(name=None):
    return render_template("index.html")

# SocketIO handle events from client so server receives it
@socketio.on("connect")
def test_connect(auth):
    emit("my response", {"data": "Server connected to client"})

@socketio.on("disconnect")
def test_disconnect():
    print("Client disconnected")

@socketio.on("my event")
def client_response(json):
    print(json)

@socketio.on("chat message")
def recv_msg(msg):
    print(f"received message: {msg}")
    emit("chat message", msg, broadcast=True)

if __name__ == "__main__":
    socketio.run(app, debug=True)