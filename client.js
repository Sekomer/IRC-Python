import { createRequire } from 'module';
const require = createRequire(import.meta.url);

//let net = require('net');
let prompt = require('prompt-sync')();

const name = prompt('Username: ');

// Encoder 
let encode = s => decodeURIComponent(escape(s));

const HOST = '127.0.0.1';
const PORT = 4242;
let client = new net.Socket();


function packetProcess(name) {
    const data = prompt(`${name}: `);
    
    if (data == 'Q' || data == 'q')
        return -1

    const encoded = encode(data)
    const length = encoded.length
    const header = `${length}`.padEnd(4)
    
    const packet = encode(header + encoded) 
    
    return packet
}

client.connect(PORT, HOST, () => {
    console.log('CONNECTED TO: ' + HOST + ':' + PORT);
});

function main() {
    while (true) {
        const packet = packetProcess(name);
    
        if (packet == -1) {
            return -1
        }
    
        client.write(packet)
    }
}

client.on('connect', main)



//const worker = require('worker_threads');



// ASYNCH
/* 
async function safeConnection() {
    client.connect(PORT, HOST, () => {
        console.log('CONNECTED TO: ' + HOST + ':' + PORT);
    });
}

async function main() {
    await safeConnection();

    while (true) {
        const packet = packetProcess(name);
    
        if (packet == -1) {
            return -1
        }
    
        client.write(packet)
    }   
}

main()  */