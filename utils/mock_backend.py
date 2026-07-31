import http.server
import socketserver
import json
import re

PORT = 3001

class MockBackendHandler(http.server.BaseHTTPRequestHandler):
    # Quiet console logging
    def log_message(self, format, *args):
        pass

    def do_GET(self):
        self._route()

    def do_POST(self):
        self._route()

    def do_PATCH(self):
        self._route()

    def _route(self):
        # Allow CORS
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Headers", "*")
        self.send_header("Access-Control-Allow-Methods", "*")
        self.end_headers()

        path = self.path.split("?")[0]
        
        response_data = {
            "success": True,
            "message": "Mock operation successful",
            "data": {
                "id": "mock-id-12345",
                "email": "doctor@cognitest.com",
                "role": "doctor",
                "score": 95,
                "status": "COMPLETED",
                "grade": "NORMAL",
                "riskLevel": "LOW",
                "response": "Clinical MRI analysis complete: No hippocampal atrophy detected."
            }
        }
        
        self.wfile.write(json.dumps(response_data).encode("utf-8"))

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Headers", "*")
        self.send_header("Access-Control-Allow-Methods", "*")
        self.end_headers()

def main():
    # Use ThreadingTCPServer to handle concurrent requests under load testing
    class ThreadingTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
        allow_reuse_address = True
        
    with ThreadingTCPServer(("", PORT), MockBackendHandler) as httpd:
        print(f"🚀 Started Mock Backend Server on port {PORT}")
        httpd.serve_forever()

if __name__ == "__main__":
    main()
