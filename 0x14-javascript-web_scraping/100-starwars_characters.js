#!/usr/bin/node
const request = require('request');

request('https://swapi-api.hbtn.io/api/films/' + process.argv[2], (err, response, body) => {
  if (err) {
    console.log(err);
  }
  for (const i in JSON.parse(body).characters) {
    request(JSON.parse(body).characters[i], (err, response, body) => {
      if (err) {
        return console.log(err);
      }
      console.log(JSON.parse(body).name);
    });
  }
});
