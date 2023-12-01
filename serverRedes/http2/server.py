import http.server
import ssl
import h2.connection
import h2.events

class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"Hello, HTTP/2!")

def run(server_class=http.server.HTTPServer, handler_class=MyHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)

    httpd.socket = ssl.wrap_socket(httpd.socket, keyfile="/home/helias/embarcados2023/chave_privada.key", certfile="/home/helias/embarcados2023/certificate.crt", server_side=True, ssl_version=ssl.PROTOCOL_TLS)

    print(f"Starting server on port {port}")
    httpd.serve_forever()

if __name__ == '__main__':
    run()
