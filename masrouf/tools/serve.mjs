// A static server with no dependencies.
//
//   node tools/serve.mjs          -> http://localhost:8080
//   node tools/serve.mjs 8123     -> the port is the first argument

import { createReadStream, existsSync, statSync } from 'node:fs';
import { createServer } from 'node:http';
import { extname, join, normalize, resolve } from 'node:path';

const port = Number(process.argv[2] || process.env.PORT || 8080);
const root = resolve(new URL('..', import.meta.url).pathname);

const TYPES = {
  '.html': 'text/html; charset=utf-8',
  '.css': 'text/css; charset=utf-8',
  '.mjs': 'text/javascript; charset=utf-8',
  '.js': 'text/javascript; charset=utf-8',
  '.json': 'application/json; charset=utf-8',
  '.svg': 'image/svg+xml',
  '.png': 'image/png',
  '.ico': 'image/x-icon',
  '.txt': 'text/plain; charset=utf-8',
};

const server = createServer((request, response) => {
  const url = decodeURIComponent((request.url || '/').split('?')[0]);
  const wanted = normalize(url).replace(/^(\.\.[/\\])+/, '');
  let path = join(root, wanted);
  if (!path.startsWith(root)) {
    response.writeHead(403).end('no');
    return;
  }
  if (existsSync(path) && statSync(path).isDirectory()) path = join(path, 'index.html');
  if (!existsSync(path)) {
    response.writeHead(404, { 'content-type': TYPES['.txt'] }).end('404');
    return;
  }
  response.writeHead(200, {
    'content-type': TYPES[extname(path)] || 'application/octet-stream',
    'cache-control': 'no-store',
  });
  createReadStream(path).pipe(response);
});

server.listen(port, '0.0.0.0', () => {
  console.log(`masrouf on http://localhost:${port} (serving ${root})`);
});
