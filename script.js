document.addEventListener('DOMContentLoaded', () => {
    const output = document.getElementById('terminal-output');
    const dashboard = document.getElementById('dashboard-container');

    // Simulate terminal output
    const messages = [
        'Scanning for vulnerabilities...',
        'Collecting data from public sources...',
        'Analysis complete. Found 5 potential threats.'
    ];
    
    let index = 0;
    function displayMessage() {
        if (index < messages.length) {
            output.textContent += messages[index] + '\n';
            index++;
            setTimeout(displayMessage, 2000);
        }
    }
    
    dashboard.addEventListener('click', () => {
        output.textContent = 'Initializing OSINT tools...\n';
        displayMessage();
    });
});