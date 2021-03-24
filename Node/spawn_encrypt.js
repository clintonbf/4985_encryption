import {ENCRYPT_SCRIPT} from "./resources";

const {spawn} = require('child_process');

const object = {
    "name": "Clint",
    "profession": "Student",
    "program": "CST"
};

const DATA_TO_ENCRYPT = JSON.stringify(object);

const python = spawn('python', [ENCRYPT_SCRIPT, DATA_TO_ENCRYPT]); // Will NOT work in Windows
let dataToSend;

python.stdout.on('data', (data) => {
    console.log(`Got data "${data.toString()}"`);
    dataToSend = data.toString();
});

python.stderr.on('data', (data) => {
    console.log(`Error occurred: ${data}`);
})

python.on('exit', (code) => {
    console.log(`Exit code ${code}`);
});
