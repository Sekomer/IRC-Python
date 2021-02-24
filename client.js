const { time } = require('console');
var net = require('net');
const { mainModule } = require('process');

var HOST = '127.0.0.1';
var PORT = 4242;

var client = new net.Socket();

const prompt = require('prompt-sync')();
const name = prompt('Username: ');

var encode = s => decodeURIComponent(escape(s));

function packetProcess(name) {
    const data = prompt(`${name}: `);
    
    if (data == 'Q' || data == 'q') {
        return -1
    }

    const encoded = encode(data)
    const length = encoded.length
    var header = `${length}`.padEnd(4)
    
    const packet = encode(header + encoded) 
    
    return packet
}

client.connect(PORT, HOST, () => {
    console.log('CONNECTED TO: ' + HOST + ':' + PORT);

});

client.on('connect', main)

function main() {
    while (true) {
        const packet = packetProcess(name);
    
        if (packet == -1) {
            return -1
        }
    
        client.write(packet)
    }
}

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