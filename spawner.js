const {spawn} = require('child_process');

const object = {
    "name": "Clint",
    "profession": "Student",
    "program": "CST"
};

const python = spawn('python', ['./external/dc_encrypt.py', JSON.stringify(object)]); // Will NOT work in Windows
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