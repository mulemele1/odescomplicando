#!/usr/bin/env node

const http = require('http');
const fs = require('fs');
const path = require('path');
const url = require('url');
const mime = require('mime-types');

const PORT = 3000;
const STATIC_DIR = path.join(__dirname, 'odescomplicando.com');

const server = http.createServer((req, res) => {
  let pathname = url.parse(req.url).pathname;
  
  // Remove query string
  pathname = decodeURIComponent(pathname);
  
  // Default to index.html for root
  if (pathname === '/' || pathname === '') {
    pathname = '/index.html';
  }
  
  // Build full file path
  let filePath = path.join(STATIC_DIR, pathname.startsWith('/') ? pathname.slice(1) : pathname);
  
  // If it's a directory, try index.html
  try {
    const stats = fs.statSync(filePath);
    if (stats.isDirectory()) {
      filePath = path.join(filePath, 'index.html');
    }
  } catch (err) {
    // File doesn't exist, will be handled below
  }
  
  // Read and serve file
  fs.readFile(filePath, (err, content) => {
    // CORS headers
    res.setHeader('Access-Control-Allow-Origin', '*');
    res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
    res.setHeader('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0');
    
    if (err) {
      res.writeHead(404, { 'Content-Type': 'text/plain' });
      res.end('404 Not Found');
      console.log(`[${new Date().toISOString()}] 404 ${req.method} ${req.url}`);
      return;
    }
    
    // Set content type
    const contentType = mime.lookup(filePath) || 'application/octet-stream';
    res.writeHead(200, { 'Content-Type': contentType });
    res.end(content);
    console.log(`[${new Date().toISOString()}] 200 ${req.method} ${req.url}`);
  });
});

server.listen(PORT, () => {
  console.log(`\n✅ Servidor rodando em http://localhost:${PORT}`);
});
