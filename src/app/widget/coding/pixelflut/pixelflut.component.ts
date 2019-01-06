import {Component, ElementRef, OnDestroy, OnInit} from '@angular/core';
import {Observable, Observer} from "rxjs";

@Component({
  selector: 'app-pixelflut',
  templateUrl: './pixelflut.component.html',
  styleUrls: ['./pixelflut.component.css']
})
export class PixelflutComponent implements OnInit, OnDestroy {

  public initialized = false;
  public xSize;
  public ySize;

  private canvas;
  private obs: Observable<MessageEvent>;

  constructor(private elRef: ElementRef) { }

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
    this.getCanvas();
    let msgs = event.data.toString().split(";");
    for (let msg of msgs) {
      if (msg.startsWith("SIZE")) {
        this.handle_SIZE(msg);
      }
      else if (msg.startsWith("PX")) {
        this.handle_PX(msg);
      }
      else {
        //console.error("Unknown pixelflut message: " + msg);
      }
    }
  }

  getCanvas() {
    if (this.canvas == undefined) {
      this.canvas = this.elRef.nativeElement.getElementsByTagName("canvas")[0];
    }
  }

  handle_SIZE(msg: String) {
    let splitted = msg.split(" ");
    this.xSize = splitted[1];
    this.ySize = splitted[2];

    this.initialized = true;
  }

  handle_PX(msg: String) {
    if (this.canvas != undefined) {
      let splitted = msg.split(" ");
      let x = splitted[1];
      let y = splitted[2];
      let color = splitted[3];

      this.canvas.getContext("2d").fillStyle = "#" + color;
      this.canvas.getContext("2d").fillRect(x, y, 1, 1);
    }
  }

  ngOnDestroy(): void {

  }

}
