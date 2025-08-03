const terminalOutput = document.getElementById('terminal-output');
const cursor = document.getElementById('cursor');
const dataVisual = document.getElementById('data-visual');
const commands = ["Searching IP...", "Fetching data...", "Analyzing results...", "Completed!"];
let commandIndex = 0;

function blinkCursor() {
    cursor.classList.toggle('blink');
}

function typeCommand() {
    if (commandIndex < commands.length) {
        terminalOutput.innerHTML += `<div>${commands[commandIndex]}</div>`;
        commandIndex++;
        setTimeout(typeCommand, 2000);
    } else {
        updateVisual();
    }
}

function updateVisual() {
    const randomData = Math.floor(Math.random() * 100);
    dataVisual.style.width = `${randomData}%`;
    dataVisual.innerHTML = `${randomData}% Complete`;
}

document.addEventListener('DOMContentLoaded', () => {
    setInterval(blinkCursor, 500);
    typeCommand();
});
```

```css
.blink {
    animation: blink 1s step-end infinite;
}

@keyframes blink {
    50% { opacity: 0; }
}
```

```html
<div id="terminal-output"></div>
<div id="cursor">|</div>
<div id="data-visual" style="width: 0; background: green; height: 20px;"></div>