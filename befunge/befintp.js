const fs = require('fs');
const Befunge = require('befunge93');

const filePath = process.argv[2];

if (!filePath) {
    console.log("Usage: node befintp.js <PATH-TO-FILE>");
    process.exit(1);
}

fs.readFile(filePath, 'utf8', (err, data) => {
    if (err) {
        console.error("Error reading file:", err);
        process.exit(1);
    }

    let befunge = new Befunge();

    befunge.run(data)
        .then((output) => {
            console.log(output);
        })
        .catch((err) => {
            console.error("Error running Befunge program:", err);
        });
});
