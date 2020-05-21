# Python Websocket Example

This repository demonstrates a simple use case of
* How to make a simple websocket server
* How to make an asynchronous websocket client that can be used from synchronous code

The websocket server is not difficult and can be built from examples of the Tornado library. The websocket client, however, is rather tricky as it involves `asyncio` event loops being managed across threads. After struggling to get it to work just right, I've made this example to serve as a reminder of how to do it.

### Server
The server is simply an echo server. It accepts all connections on `ws://localhost:8080/socket`. Whenever it receives a message, it simply echos that message back to all clients connected to it (along with printing to the console).

### Client
There is an abstract client that can be overwritten with advanced behavior. I provide a simple implementation that just prints all messages it receives from the socket to the console.

## Running
* Make sure the requirements are installed
```
pip install -r requirements.txt
```
* In one terminal, start the server
```
python server.py
```
* In a second terminal, run the client
```
python client.py
```
In the client terminal, you can then type messages to send to the server (which will be echoed back). You can type "kill" to kill the client.
