//N.B. this will NOT work on Windows

const {spawn} = require('child_process');
const fs = require('fs');

const PYTHON_PATH = '../../python';
const ENCRYPT_SCRIPT = PYTHON_PATH + '/dc_encrypt.py';
const DECRYPT_SCRIPT = PYTHON_PATH + '/dc_decrypt.py';

/**
 * Decrypts an encrypted file.
 *
 * @param {string} filename file to encrypt. Include path.
 * @return {string} the file contents decrypted.
 */
exports.decryptFile = function(filename) {
    fs.readFile(filename, (err, data) => {
       if (err) {
           console.log(`Could not read file ${filename}`);
       }

       return this.decryptMessage(data);
    });
}

/**
 * Decrypts a message.
 *
 * @param {string} message encrypted message
 * @return {string} decrypted message. Returns null if there was an error or an exit (whatever that is)
 */
exports.decryptMessage = function(message) {
    const python = spawn('python', [DECRYPT_SCRIPT, message]);

    python.stdout.on('data', (data) => {
        return (data.toString());
    });

    python.stderr.on('data', (data) => {
        console.error(`Error occurred: ${data}`);
        return null;
    })

    python.on('exit', (code) => {
        console.log(`Exit code ${code}`);
        return null;
    });
}

/**
 * Encrypts a message.
 *
 * @param {string} message to encrypt
 * @return {string} encrypted message. Returns null if there was an error or an exit (whatever that is)
 */
exports.encryptMessage = function(message) {
    const python = spawn('python', [ENCRYPT_SCRIPT , message]);

    python.stdout.on('data', (data) => {
        return data.toString;
    });

    python.stderr.on('data', (data) => {
        console.error(`Error occurred: ${data}`);
        return null;
    })

    python.on('exit', (code) => {
        console.log(`Exit code ${code}`);
        return null;
    });
}