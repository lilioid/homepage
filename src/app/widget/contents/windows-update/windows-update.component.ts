import {Component, Input, OnInit} from '@angular/core';
import {PopupComponent} from "../../popup.component";

@Component({
    selector: 'app-windows-update',
    templateUrl: './windows-update.component.html',
    styleUrls: ['./windows-update.component.css']
})
export class WindowsUpdateComponent implements OnInit {

    @Input() popup: PopupComponent;

    constructor() {
    }

    ngOnInit() {
    }

}
