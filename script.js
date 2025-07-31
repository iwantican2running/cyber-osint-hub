// Terminal Simulator for OSINT Web Project
const terminalOutput = document.getElementById('terminal-output');
const cursor = document.createElement('span');
cursor.innerText = '|';
cursor.className = 'cursor';
terminalOutput.appendChild(cursor);

const commands = [
    "Scanning network...",
    "Collecting data...",
    "Analyzing patterns...",
    "Generating report...",
    "Scan completed successfully!"
];

let commandIndex = 0;

function typeCommand() {
    if (commandIndex < commands.length) {
        const command = commands[commandIndex];
        let charIndex = 0;

        const typingInterval = setInterval(() => {
            if (charIndex < command.length) {
                terminalOutput.innerHTML += command.charAt(charIndex);
                charIndex++;
            } else {
                clearInterval(typingInterval);
                setTimeout(() => {
                    terminalOutput.innerHTML += '<br>';
                    commandIndex++;
                    typeCommand();
                }, 1000);
            }
        }, 100);
    } else {
        cursor.style.display = 'none';
    }
}

function updateDashboard() {
    const dataElement = document.getElementById('data-visualization');
    dataElement.innerHTML = Math.floor(Math.random() * 100) + '% of data processed';
}

setInterval(updateDashboard, 2000);
typeCommand();

// CSS for blinking cursor
const style = document.createElement('style');
style.innerHTML = `
    .cursor {
        animation: blink 1s step-end infinite;
    }
    @keyframes blink {
        50% { opacity: 0; }
    }
`;
document.head.appendChild(style);