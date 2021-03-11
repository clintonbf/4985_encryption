'use strict';

const crypto = require('crypto');
const fs = require('fs');

const phrase = 'datacomm for life';

const filename = 'keyfile';
let ENC_KEY = "Nz0duCCUve2YH41n_SCLkWdMGwLfdMM3_2mYy68I0Go=".toString('binary');

// await fs.readFile(filename, (err, data) => {
//     if (err) throw err;
//
//     console.log(`Data is ${data}`)
//     ENC_KEY = data;
//
// });

let encrypt = ( (val) => {
    let cipher = crypto.createCipher('aes-128-cbc', ENC_KEY);
    let encrypted = cipher.update(val, 'utf8', 'base64');
    encrypted += cipher.final('base64');

    return encrypted;
});

let decrypt = ((encrypted) => {
    let decipher = crypto.createDecipher('aes-128-cbc', ENC_KEY);
    let decrypted = decipher.update(encrypted, 'base64', 'utf8');
    return (decrypted + decipher.final('utf8'));
});


let encrypted_key = encrypt(phrase);
console.log(`Encrypted phrase is ${encrypted_key}`);
console.log(`Decrypted phrase is ${decrypt(encrypted_key)}`);
