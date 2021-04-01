/*
 * @Author: dingdingtao
 * @Date: 2021-04-01 10:34:16
 * @LastEditTime: 2021-04-01 12:09:30
 * @LastEditors: dingdingtao
 * @Description: 
 */
const { app, BrowserWindow } = require('electron')
const path = require('path')


function createWindow () {
  const win = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      preload: path.join(__dirname, 'modules/main/preload.js')
    }
  })
  
  win.webContents.openDevTools()
  win.loadFile('./modules/main/index.html')
}

app.whenReady().then(() => {
    require('./modules/main/menu.js')
    createWindow()
    
  app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0) {
      createWindow()
    }
  })
})

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit()
  }
})
