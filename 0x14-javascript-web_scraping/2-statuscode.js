#!/usr/bin/node
//a script that displays the status code of a GET request.

const request = require('request');
const url = process.argv[2];

request.get(url, (error, response) => {
  if (error) {
    console.log(error);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
