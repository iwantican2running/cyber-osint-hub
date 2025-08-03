document.addEventListener("DOMContentLoaded", () => {
    const terminal = document.querySelector("#terminal");
    const cursor = document.createElement("span");
    cursor.innerText = "|";
    cursor.className = "cursor";
    terminal.appendChild(cursor);
    
    const commands = [
        "Initializing OSINT tools...",
        "Gathering data from public sources...",
        "Analyzing IP address...",
        "Fetching user profiles...",
        "Scanning for vulnerabilities..."
    ];

    let index = 0;

    function typeCommand() {
        if (index < commands.length) {
            const commandText = commands[index];
            terminal.innerHTML += `<div>${commandText}</div>`;
            index++;
            setTimeout(typeCommand, 2000);
        } else {
            cursor.style.display = 'none'; // Hide cursor when done
        }
    }

    function toggleCursor() {
        cursor.style.visibility = (cursor.style.visibility === 'hidden') ? 'visible' : 'hidden';
    }

    setInterval(toggleCursor, 500);
    typeCommand();

    // Interactive element to simulate data update
    const updateButton = document.createElement("button");
    updateButton.innerText = "Update Dashboard";
    updateButton.onclick = () => {
        const newData = `Updated data at ${new Date().toLocaleTimeString()}`;
        terminal.innerHTML += `<div>${newData}</div>`;
    };
    document.body.appendChild(updateButton);
});
```

Make sure you have a corresponding HTML structure with an element having an ID of `terminal` for this script to function properly.