// A static server with no dependencies.
//
//   node tools/serve.mjs          -> http://localhost:8080
//   node tools/serve.mjs 8123     -> the port is the first argument

import { createReadStream, realpathSync } from 'node:fs';
import { realpath, stat } from 'node:fs/promises';
import { createServer } from 'node:http';
import { extname, isAbsolute, join, relative, resolve, sep } from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';

const ROOT = fileURLToPath(new URL('..', import.meta.url));
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

function inside(root, path) {
  const suffix = relative(root, path);
  return suffix !== '..' && !suffix.startsWith('..' + sep) && !isAbsolute(suffix);
}

function reply(response, status, headers = {}) {
  response.writeHead(status, { 'content-type': TYPES['.txt'], ...headers }).end(String(status));
}

export function createStaticServer({ root = ROOT } = {}) {
  root = realpathSync(root);
  return createServer(async (request, response) => {
    if (!['GET', 'HEAD'].includes(request.method)) {
      reply(response, 405, { allow: 'GET, HEAD' });
      return;
    }
    let url;
    try {
      url = decodeURIComponent((request.url || '/').split('?')[0]);
    } catch {
      reply(response, 400);
      return;
    }
    if (!url.startsWith('/') || url.includes('\0')) {
      reply(response, 400);
      return;
    }
    let path = resolve(root, '.' + url);
    if (!inside(root, path)) {
      reply(response, 403);
      return;
    }
    try {
      path = await realpath(path);
      if (!inside(root, path)) { reply(response, 403); return; }
      let info = await stat(path);
      if (info.isDirectory()) {
        path = await realpath(join(path, 'index.html'));
        if (!inside(root, path)) { reply(response, 403); return; }
        info = await stat(path);
      }
      if (!info.isFile()) { reply(response, 404); return; }
      response.writeHead(200, {
        'content-type': TYPES[extname(path)] || 'application/octet-stream',
        'content-length': info.size,
        'cache-control': 'no-store',
      });
      if (request.method === 'HEAD') { response.end(); return; }
      const stream = createReadStream(path);
      stream.on('error', () => {
        if (response.headersSent) response.destroy();
        else reply(response, 500);
      });
      response.on('close', () => stream.destroy());
      stream.pipe(response);
    } catch (error) {
      const status = ['ENOENT', 'ENOTDIR'].includes(error.code) ? 404
        : ['EACCES', 'EPERM'].includes(error.code) ? 403 : 500;
      reply(response, status);
    }
  });
}

if (process.argv[1] && import.meta.url === pathToFileURL(resolve(process.argv[1])).href) {
  const port = Number(process.argv[2] || process.env.PORT || 8080);
  if (!Number.isInteger(port) || port < 0 || port > 65535) {
    console.error('port must be an integer between 0 and 65535');
    process.exitCode = 1;
  } else {
    const server = createStaticServer();
    server.on('error', (error) => { console.error(error.message); process.exitCode = 1; });
    server.listen(port, '0.0.0.0', () => {
      console.log(`masrouf on http://0.0.0.0:${server.address().port} (serving ${ROOT})`);
    });
  }
}
