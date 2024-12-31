const RECONNECT_DELAY = 5_000;
const SERVER_URL = "wss://li.lly.sh/pixelflut.sock";

function setupWebsocket(url) {
    if (window.px != null) {
        window.px.close();
    }

    console.info("Connecting to pixelflut server via WebSocket");
    window.px = new WebSocket(url);
    window.px.onopen = () => {
        console.info("WebSocket connection to pixelflut server established");
    };
    window.px.onclose = () => {
        console.error("WebSocket connection to pixelflut server lost, trying to reconnect in 5 seconds");
        setTimeout(setupWebsocket, RECONNECT_DELAY, url);
    };
    window.px.onerror = (e) => {
        console.warn("Error on WebSocket connection to pixelflut server", e);
    };
    window.px.onmessage = (e) => {
        console.info(e.data);
    };
}

setupWebsocket(SERVER_URL);
