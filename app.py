from http.server import HTTPServer, BaseHTTPRequestHandler

class MyApp(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"woohooooo hooray Hello! Jenkins CI/CD Pipeline is working! congrats , sakshiiii redhu")

server = HTTPServer(("0.0.0.0", 5000), MyApp)
print("Application running on port 5000 ")
server.serve_forever()
