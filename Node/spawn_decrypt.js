import {DECRYPT_SCRIPT} from "./resources";
import {ENCRYPTED_MESSAGE} from "./resources";

const {spawn} = require('child_process');

const SOURCE = '-- filename';

const python = spawn('python', [DECRYPT_SCRIPT, SOURCE, ENCRYPTED_MESSAGE]); // Will NOT work in Windows

python.stdout.on('data', (data) => {
    console.log(`Got data "${data.toString()}"`);
});

python.stderr.on('data', (data) => {
    console.log(`Error occurred: ${data}`);
})

python.on('exit', (code) => {
    console.log(`Exit code ${code}`);
});
