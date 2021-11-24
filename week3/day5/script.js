// function getData(){
// 	fetch("https://jsonplaceholder.typicode.com/users")
// 	//fetch is a promise
// .then(res => res.json())
// .then(data => {
// 	console.log(data);
// 	createRobots(data)
// })
// }


// function createRobots(arr){
// 	let root = document.getElementById('root');
// 	for (let i = 0; i < arr.length; i++) {
// 		let div = document.createElement('div');
// 		//img ->id
// 	let img = document.createElement('img');
// 	img.setAttribute('src',`https://robohash.org/${arr[i].id}?size=200x200`)
// 	div.appendChild(img)
// 	//user name
// 	let h2 = document.createElement('h2');
// 	h2.innerText = arr[i].name;
// 	div.appendChild(h2)
// 	//email
// 	let h4 = document.createElement('h4');
// 	h4.innerText = arr[i].email;
// 	div.appendChild(h4);
// 	//username
// 	let p = document.createElement('p');
// 	p.innerText = arr[i].username;
// 	div.appendChild(p);
// 	root.appendChild(div)
// 	}
	
// }

//--------------------------------------------------------------------------------
// let f = document.getElementById('fname');
// let s = document.getElementById('sname');

// function getData(){
//     let f = document.getElementById('fname').value
//     let s = document.getElementById('sname').value  
// 	fetch(`https://love-calculator.p.rapidapi.com/getPercentage?sname=${s}&fname=${f}`, {
// 	"method": "GET",
// 	"headers": {
// 		"x-rapidapi-host": "love-calculator.p.rapidapi.com",
// 		"x-rapidapi-key": "8337f40406mshc7fb184342977b5p17f3a1jsne6dbece24b7e"
// 	}
// })
// .then(response => response.json())
// .then(data => {
//     console.log(data);
//     putResults(data)
// })
// .catch(err => {
//     console.error(err);
// });
// }


// function putResults(objRes){
// 	let res = document.getElementById('results');
// 	res.innerText = "";
//     let h4 = document.createElement('h4');
//     h4.innerText = " Name " + objRes.fname;
//     res.appendChild(h4);
//     let h4s = document.createElement('h4');
//     h4s.innerText = " Your match name " + objRes.sname;
//     res.appendChild(h4s);
//     let h3 = document.createElement('h3');
//     h3.innerText = " percentage " + objRes.percentage + "%";
//     res.appendChild(h3);
//     let result = document.createElement('h2');
//     result.innerText = objRes.result;
//     res.appendChild(result);
// }
//------------------------------------------------------

// let f = document.getElementById('fname');
// let s = document.getElementById('sname');
// let ccode = document.getElementById
function getData(){
    // let f = document.getElementById('fname').value
    // let s = document.getElementById('sname').value  
	fetch(`https://covid-19-data.p.rapidapi.com/country/code?code=mu`, {
	"method": "GET",
	"headers": {
		"x-rapidapi-host": "covid-19-data.p.rapidapi.com",
		"x-rapidapi-key": "8337f40406mshc7fb184342977b5p17f3a1jsne6dbece24b7e"
	}
})
.then(response => response.json())
.then(data => {
    console.log(data);
    putResults(data)
})
// .catch(err => {
//     console.error(err);
// });
}

function putResults(objRes){
	let res = document.getElementById('results');
    res.innerText = " "

    var h4 = document.createElement('h4');
    res.innerText = "Covid-19 update for Maurituis" ;
    res.appendChild(h4);

    var h4 = document.createElement('h4');
    res.innerText = "Confirmed cases: " + objRes[0].confirmed;
    res.appendChild(h4);

    var h4 = document.createElement('h4');
    h4.innerText = "Recovered cases: " + objRes[0].recovered;
    res.appendChild(h4);
}


