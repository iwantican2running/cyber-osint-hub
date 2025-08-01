// Terminal-like output simulation
const terminalOutput = document.getElementById('terminal');
const cursor = document.createElement('span');
cursor.className = 'cursor';
cursor.textContent = '|';
terminalOutput.appendChild(cursor);

function typeText(text, delay = 100) {
    return new Promise(resolve => {
        const chars = text.split('');
        let i = 0;
        const interval = setInterval(() => {
            if (i < chars.length) {
                terminalOutput.innerHTML += chars[i++];
            } else {
                clearInterval(interval);
                resolve();
            }
        }, delay);
    });
}

async function simulateTerminal() {
    await typeText('Fetching OSINT data...\n');
    await typeText('Data acquired: 12345 records found.\n', 50);
    await typeText('Analyzing data...\n\n', 100);
    await typeText('Threats detected: [XSS, SQL Injection, Phishing]\n', 50);
    cursor.style.display = 'none';
}

simulateTerminal();

// Interactive element for data visualization
const button = document.getElementById('updateDataBtn');
const dataDisplay = document.getElementById('dataDisplay');

button.addEventListener('click', () => {
    const newData = Math.floor(Math.random() * 100);
    dataDisplay.textContent = `Current Threat Level: ${newData}`;
    dataDisplay.style.color = newData > 50 ? 'red' : 'green';
});

// Cursor blink effect
setInterval(() => {
    cursor.style.visibility = cursor.style.visibility === 'hidden' ? 'visible' : 'hidden';
}, 500);
```

Make sure to include the necessary HTML structure for this JavaScript code to function correctly, such as elements with IDs `terminal`, `updateDataBtn`, and `dataDisplay`.