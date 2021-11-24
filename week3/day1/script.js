

let div_page = document.getElementById("page");
console.log(div_page);

//firstElementChild / firstChild
console.log(div_page.firstElementChild);
console.log(div_page.firstChild);

//lastElementChild / lastChild
console.log(div_page.lastElementChild);
console.log(div_page.lastChild);

//nextElementSibling / nextSibling
console.log(div_page.nextElementSibling);
console.log(div_page.nextSibling);

//previousElementSibling / previousSibling
console.log(div_page.previousElementSibling);
console.log(div_page.previousSibling);

//parentNode
console.log(div_page.parentNode);

//childNodes
console.log(div_page.childNodes);




//classwork ex1: Traversing the DOM
let div1 = document.getElementById('page');// firstChild returns the first child node as an element node
console.log(div1);
console.log(div1.firstElementChild);
console.log(div1.firstChild); // firstElementChild returns the first child node as an element node (ignores text and comment nodes)
let div2 = document.getElementById('content');
console.log(div2);
console.log(div2.lastElementChild);
console.log(div2.lastChild);
var div2 = document.getElementById("header");
console.log(div2.nextElementSibling);
console.log(div2.nextSibling);
var div2 = document.getElementById("content");
console.log(div2.previousElementSibling);
console.log(div2.previousSibling);
let body = document.body;
console.log(body.parentNode);
let body =document.body;
console.log(body.childNodes);
//ex2- Targeting nodes
let elem_value = document.querySelector('#contenth2');
console.log(elem_value);
console.log('nodevalue textContent',elem_value.textContent);
console.log('nodevalue innerHTML',elem_value.innerHTML);
console.log('nodevalue innerText', elem_value.innerText);
elem_value.innerHTML = "<h1> Header</h1>";
elem_value.innerText = "text text text";
elem_value.setAttribute('blabla', '1233455');
let bla = elem_value.getAttribute('blabla')
console.log('bla');
let img = document.createElement('img');
img.setAttribute('src', 'img1.jpg' );
img.styles.height = '100px';
//div_page.appendChild(img);
div_page.insertBefore(img,div_page.lastElementChild);
// console.log(div_page.lastElementChild);
// div_page.removeChild(div_page.lastElementChild)
let div_content = document.getElementById('content');
let children = div_content.children;
div_content.replaceChild(children[2],)