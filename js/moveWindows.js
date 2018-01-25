var dragElements = document.getElementsByClassName("drag-handler");

var lookForElements = window.setInterval(function() {
	if (dragElements.length) {
		mapEvents(dragElements);
		window.clearInterval(lookForElements);
	}
}, 500);

function mapEvents(ListOfElements) {
	for (var i = 0; i < ListOfElements.length; i++) {
		ListOfElements[i].addEventListener("mousedown", startDrag);
	}
}

function startDrag(e) {
	window["startX"] = e.screenX;
	window["startY"] = e.screenY;
	window["dragElement"] = $(e.currentTarget ).closest(".draggable").get(0);
	window["startTargetX"] = window.dragElement.offsetLeft;
	window["startTargetY"] = window.dragElement.offsetTop;

	var bodyElement = document.getElementsByTagName("body");
	bodyElement[0].addEventListener("mousemove", moveDrag);
	bodyElement[0].addEventListener("mouseup", endDrag);
	bodyElement[0].classList.add("noSelect");
}

function moveDrag(e) {
	var currentMouseX = e.screenX;
	var currentMouseY = e.screenY;

	window["mouseDiffX"] = (currentMouseX - window.startX);
	window["mouseDiffY"] = (currentMouseY - window.startY);
	window.dragElement.style.left = (window.mouseDiffX + window.startTargetX) + "px";
	window.dragElement.style.top = (window.mouseDiffY + window.startTargetY) + "px";
}

function endDrag(e) {
	var bodyElement = document.getElementsByTagName("body");
	bodyElement[0].removeEventListener("mousemove", moveDrag);
	bodyElement[0].classList.remove("noSelect");
}
