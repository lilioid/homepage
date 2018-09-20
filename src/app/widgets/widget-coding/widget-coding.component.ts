import {Component} from '@angular/core';
import {Widget} from "../widget";
import {DesktopService} from "../desktop.service";
import {TaskbarService} from "../../taskbar/taskbar.service";

@Component({
  selector: 'app-widget-coding',
  templateUrl: './widget-coding.component.html',
  styleUrls: ['./widget-coding.component.css', '../widget.css']
})
export class WidgetCodingComponent extends Widget{

    icon: string = "code";
    taskbarName: string = "Coding";

    constructor(desktopService: DesktopService, taskbarService: TaskbarService) {
        super(desktopService, taskbarService);
    }

}
