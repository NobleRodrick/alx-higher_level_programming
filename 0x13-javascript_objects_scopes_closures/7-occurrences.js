#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let occurrenceNumber = 0;
  for (let i = 0; i < list.length; i++) {
    if (searchElement === list[i]) {
      occurrenceNumber++;
    }
  }
  return occurrenceNumber;
};
