#!/usr/bin/node
const request = require('request');
const fs = require('fs');

request(process.argv[2], (err, response, body) => {
  if (err) {
    console.log(err);
  }

  fs.writeFile(process.argv[3], body, { flag: 'w' }, err => {
    if (err) { console.log(err); }
  });
});
