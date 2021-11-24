
let box = document.getElementById('box');

box.addEventListener('drag', function(e){
  let x = e.clientX;
  let y = e.clientY;
  console.log(x,y);
})

box.addEventListener('dragend',function(e){
  let x = e.clientX;
  let y = e.clientY;
  box.style.left = x + 'px';
  box.style.top = y + 'px';
})
// function setTime_out(){
//   setTimeout(function(){
//     console.log('it is raining and I do not like it');
//   },3000);
// }
// // let id;
// function setInter_val(){
//   id = setInterval(function(){
//     console.log('hello');
//   },2000)
// }
//
// function clearInter_val(){
//   clearInterval(id)
// }
// let id;
// function move() {
//   let pos = 0;
//   let pos2 = 0;
//   let a = 1;
//   let b = 0;
//   let elem = document.getElementById('inner');
//   id = setInterval(function(){
//       if(pos < 350 && b == 0){
//         a = 1;
//         b = 0;
//       }
//       else if (pos === 350 && b==0) {
//         b = 1;
//         a = 0;
//       }
//       else if(pos === 0 && pos2 === 0 && b==-1){
//         a=1
//         b=0;
//       }
//       if(pos2 === 350){
//         a = -1;
//         b = 0;
//       }
//       if (pos2 === 350 && pos === 0 ){
//         a = 0;
//         b = -1;
//       }
//
//       pos = pos + a;
//       pos2 = pos2 + b;
//       elem.style.left = pos + 'px';
//       elem.style.top = pos2 + 'px';
//
//   },5)
// }
//
// function stop(){
//   clearInterval(id)
// }
