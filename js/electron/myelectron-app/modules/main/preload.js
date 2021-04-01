/*
 * @Author: dingdingtao
 * @Date: 2021-04-01 10:36:09
 * @LastEditTime: 2021-04-01 11:54:36
 * @LastEditors: dingdingtao
 * @Description: 
 */
window.addEventListener('DOMContentLoaded', () => {
    const replaceText = (selector, text) => {
      const element = document.getElementById(selector)
      if (element) element.innerText = text
    }
  
    for (const type of ['chrome', 'node', 'electron']) {
      replaceText(`${type}-version`, process.versions[type])
    }
  })


// const { remote } = require('electron')

// let rigthTemplate = [
//     {label:'粘贴',accelerator: 'ctrl+z'},
//     {label:'复制',accelerator: 'ctrl+c'}
// ]

// let m = remote.Menu.buildFromTemplate(rigthTemplate)
// window.addEventListener('contextmenu', function(e) {
//     //阻止当前窗口默认事件
//     e.preventDefault();
//     //把菜单模板添加到右键菜单
//     m.popup({
//         window: remote.getCurrentWindow()
//     })
// })