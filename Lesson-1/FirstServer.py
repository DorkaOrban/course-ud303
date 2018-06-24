#!/usr/bin/env python3
#
# The *first server* is an HTTP server that responds to a GET request by
# sending back a friendly greeting.  Run this program in your terminal and
# access the server at http://localhost:7000 in your browser.

from http.server import HTTPServer, BaseHTTPRequestHandler


class FirstHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # First, send a 307 redirect response.
        self.send_response(301)

        # Then send headers.
        self.send_header('Location','https://www.youtube.com/watch?v=MQXLpSl26q4')
        self.end_headers()


if __name__ == '__main__':
    server_address = ('', 7000)  # Serve on all addresses, port 8000.
    httpd = HTTPServer(server_address, FirstHandler)
    httpd.serve_forever()
