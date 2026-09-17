const { app, BrowserWindow } = require("electron");

function taoCuaSo() {
    const win = new BrowserWindow({
        width: 400,
        height: 600,
        alwaysOnTop: true,
        resizable: true,
        webPreferences: {
            nodeIntegration: false
        }
    });

    win.loadURL("http://127.0.0.1:5000");
}

app.whenReady().then(taoCuaSo);