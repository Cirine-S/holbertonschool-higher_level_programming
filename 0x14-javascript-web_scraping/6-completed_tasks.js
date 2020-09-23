#!/usr/bin/node
const request = require('request');

request(process.argv[2], (err, reponse, body) => {
  if (err) {
    console.log(err);
  }

  const DoneDict = {};
  const todos = JSON.parse(body);

  for (const i in JSON.parse(body)) {
    if (todos[i].completed) {
      if (DoneDict[todos[i].userId] === undefined) {
        DoneDict[todos[i].userId] = 0;
      }
      DoneDict[todos[i].userId]++;
    }
  }
  console.log(DoneDict);
});
