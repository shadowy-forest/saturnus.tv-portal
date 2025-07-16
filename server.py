import os
from http.server import HTTPServer, SimpleHTTPRequestHandler


class CustomHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if not os.path.exists(self.translate_path(self.path)):
            self.path = '/404.html'
        return SimpleHTTPRequestHandler.do_GET(self)

def run(server_class=HTTPServer, handler_class=CustomHandler, port=8137):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"💎 starting server on port {port}...")
    httpd.serve_forever()

if __name__ == '__main__':
    run() 
