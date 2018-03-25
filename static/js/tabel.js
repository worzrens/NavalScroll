function tabelPress(){
	const element = document.querySelector('#tabel');
	const sent = document.querySelector('#sent');
	const text = document.querySelector('#textArea').value;
	const table = document.querySelector('#forResult');
	const textForTr = document.createElement('tr');

	table.appendChild(textForTr);

	textForTr.innerText = text;

}
sent.addEventListener("click", tabelPress);