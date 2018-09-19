import {Input, OnInit} from "@angular/core";
import {DesktopService} from "./desktop.service";
import {TaskbarService} from "../taskbar/taskbar.service";

export class Widget implements OnInit {

    @Input() height:String = "auto";
    @Input() width: String = "auto";
    @Input() posX: String = "0";
    @Input() posY: String = "0";
    @Input() autOpen: boolean = false;

    constructor (public desktopService:DesktopService, public taskbarService:TaskbarService) {

    }

    ngOnInit(): void {
        this.taskbarService.registerWidget(this);

        if (this.autOpen)
            this.desktopService.open(this);

    }

}
