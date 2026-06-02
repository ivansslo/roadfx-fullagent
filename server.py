# server.py
# Script tambahan untuk mengarahkan host:port langsung ke halaman Arena Agent Mode

import http.server
import socketserver
import sys

# Default port
PORT = 8080 if len(sys.argv) < 2 else int(sys.argv[1])

class ArenaAgentRedirectHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Mengarahkan default path '/' ke 'index.html' secara langsung
        if self.path == '/' or self.path == '/index.html':
            self.path = '/index.html'
        return super().do_GET()

# Meluncurkan TCP server
handler = ArenaAgentRedirectHandler

with socketserver.TCPServer(("", PORT), handler) as httpd:
    print("-" * 65)
    print(f"🚀 Arena.ai - Agent Mode Server berjalan!")
    print(f"🔗 Buka browser Anda dan kunjungi: http://localhost:{PORT}")
    print("-" * 65)
    print("Tekan Ctrl+C untuk menghentikan server.\n")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping server...")
        httpd.server_close()
        print("Server stopped.")
