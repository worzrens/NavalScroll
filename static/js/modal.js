function forModalA(){
	var modal = document.getElementById('myModalA');
	var btn = document.getElementById("myBtnA");
	var span = document.getElementsByClassName("close")[0];

	btn.onclick = function() {
	    modal.style.display = "block";
	}
	span.onclick = function() {
	    modal.style.display = "none";
	}
	window.onclick = function(event) {
	    if (event.target == modal) {
	        modal.style.display = "none";
	    }
	}
}
function forModalF(){
	var modal = document.getElementById('myModalF');
	var btn = document.getElementById("myBtnF");
	var span = document.getElementsByClassName("close")[0];

	btn.onclick = function() {
	    modal.style.display = "block";
	}
	span.onclick = function() {
	    modal.style.display = "none";
	}
	window.onclick = function(event) {
	    if (event.target == modal) {
	        modal.style.display = "none";
	    }
	}
}

function popup() {
    var popup = document.getElementById("myPopup");
    popup.classList.toggle("show");
}

 function getdate(){
	let date = new Date();
	console.log(date);
 }
document.getElementById("myBtnA").addEventListener("click",forModalA);
document.getElementById("myBtnF").addEventListener("click",forModalF);