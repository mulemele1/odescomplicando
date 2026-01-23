#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import http.server
import socketserver
import os
import mimetypes
from pathlib import Path
from urllib.parse import unquote, urlparse

PORT = 3000
STATIC_DIR = os.path.join(os.path.dirname(__file__), 'odescomplicando.com')

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def translate_path(self, path):
        # Parse URL
        path = unquote(path)
        
        # Remove query string
        if '?' in path:
            path = path.split('?')[0]
        
        # Default to index.html for root
        if path == '/' or path == '':
            path = '/index.html'
        
        # Build full file path
        file_path = os.path.join(STATIC_DIR, path.lstrip('/'))
        
        # If it's a directory, try index.html
        if os.path.isdir(file_path):
            file_path = os.path.join(file_path, 'index.html')
        
        return file_path
    
    def end_headers(self):
        # Add CORS headers
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
        super().end_headers()
    
    def log_message(self, format, *args):
        print(f'[{self.log_date_time_string()}] {format % args}')

if __name__ == '__main__':
    os.chdir(os.path.dirname(__file__))
    
    with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
        print(f'\n✅ Servidor rodando em http://localhost:{PORT}')
        print(f'📂 Arquivos sendo servidos de: {STATIC_DIR}\n')
        print('Pressione CTRL+C para parar o servidor...\n')
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print('\n\n❌ Servidor parado.')
