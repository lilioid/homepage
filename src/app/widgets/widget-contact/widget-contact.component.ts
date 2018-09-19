import {Component} from '@angular/core';
import {Widget} from "../widget";
import {DesktopService} from "../desktop.service";
import {TaskbarService} from "../../taskbar/taskbar.service";

@Component({
  selector: 'app-widget-contact',
  templateUrl: './widget-contact.component.html',
  styleUrls: ['./widget-contact.component.css', '../widget.css']
})
export class WidgetContactComponent extends Widget {

    constructor(desktopService: DesktopService, taskbarService: TaskbarService) {
        super(desktopService, taskbarService);
    }

}

