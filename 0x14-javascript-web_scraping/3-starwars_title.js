#!/usr/bin/node
const request = require('request');

request('https://swapi-api.hbtn.io/api/films/' + process.argv[2], (err, reponse, body) => {
  if (err) {
    return console.log(err);
  }
  console.log(JSON.parse(body).title);
});
