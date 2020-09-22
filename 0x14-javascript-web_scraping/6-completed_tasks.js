#!/usr/bin/node
const request = require('request');
const dt = {};

const options = {
  url: process.argv[2],
  method: 'GET'
};

request(options, (err, reponse, body) => {
  if (err) {
    return console.log(err);
  }
  for (const i of JSON.parse(body)) {
    const j = i.userId;
    dt[j] = 0;
  }
  for (const cn of JSON.parse(body)) {
    if (cn.completed) {
      dt[cn.userId] = dt[cn.userId] + 1;
    }
  }

  console.log(dt);
});
