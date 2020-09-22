#!/usr/bin/node
const request = require('request');
const fs = require('fs');

const options = {
  url: process.argv[2],
  method: 'GET'
};

request(options, (err, reponse, body) => {
  if (err) {
    return console.log(err);
  }

  fs.writeFile(process.argv[3], body,
    {
      encoding: 'utf8',
      flag: 'w'
    },
    (err) => {
      if (err) { console.log(err); }
    });
});