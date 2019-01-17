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

            this.connect("wss://finn-thorben.me/pixelflut/", "pixelflut");

        }
    }

    getCanvas() {
        this.canvasCtx = this.elRef.nativeElement.getElementsByTagName("canvas")[0].getContext("2d");
    }

    private connect(url: string, protocol: string): void {
        let _this = this;

        this.sock = new WebSocket(url, protocol);


        this.sock.onmessage = function (event: MessageEvent) {
            _this.msgHandler(event);
        };

        this.sock.onclose = function (event) {};

        this.sock.onerror = function (event) {
            console.log("Socket error: ");
            console.log(event);
        };
        this.sock.onopen = function (event) {
            console.log("Pixelflut websocket opened");
            _this.sock.send("SIZE");
        }
    }

    private command_loop(ix: number, iy: number) {
        let size = 80;

        // if right side is reached -> read a new line
        if (ix >= this.xSize) {
            ix = 0;
            iy = iy + size
        }

        // if bottom is reached -> start from top
        if (iy >= this.ySize) {
            ix = 0;
            iy = 0;
        }

        let x_start = ix;
        let x_end = Math.min(ix + size, this.xSize) -1;
        let y_start = iy;
        let y_end = Math.min(iy + size, this.ySize) -1;

        //console.log("STATE " + x_start + " " + x_end + " " + y_start + " " + y_end);
        this.sock.send("STATE " + x_start + " " + x_end + " " + y_start + " " + y_end);
        //this.sock.send("STATE 101 202 0 101");

        let _this = this;
        setTimeout(_ => _this.command_loop(x_end + 1, y_start), 50);
    }

    private msgHandler(event: MessageEvent) {
        let msg: string = event.data;

        if (msg.startsWith("SIZE")) {
            this.handle_SIZE(msg);
        } else if (msg.startsWith("PX")) {
            this.handle_PX(msg);
        } else if (msg.startsWith("STATE")) {
            this.handle_STATE(msg);
        }

        else {
            console.error("Unknown pixelflut command: " + msg);
        }
    }

    handle_SIZE(msg: string) {
        let splitted = msg.replace("\n", "").split(" ");
        this.xSize = +splitted[1];
        this.ySize = +splitted[2];
        this.xScaling = this.canvasXSize / this.xSize;
        this.yScaling = this.canvasYSize / this.ySize;

        console.log("Setup pixelflut canvas with " + this.xSize + "x" + this.ySize);

        // Also start the command loop since the size is now known
        this.command_loop(0, 0);
    }

    handle_PX(msg: string) {
        let splitted = msg.replace("\n", "").split(" ");
        this.draw_pixel(+splitted[1], +splitted[2], splitted[3]);
    }

    handle_STATE(msg: string) {
        // Variables which save the range of received pixels
        let x_start: number;
        let x_end: number;
        let y_start: number;
        let y_end: number;

        // Iterator variables needed to know which pixel is currently processed
        let ix = 0;
        let iy = 0;

        // Iterate over the message to split it by "," separators
        let builder: string = "";
        for (let i of msg) {
            if (i == ",") {

                // With this information we can setup the x and y ranges
                if (builder.startsWith("STATE")) {
                    let splitted = builder.split(" ");
                    x_start = +splitted[1];
                    x_end = +splitted[2];
                    y_start = +splitted[3];
                    y_end = +splitted[4];

                    ix = x_start;
                    iy = y_start;
                }

                // Otherwise this is pixel data
                else {
                    this.draw_pixel(ix, iy, builder);

                    if (iy == y_end) {
                        iy = y_start;
                        ix++;
                    } else {
                        iy++;
                    }
                }

                builder = "";
            } else {
                builder += i;
            }
        }
    }

    draw_pixel(x: number, y: number, color: string) {
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
