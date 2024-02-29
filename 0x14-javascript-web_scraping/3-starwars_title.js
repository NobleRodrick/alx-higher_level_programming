#!/usr/bin/node
//a script that prints the title of a Star Wars movie
//where the episode number matches a given integer

const request = require('request');
const movie_ID = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movie_ID}`;

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    console.log(data.title);
  }
});
