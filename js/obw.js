/*
 * @Author: dingdingtao
 * @Date: 2021-03-08 10:12:30
 * @LastEditTime: 2021-03-08 10:45:09
 * @LastEditors: dingdingtao
 * @Description: 
 */

window.onload = function(){
    let element = document.getElementById("container")
    const texts = ['test1','test2','test3']
    const texts_len = texts.length
    element.innerHTML = texts[0]
    element.style.opacity = '60%'

    function breath(index){
        if(index >= texts_len){
            index = index % texts_len
        }
        element.innerHTML = texts[index]
    }

    let breath_counter = 1
    let breath_timer = setInterval(function(){
        breath(breath_counter++)
    }, 2000)
}
 