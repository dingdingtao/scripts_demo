/*
 * @Author: dingdingtao
 * @Date: 2021-04-01 11:25:07
 * @LastEditTime: 2021-04-01 12:24:36
 * @LastEditors: dingdingtao
 * @Description: 
 */

const { Menu } = require('menu')

let rigthTemplate = [
    {label:'粘贴',accelerator: 'ctrl+z'},
    {label:'复制',accelerator: 'ctrl+c'}
]

let m = Menu.buildFromTemplate(rigthTemplate)
window.addEventListener('contextmenu', function(e) {
    //阻止当前窗口默认事件
    e.preventDefault();
    //把菜单模板添加到右键菜单
    m.popup({
        window: getCurrentWindow()
    })
})
