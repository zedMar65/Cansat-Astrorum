const express = require('express');
const { SerialPort } = require('serialport');
const { WebSocketServer } = require('ws');

const serverPort = 3000;
const serialPath = 'COM3';
const serialBaudRate = 9600;

const app = express();

const server = app.listen(serverPort, () => console.log(`Server running at http://localhost:${serverPort}`));

app.use(express.static('public'));

const wss = new WebSocketServer({ server });

let serialPort;

let messageId = 0;

function sendToAllClients(message) {
  wss.clients.forEach(client => {
    if (client.readyState === 1) {
      client.send(JSON.stringify({id: messageId, data: message}));
    }
  });
  messageId++;
}

function openSerialPort() {
  try {
    serialPort = new SerialPort({ path: serialPath, baudRate: serialBaudRate }, (err) => {
      if (err) {
        console.error('Failed to open the serial port:', err.message);
        return;
      }
      console.log('Serial port opened succesfully');
    });

    serialPort.on('data', (data) => {
      sendToAllClients(data.toString());
    });

    serialPort.on('error', (err) => {
      console.error('Serial port error:', err.message);
    })

  } catch (err) {
    console.error('Failed to open the serial port:', err.message);
    return;
  }
}

openSerialPort();


/// Testing

setInterval(sendToAllClients, 1000, "Hello, World!");