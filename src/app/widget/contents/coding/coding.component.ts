import {Component, ElementRef, OnInit} from '@angular/core';
import {PixelflutClient} from 'pixelflut-client';

@Component({
    selector: 'app-coding',
    templateUrl: './coding.component.html',
    styleUrls: ['./coding.component.css']
})
export class CodingComponent implements OnInit {

    pxCanvasWidth = -1;
    pxCanvasHeight = -1;

    private pxClient;

    constructor(private elRef: ElementRef) {
    }

    ngOnInit(): void {
        const canvas = this.elRef.nativeElement.getElementsByTagName('canvas')[0];
        this.pxClient = new PixelflutClient('wss://www.finn-thorben.me/pixelflut', canvas);
    }

}
