const http = require('http');
const fs = require('fs');
const path = require('path');
const url = require('url');

const PORT = 3000;
const STATIC_DIR = path.join(__dirname, 'odescomplicando.com');

const server = http.createServer((req, res) => {
  // Parse a URL
  const parsedUrl = url.parse(req.url, true);
  let pathname = parsedUrl.pathname;

  // Default to index.html
  if (pathname === '/' || pathname === '') {
    pathname = '/index.html';
  }

  // Get file path
  let filePath = path.join(STATIC_DIR, pathname);

  // Read file from disk
  fs.readFile(filePath, (err, content) => {
    if (err) {
      if (err.code === 'ENOENT') {
        // Try index.html if it's a directory
        const indexPath = path.join(filePath, 'index.html');
        fs.readFile(indexPath, (indexErr, indexContent) => {
          if (indexErr) {
            res.writeHead(404, { 'Content-Type': 'text/html' });
            res.end('<h1>404 - Página não encontrada</h1>');
          } else {
            res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8' });
            res.end(indexContent);
          }
        });
      } else {
        res.writeHead(500);
        res.end('Erro do servidor: ' + err);
      }
    } else {
      // Determine content type
      const ext = path.extname(filePath).toLowerCase();
      let contentType = 'text/plain';
      
      switch (ext) {
        case '.html': contentType = 'text/html; charset=utf-8'; break;
        case '.css': contentType = 'text/css; charset=utf-8'; break;
        case '.js': contentType = 'application/javascript; charset=utf-8'; break;
        case '.json': contentType = 'application/json; charset=utf-8'; break;
        case '.png': contentType = 'image/png'; break;
        case '.jpg':
        case '.jpeg': contentType = 'image/jpeg'; break;
        case '.gif': contentType = 'image/gif'; break;
        case '.svg': contentType = 'image/svg+xml'; break;
        case '.mp4': contentType = 'video/mp4'; break;
        case '.m3u': contentType = 'application/vnd.apple.mpegurl'; break;
        case '.txt': contentType = 'text/plain; charset=utf-8'; break;
      }

      res.writeHead(200, { 'Content-Type': contentType });
      res.end(content);
    }
  });
});

server.listen(PORT, () => {
  console.log(`\n✅ Servidor rodando em http://localhost:${PORT}`);
  console.log(`📂 Arquivos sendo servidos de: ${STATIC_DIR}\n`);
});
