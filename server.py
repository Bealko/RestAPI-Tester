import http.server
import socketserver
import time
import os

PORT = 8000
#optional directory allocation
#DIRECTORY = "web"


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=os.getcwd(), **kwargs)


if __name__ == "__main__":  
    with http.server.HTTPServer(("", PORT), Handler) as httpd:
        
        print("Serving at port: ", PORT)
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            pass

        httpd.server_close()
        print("Server stopped.")