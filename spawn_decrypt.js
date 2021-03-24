const {spawn} = require('child_process');

const SCRIPT = './python/dc_decrypt.py';
const SOURCE = '-- filename';
const ENCRYPTED_MESSAGE = "./encrypted_message";

const python = spawn('python', [SCRIPT, SOURCE, ENCRYPTED_MESSAGE]); // Will NOT work in Windows

python.stdout.on('data', (data) => {
    console.log(`Got data "${data.toString()}"`);
});

python.stderr.on('data', (data) => {
    console.log(`Error occurred: ${data}`);
})

python.on('exit', (code) => {
    console.log(`Exit code ${code}`);
});
