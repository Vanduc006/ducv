from http.server import SimpleHTTPRequestHandler as handler
from socketserver import TCPServer


httpd = TCPServer(('',1234),handler)
httpd.serve_forever()
