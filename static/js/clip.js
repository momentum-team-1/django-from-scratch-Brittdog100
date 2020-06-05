let copy = document.querySelector("#copy");

function copyFunc() {
	let range = document.createRange();
	range.selectNode(document.querySelector("code"));
	window.getSelection().addRange(range);
	document.execCommand('copy');
	window.getSelection().empty();
}

copy.addEventListener('click', copyFunc);