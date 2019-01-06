import {Component, ElementRef, OnInit} from '@angular/core';
import {Observable, Observer} from "rxjs";

@Component({
    selector: 'app-pixelflut',
    templateUrl: './pixelflut.component.html',
    styleUrls: ['./pixelflut.component.css']
})
export class PixelflutComponent implements OnInit {
    public canvasXSize = 600;
    public canvasYSize = 300;

    public xSize: number;
    public ySize: number;
    private xScaling: number;
    private yScaling: number;

    private canvasCtx;
    private obs: Observable<MessageEvent>;

    constructor(private elRef: ElementRef) {}

    ngOnInit() {
        let _this = this;

        this.obs = this.connect("wss://finn-thorben.me/pixelflut/", "pixelflut-websocket");

        this.obs.subscribe(function (event) {
            _this.updateHandler(event);
        }, null, null);

        console.log("Connected to pixelflut server");
    }

    private connect(url: string, protocol: string): Observable<MessageEvent> {
        let sock = new WebSocket(url, protocol);

        return Observable.create((obs: Observer<MessageEvent>) => {
            sock.onmessage = obs.next.bind(obs);
            sock.onerror = obs.error.bind(obs);
            sock.onclose = obs.complete.bind(obs);
            return sock.close.bind(sock);
        });
    }

    private updateHandler(event: MessageEvent) {
        if (this.canvasCtx == undefined) {
            this.getCanvas();

        } else {
            let msgs = event.data.toString().split(";");
            for (let msg of msgs) {
                if (msg === "") {}
                else if (msg.startsWith("SIZE")) {
                    this.handle_SIZE(msg);
                } else if (msg.startsWith("PX")) {
                    this.handle_PX(msg);
                } else {
                    console.error("Unknown pixelflut message: " + msg);
                }
            }
        }
    }

    getCanvas() {
        this.canvasCtx = this.elRef.nativeElement.getElementsByTagName("canvas")[0].getContext("2d");
    }

    handle_SIZE(msg: String) {
        let slitted = msg.split(" ");
        this.xSize = +slitted[1];
        this.ySize = +slitted[2];
        this.xScaling = this.canvasXSize / this.xSize;
        this.yScaling = this.canvasYSize / this.ySize;
    }

    handle_PX(msg: String) {
        let splitted = msg.split(" ");
        let x = +splitted[1];
        let y = +splitted[2];
        let color = splitted[3];

        this.canvasCtx.fillStyle = "#" + color;
        this.canvasCtx.fillRect(
            x * this.xScaling,
            y * this.yScaling,
            this.xScaling,
            this.yScaling);
    }

}
