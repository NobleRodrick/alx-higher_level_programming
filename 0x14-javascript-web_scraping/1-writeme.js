#!/usr/bin/node
//a script that writes a string to a file.

const file_system = require('fs');
const filename = process.argv[2];
const content = process.argv[3];

file_system.writeFile(filename, content, 'utf-8', (error) => {
  if (error) {
    console.log(error);
  }
});
