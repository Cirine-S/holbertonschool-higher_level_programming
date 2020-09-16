#!/usr/bin/node
if (! process.argv[2]) {
console.log('Missing size')
} else {
    for (i = 0; i < process.argv[2]; i++) {
        let square = '';
        for (j = 0; j < process.argv[2]; j++) {
            square += 'X';
        }
        console.log(square);
    }
}
