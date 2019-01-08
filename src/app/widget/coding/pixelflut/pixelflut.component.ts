import {Component, ElementRef, OnDestroy, OnInit} from '@angular/core';

@Component({
    selector: 'app-pixelflut',
    templateUrl: './pixelflut.component.html',
    styleUrls: ['./pixelflut.component.css']
})
export class PixelflutComponent implements OnInit, OnDestroy {
    public canvasXSize = 800;
    public canvasYSize = 600;

    public xSize: number;
    public ySize: number;
    private xScaling: number;
    private yScaling: number;

    private canvasCtx;
    private sock: WebSocket;

    constructor(private elRef: ElementRef) {
    }

    ngOnInit() {
        if (this.canvasCtx == undefined) {
            this.getCanvas();

            let _this = this;
            setTimeout(_ => _this.ngOnInit());
        } else {

            this.connect("wss://finn-thorben.me/pixelflut/", "pixelflut-websocket");

        }
    }

    private connect(url: string, protocol: string): void {
        let _this = this;

        this.sock = new WebSocket(url, protocol);


        this.sock.onmessage = function (event: MessageEvent) {
            _this.updateHandler(event);
        };

        this.sock.onclose = function (event) {
            console.log("Socket closed by ");
            console.log(event);
        };
        this.sock.onerror = function (event) {
            console.log("Socket error: ");
            console.log(event);
        };
        this.sock.onopen = function (event) {
            console.log("Pixelflut websocket opened")
        }
    }

    private updateHandler(event: MessageEvent) {
        let msg_build = "";
        for (let part of event.data) {
            msg_build += part;

            if (part == ";") {
                this.parse_cmd(msg_build);
                msg_build = "";
            }
        }
    }

    getCanvas() {
        this.canvasCtx = this.elRef.nativeElement.getElementsByTagName("canvas")[0].getContext("2d");
    }

    parse_cmd(cmd: string) {
        if (cmd.startsWith("SIZE")) {
            this.handle_SIZE(cmd);
        } else if (cmd.startsWith("PX")) {
            this.handle_PX(cmd);
        } else {
            console.error("Unknown pixelflut command: " + cmd);
        }
    }

    handle_SIZE(msg: string) {
        let splitted = msg.replace(";", "").split(" ");
        this.xSize = +splitted[1];
        this.ySize = +splitted[2];
        this.xScaling = this.canvasXSize / this.xSize;
        this.yScaling = this.canvasYSize / this.ySize;

        console.log("Initiate pixelflut canvas with " + this.xSize + "x" + this.ySize);
    }

    handle_PX(msg: String) {
        let splitted = msg.replace(";", "").split(" ");
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

    ngOnDestroy(): void {
        console.log("Closing websocket");
        this.sock.close(null, "Component unloaded");
    }

}
