console.log("Hello welcome to index.js file from static folder")
document.addEventListener("DOMContentLoaded",function(event){
  let form_ele = document.querySelector("#form")
  form_ele.onsubmit  = function (event){
    event.preventDefault()
    let hour = document.querySelector("#hour")
    let hour_value = hour.value
    let am_pm = document.querySelector("#am_pm")

    let am_pm_value = am_pm.value
    console.log(am_pm_value,typeof(am_pm_value),am_pm_value.length)
    console.log(hour_value,typeof(hour_value),hour_value.length)
    console.log(window.location.href)
    let url_string = window.location.href+ "data" +"?hour=" + hour_value + "&" + "am_pm=" + am_pm_value
    console.log(url_string)
    window.location.href = url_string
  }
  console.log("hours element",hour);
  console.log(hour.value)
});
