import {Component, Input, OnInit} from '@angular/core';
import {DesktopService} from "./desktop.service";
import {TaskbarService} from "../taskbar/taskbar.service";

@Component({
  selector: 'app-widget',
  templateUrl: './widget.component.html',
  styleUrls: ['./widget.component.css']
})
export class WidgetComponent implements OnInit {

    @Input() icon: string = "rocket";
    @Input() title: string = "Awesome Programm";

    @Input() height: string = "auto";
    @Input() width: string = "auto";
    @Input() posX: string = "0";
    @Input() posY: string = "0";
    @Input() autOpen: boolean = false;
    @Input() bounds: HTMLElement = null;

    dragEnabled: boolean = true;

    constructor (public desktopService:DesktopService, public taskbarService:TaskbarService) {
    }

    ngOnInit(): void {
        this.taskbarService.registerWidget(this);

        if (this.autOpen)
            this.desktopService.open(this);
    }

}
