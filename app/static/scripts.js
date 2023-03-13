function playAudio(text) {
	var audio = new Audio("/audio/" + text);
	audio.play();
}
