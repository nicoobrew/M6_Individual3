from http.server import HTTPServer, BaseHTTPRequestHandler

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        self.wfile.write("Hola, bienvenidos".encode('UTF-8'))     
             
PORT = 8080
server = HTTPServer(('localhost', PORT), Handler)
print(f'“Servidor levantado mediante http.server en el puerto”, {PORT}')
server.serve_forever() # mantiene el servidor activo siempre