#!/usr/bin/env python
"""
    A simple echo websocket server
"""
import asyncio

import tornado.ioloop
import tornado.web
import tornado.websocket


WS_PORT = 8080


class EchoSocket(tornado.websocket.WebSocketHandler):
    """ An websocket server that echos all messages back to all clients """

    clients = set()

    async def open(self):
        print('Client connected')
        type(self).clients.add(self)

    def on_close(self):
        type(self).clients.remove(self)
        print('Client disconnected')

    async def on_message(self, message):
        asyncio.create_task(self.print_message(message))
        asyncio.create_task(self.echo_message(message))

    async def print_message(self, message):
        print("Received message:", message)

    @classmethod
    async def echo_message(cls, message):
        for client in cls.clients:
            try:
                client.write_message(message)
                print("Echoed message:", message)
            except Exception as e:
                print('Error echoing message:', e)


def main():
    handlers = [
        (r'/socket', EchoSocket)
    ]
    app = tornado.web.Application(
        handlers,
        websocket_ping_interval=30,
        xsrf_cookies=False
    )
    app.listen(WS_PORT)
    tornado.ioloop.IOLoop.current().start()


if __name__ == '__main__':
    main()
