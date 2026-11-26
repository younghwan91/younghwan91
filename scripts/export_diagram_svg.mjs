// Export light/dark SVGs from an archify HTML via its viewer export menu.
// usage: ARCHIFY_CHROME=<chrome> node scripts/export_diagram_svg.mjs <diagram.html> <outPrefix>
import { spawn } from 'node:child_process';
import fs from 'node:fs';
import path from 'node:path';
import os from 'node:os';
const [html, outPrefix] = process.argv.slice(2);
const chrome = process.env.ARCHIFY_CHROME || 'chromium';
const udir = fs.mkdtempSync(path.join(os.tmpdir(), 'archify-chrome-'));
const port = 9300 + Math.floor(Math.random() * 500);
const p = spawn(chrome, ['--headless=new', '--no-sandbox', `--remote-debugging-port=${port}`, `--user-data-dir=${udir}`, '--window-size=1440,1000', 'about:blank'], { stdio: 'ignore' });
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
let ws;
for (let i = 0; i < 50; i++) {
  try { const t = await (await fetch(`http://127.0.0.1:${port}/json`)).json(); const pg = t.find((x) => x.type === 'page'); if (pg) { ws = pg.webSocketDebuggerUrl; break; } } catch {}
  await sleep(200);
}
const sock = new WebSocket(ws);
await new Promise((r) => sock.addEventListener('open', r));
let id = 0; const pend = new Map();
sock.addEventListener('message', (e) => { const m = JSON.parse(e.data); if (m.id && pend.has(m.id)) { pend.get(m.id)(m); pend.delete(m.id); } });
const send = (method, params = {}) => new Promise((r) => { const i = ++id; pend.set(i, r); sock.send(JSON.stringify({ id: i, method, params })); });
await send('Page.enable');
await send('Page.addScriptToEvaluateOnNewDocument', { source: `
  window.__captured = [];
  const oc = URL.createObjectURL; URL.createObjectURL = function(b){ window.__captured.push(b); return oc.call(URL,b); };
  HTMLAnchorElement.prototype.click = function(){};
` });
await send('Page.navigate', { url: 'file://' + path.resolve(html) });
await sleep(2500);
for (const fmt of ['svg-light', 'svg-dark']) {
  const r = await send('Runtime.evaluate', { awaitPromise: true, returnByValue: true, expression: `(async () => {
    window.__captured.length = 0;
    const b = document.querySelector('button[data-format="${fmt}"]');
    if (!b) return 'NO BUTTON';
    b.click();
    for (let i=0;i<50 && !window.__captured.length;i++) await new Promise(r=>setTimeout(r,100));
    const blob = window.__captured.find(x => /svg/.test(x.type)) || window.__captured[0];
    return blob ? await blob.text() : 'NO BLOB';
  })()` });
  const v = r.result?.result?.value;
  const out = `${outPrefix}-${fmt.replace('svg-', '')}.svg`;
  fs.writeFileSync(out, v);
  console.log(out, String(v).length, String(v).slice(0, 80));
}
sock.close(); p.kill(); await sleep(500); fs.rmSync(udir, { recursive: true, force: true, maxRetries: 5 });
