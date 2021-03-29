const {spawn} = require('child_process');
const fs = require('fs');

exports.decryptFile = function(filename) {
    fs.readFile(filename, (err, data) => {
       if (err) {
           console.log(`Could not read file ${filename}`);
       }

       return this.decryptMessage(data);
    });
}

exports.decryptMessage = function(message) {
    const SCRIPT = './python/dc_decrypt.py';

    const python = spawn('python', [SCRIPT, message]); // Will NOT work in Windows

    python.stdout.on('data', (data) => {
        return (data.toString());
    });

    python.stderr.on('data', (data) => {
        console.log(`Error occurred: ${data}`);
    })

    python.on('exit', (code) => {
        console.log(`Exit code ${code}`);
    });
}

exports.encryptObject = function(message) {
    const SCRIPT = './python/dc_encrypt.py';
    const python = spawn('python', [SCRIPT , message]); // Will NOT work in Windows

    python.stdout.on('data', (data) => {
        return data.toString;
    });

    python.stderr.on('data', (data) => {
        console.log(`Error occurred: ${data}`);
    })

    python.on('exit', (code) => {
        console.log(`Exit code ${code}`);
    });
}