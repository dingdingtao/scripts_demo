/*
 * @Author: dingdingtao
 * @Date: 2021-04-01 10:55:34
 * @LastEditTime: 2021-04-01 12:17:41
 * @LastEditors: dingdingtao
 * @Description: 
 */
const { Menu, BrowserWindow } = require('electron')
const path = require('path')

let mainMenu = [
    {
        label: '前端',
        submenu: [
            {
                label: 'JavaScript',
                //绑定快捷键
                accelerator: `ctrl+n`,
                click: () => {
                    win = new BrowserWindow({
                        width: 400,
                        height: 300,
                        webPreferences: { nodeIntegration: true }
                    })
                    win.loadFile('./modules/javascript/javascript_main.html')
                    win.on('closed', () => {
                        win = null
                    })
                }
            },
            {
                label: 'HTML'
            },
            {
                label: 'CSS'
            }
        ]
    },
    {
        label: '后端',
        submenu: [
            {
                label: 'Java'
            },
            {
                label: 'Python'
            }
        ]
    },
    {
        label: '测试',
        submenu: [
            {
                label: '菜单点击效果测试',
                click: () => {
                    win = new BrowserWindow({
                        width: 400,
                        height: 300,
                        webPreferences: { 
                            nodeIntegration: true
                        }
                    })
                    win.loadFile('./modules/test/test1/test1.html')
                    win.on('closed', () => {
                        win = null
                    })
                }
            },
            {
                label: '自定义右键菜单测试',
                click: () => {
                    win = new BrowserWindow({
                        width: 800,
                        height: 600,
                        webPreferences: { 
                            // nodeIntegration: true,
                            preload: path.join(__dirname, '../test/test2/test2.js')
                        }
                    })
                    win.webContents.openDevTools()
                    win.loadFile('./modules/test/test2/test2.html')
                    win.on('closed', () => {
                        win = null
                    })
                }
            }
        ]
    }

]

let menu = Menu.buildFromTemplate(mainMenu)
Menu.setApplicationMenu(menu)