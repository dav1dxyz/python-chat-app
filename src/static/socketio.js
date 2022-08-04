let socket = io();

let messages = document.getElementById("msgs"); // msgs unordered list
let button = document.getElementById("button"); // button to do stuff

// Socket.IO stuff
socket.on("connect", () => {
    socket.emit("my event", {data: "Client connected to server"});
});

socket.on("disconnect", () => {
    socket.emit("my event", {data: "Client disconnected from server"})
});

socket.on("my response", (msg) => {
    console.log("received: ", msg);
});

// message received from server to client (msg)
socket.on("chat message", (msg) => {
    console.log(msg); 

    let ul = document.getElementById("messages");
    let li = document.createElement("li");
    li.appendChild(document.createTextNode(msg));
    ul.appendChild(li);
});

function text() {
    // message sent from client to server (value)
    let value = document.getElementById("textbox").value;
    socket.emit("chat message", value);
}