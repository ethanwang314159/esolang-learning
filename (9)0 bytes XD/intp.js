const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question('What is your favorite color? ', (answer) => {
    console.log(`Your favorite color is: ${answer}`);
    rl.close();
});