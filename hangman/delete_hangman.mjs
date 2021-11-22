import readline from 'readline';

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question("What's your name?", n => {
    console.log("Hello " + n);
    rl.close();
});

