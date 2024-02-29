#!/usr/bin/node
//a script that prints the number of movies where
//the character “Wedge Antilles” is present
//its the character ID 18

const request = require('request');
const url = process.argv[2];
const character_ID = '18';
let count_number = 0;

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    data.results.forEach((film) => {
      film.characters.forEach((character) => {
        if (character.includes(character_ID)) {
          count_number += 1;
        }
      });
    });
    console.log(count_number);
  }
});
