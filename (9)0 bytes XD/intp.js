const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question('Input code > ', (answer) => {
    if (code === '0') {
        console.log('0');
        return;
    } 
    if (code == '1') {
        while (true) {
            console.log('1');
        }
    }
    rl.close();
});