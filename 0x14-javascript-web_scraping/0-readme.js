#!/usr/bin/node

//a script that reads and prints the content of a file

const file_system = require('fs');
const file_name = process.argv[2];

file_system.readFile(file_name, 'utf-8', (error, content) => {
  if (error) {
    console.log(error);
  } else {
    console.log(content);
  }
});
