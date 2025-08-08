const rawOutput = document.getElementById('raw-output');
const ws = new WebSocket(`ws://${location.host}`);

ws.onmessage = (event) => {
    const message = JSON.parse(event.data);
    const id = message.id;
    const data = message.data;
    const time = new Date();
    rawOutput.textContent += `#${String(id).padStart(5, '0')} @ ${time.toLocaleTimeString('lt-LT')}    ${data}\n`;
}