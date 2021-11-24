<html>
  <head>
    <title>JavaScript and the Document Object Model</title>
  </head>
  <body>
    <div id="page">
      <div id="header">
        <h1 id="title">Page title</h1>
      </div>
      <div id="content">
        <h2>Content title</h2>
        <p>Some copy goes here</p>
        <p>More copy goes here</p>
      </div>
    </div>
  </body>
</html>

Exercise 1: Traversing the DOM
Knowing how to traverse the DOM using JavaScript provides a foundation
to altering an HTML page in real time.
Using the HTML markup in Listing 1, perform these tasks:
1. Use the firstElementChild / firstChild property to access an element.
2. Use the lastElementChild / lastChild  property to access an element.
3. Use the nextElementSibling / nextSibling  property to access an element.
4. Use the previousElementSibling / previousSibling  property to access an element.
5. Use the parentNode property to access an element.
6. Use the childNodes property to access a group of child elements.


Exercise 2: Targeting nodes 
In exercise 1, you learned how to target nodes in several ways.
Continuing to use the markup in Listing 1, perform the following tasks:
1. Retrieve the value of a node using nodeValue / innerText / innerHTML.
2. Change the value of a node using nodeValue / innerText / innerHTML.
3. Retrieve the value of a node attribute.
4. Change the value of a node attribute.

Exercise 3: Manipulating the DOM
Now that you know how to traverse the DOM and alter node values,
the next logical step is to learn how to add, remove, and replace nodes.
Perform the following tasks:
1. Use the appendChild method to add a node.
2. Use the insertBefore method to add a node.
3. Use the removeChild method to remove a node.
4. Use the replaceChild method to replace a node.


let div_content = document.getElementById('content');
// console.log(div_content);
// console.log(div_content.getAttribute('class'));
// div_content.setAttribute('ziv', '123456')
​
// let bgs = document.getElementsByClassName('bg');
// for (var i = 0; i < bgs.length; i++) {
//   bgs[i].classList.add('bg1')
// }
​
// let first_elem_child = div_page.firstElementChild;
// let first_elem = div_page.firstChild;
// console.log(first_elem_child);
// console.log(first_elem);
//
// //lastElementChild lastChild
// let last_elem_child = div_page.lastElementChild;
// let last_elem = div_page.lastChild;
// console.log('lastElementChild',last_elem_child);
// console.log('lastChild',last_elem);
//
// // nextElementSibling nextSibling
// let next_element_sibling = first_elem_child.nextElementSibling;
// let next_sibling = first_elem_child.nextSibling;
// console.log('nextElementSibling',next_element_sibling);
// console.log('nextSibling',next_sibling);
//
// // previousElementSibling / previousSibling
// let previous_element_sibling = next_element_sibling.previousElementSibling;
// let previous_sibling = next_element_sibling.previousSibling;
// console.log('previousElementSibling',next_element_sibling);
// console.log('previousSibling',next_sibling);
//
// //parentNode
// console.log('parentNode',div_page.parentNode);
//
// // nodeValue / innerText / innerHTML
// let elem_value = document.querySelector('#content h2');
// console.log(elem_value);
//
// let txt = document.createTextNode('hello text node');
// div_page.appendChild(txt)
// console.log('nodeValue',document.getElementById('title').firstChild.nodeValue);
// console.log('nodeValue textContent',elem_value.textContent);
// console.log('nodeValue innerHTML',elem_value.innerHTML);
// console.log('nodeValue innerText',elem_value.innerText);
//
//
// elem_value.innerHTML = "<h1>Header h1</h1>";
// elem_value.innerText = "text text text";
//
// elem_value.setAttribute('blabla','123456');
// let bla = elem_value.getAttribute('blabla')
// console.log(bla);
//
// let img = document.createElement('img');
// img.setAttribute('src','img1.jpg');
// img.style.height = '100px';
// // div_page.appendChild(img);
//
// // div_page.insertBefore(img, div_page.lastElementChild);
// // console.log(div_page.lastElementChild);
// // div_page.removeChild(div_page.lastElementChild)
//
// // let div_content = document.getElementById('content');
// // let children = div_content.children;
// // div_content.replaceChild(children[2],children[0]);
