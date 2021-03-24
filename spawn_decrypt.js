const {spawn} = require('child_process');

const encryptedMessage = "./encrypted_message";

const python = spawn('python', ['./python/dc_decrypt.py', encryptedMessage]); // Will NOT work in Windows

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
