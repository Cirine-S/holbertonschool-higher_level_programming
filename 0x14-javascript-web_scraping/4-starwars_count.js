#!/usr/bin/node
const request = require('request');
let sum = 0;

request(process.argv[2], (err, response, body) => {
  if (err) {
    console.log(process.argv[2]);
  }
  for (const i of JSON.parse(body).results) {
    for (const j of i.characters) {
      if (j.search('api/people/18/') > 0) {
        sum += 1;
      }
    }
  }
  console.log(sum);
});
