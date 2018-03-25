const people = {
	qwe : "rty"
};


function handler() {
	const login = document.querySelector('#login').value;
	const password = document.querySelector('#password').value;
	const enter = document.querySelector('#enter');

	for(log in people){
		if(login == log || password == people[log] ){
			document.location.replace("button.html");
		}
	}
} 
enter.addEventListener("click",handler);

