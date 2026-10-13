import test, { after, before } from 'node:test';
import assert from 'node:assert/strict';
import { mkdtemp, mkdir, rm, symlink, writeFile } from 'node:fs/promises';
import { request } from 'node:http';
import { tmpdir } from 'node:os';
import { join } from 'node:path';

import { createStaticServer } from '../tools/serve.mjs';

let folder;
let root;
let server;
let port;
const HTML = '<h1>Test page</h1>\n';

before(async () => {
  folder = await mkdtemp(join(tmpdir(), 'masrouf-server-'));
  root = join(folder, 'site with spaces');
  await mkdir(root);
  await mkdir(join(root, 'empty'));
  await writeFile(join(root, 'index.html'), HTML);
  await writeFile(join(root, 'code.mjs'), 'export const ok = true;\n');
  await writeFile(join(root, 'file with spaces.txt'), 'spaces work\n');
  await writeFile(join(folder, 'outside.txt'), 'outside the site\n');
  server = createStaticServer({ root });
  await new Promise((resolve, reject) => {
    server.once('error', reject);
    server.listen(0, '0.0.0.0', resolve);
  });
  port = server.address().port;
});

after(async () => {
  if (server) await new Promise((resolve) => server.close(resolve));
  if (folder) await rm(folder, { recursive: true, force: true });
});

function fetchPath(path, method = 'GET') {
  return new Promise((resolve, reject) => {
    const req = request({ hostname: '127.0.0.1', port, path, method, agent: false }, (res) => {
      const chunks = [];
      res.on('data', (chunk) => chunks.push(chunk));
      res.on('error', reject);
      res.on('end', () => resolve({ status: res.statusCode, headers: res.headers, body: Buffer.concat(chunks).toString() }));
    });
    req.on('error', reject);
    req.end();
  });
}

test('serves index pages and JavaScript with their MIME types', async () => {
  const page = await fetchPath('/?ignored=%ZZ');
  assert.equal(page.status, 200);
  assert.equal(page.body, HTML);
  assert.match(page.headers['content-type'], /^text\/html/);
  const script = await fetchPath('/code.mjs');
  assert.equal(script.status, 200);
  assert.match(script.headers['content-type'], /^text\/javascript/);
});

test('HEAD sends the same headers without a response body', async () => {
  const response = await fetchPath('/', 'HEAD');
  assert.equal(response.status, 200);
  assert.equal(response.headers['content-length'], String(Buffer.byteLength(HTML)));
  assert.equal(response.body, '');
});

test('encoded filenames are decoded correctly', async () => {
  const response = await fetchPath('/file%20with%20spaces.txt');
  assert.equal(response.status, 200);
  assert.equal(response.body, 'spaces work\n');
});

test('malformed escapes and NUL paths return 400 without killing the server', async () => {
  for (const path of ['/%ZZ', '/%00']) assert.equal((await fetchPath(path)).status, 400);
  assert.equal((await fetchPath('/')).status, 200);
});

test('missing files and directories without an index return 404', async () => {
  for (const path of ['/missing', '/empty/']) assert.equal((await fetchPath(path)).status, 404);
});

test('traversal cannot leave the serving directory', async () => {
  for (const path of ['/../outside.txt', '/..%2Foutside.txt']) {
    const response = await fetchPath(path);
    assert.equal(response.status, 403);
    assert.ok(!response.body.includes('outside the site'));
  }
});

test('symlinks cannot expose files outside the serving directory', async (context) => {
  try {
    await symlink(join(folder, 'outside.txt'), join(root, 'link.txt'));
  } catch (error) {
    if (error.code === 'EPERM') { context.skip('symlinks unavailable'); return; }
    throw error;
  }
  const response = await fetchPath('/link.txt');
  assert.equal(response.status, 403);
  assert.ok(!response.body.includes('outside the site'));
});

test('unsupported methods are rejected explicitly', async () => {
  const response = await fetchPath('/', 'POST');
  assert.equal(response.status, 405);
  assert.equal(response.headers.allow, 'GET, HEAD');
});
