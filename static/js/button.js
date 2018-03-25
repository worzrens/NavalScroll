const leftButton = document.querySelector('#leftButton')
const rightButton = document.querySelector('#rightButton')

function forLeftButton (argument) {
	alert("click left button");
}

function forRightButton (argument) {
	alert("click right button");
}

leftButton.addEventListener("click",forLeftButton);
rightButton.addEventListener("click",forRightButton);