#!/usr/bin/node
const { argv } = require('node:process');

if (!argv[0]) {
	console.log('No argument');
}
else {
	console.log('Argument found');
}
