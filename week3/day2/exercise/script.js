let form = document.getElementsByTagName('form');

form[0].addEventListener("submit",function(e){
    e.preventDefault();
    let fname = document.getElementById('fname').value;
    let lname = document.getElementById('lname').value;
    console.log(fname.trim().length);    
})

