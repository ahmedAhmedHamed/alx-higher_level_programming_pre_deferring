#!/usr/bin/node
import { argv } from 'node:process';
if (argv[2] && !argv[3]) {
  console.log('Argument found');
} else if (argv[2] && argv[3]) {
  console.log('Arguments found');
} else {
  console.log('No argument');
}
