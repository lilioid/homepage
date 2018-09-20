import {Component} from '@angular/core';
import {Widget} from "../widget";
import {DesktopService} from "../desktop.service";
import {TaskbarService} from "../../taskbar/taskbar.service";

@Component({
  selector: 'app-widget-cv',
  templateUrl: './widget-cv.component.html',
  styleUrls: ['./widget-cv.component.css', '../widget.css']
})
export class WidgetCvComponent extends Widget {

    icon: string = "user-circle";
    taskbarName: string = "CV";

    constructor(desktopService: DesktopService, taskbarService: TaskbarService) {
        super(desktopService, taskbarService);
    }

}
