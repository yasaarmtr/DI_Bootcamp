// function setTime_out(){
//     setTime_out(function(){
//         console.log("it is raining and i do npt like it ")

//     },3000);

// }

// function setInter_var(){
//     id=setInterval(function)
// }


function setTime_out(){
    setTimeout(function(){
      console.log('it is raining and I do not like it');
    },3000);
  }
  let id;
  function setInter_val(){
    id = setInterval(function(){
      console.log('hello');
    },2000)
  }
  
  function clearInter_val(){
    clearInterval(id)
  }
  
  function move() {
    let posx = 0;
    let posy = 0;
    let elem = document.getElementById('inner');
    let id = setInterval(function(){
        
            if(posx === 350){
            clearInterval(id)
            }
            else {
            elem.style.left = posx + 'px';
            posx++;

                if(posx === 350 && posy === 0){
                elem.style.top = posy + 'px';
                posy++;
                }
            }

            // if(posy === 350){
            //     clearInterval(id)
            // }
            // else {
            // elem.style.left = posy + 'px';
            // posy++;
            // }


        
        // else if (pos.left ==350)
        // elem.style.top = pos + 'px';


    },5)
  }