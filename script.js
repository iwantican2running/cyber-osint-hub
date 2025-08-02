document.addEventListener("DOMContentLoaded", () => {
    const terminalOutput = document.getElementById("terminal-output");
    const cursor = document.createElement("span");
    cursor.className = "cursor";
    cursor.innerText = "|";
    terminalOutput.appendChild(cursor);

    const commands = [
        "Initializing OSINT tools...\n",
        "Scanning for public data...\n",
        "Data retrieved: 3,510 records found.\n",
        "Analyzing data...\n",
        "Threats identified: 5\n",
        "Report generated. Downloading...\n",
    ];

    let index = 0;
    function simulateTerminalOutput() {
        if (index < commands.length) {
            terminalOutput.innerText += commands[index];
            index++;
            setTimeout(simulateTerminalOutput, 1200);
        } else {
            cursor.style.display = "none";  // Hide cursor after output
        }
    }

    function blinkCursor() {
        setInterval(() => {
            cursor.style.visibility = cursor.style.visibility === "hidden" ? "visible" : "hidden";
        }, 500);
    }

    blinkCursor();
    simulateTerminalOutput();
    
    // Interactive button to refresh data
    const refreshButton = document.getElementById("refresh-button");
    refreshButton.addEventListener("click", () => {
        terminalOutput.innerText = "";
        index = 0;
        cursor.style.display = "inline"; // Show cursor again
        simulateTerminalOutput();
    });
});
```

### CSS (for cursor effect)
```css
.cursor {
    display: inline;
    color: green;
}
``` 

### HTML Example Structure
```html
<div id="terminal-output"></div>
<button id="refresh-button">Refresh Data</button>