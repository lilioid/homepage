import {Component} from '@angular/core';
import {Widget} from "../widget";
import {TaskbarService} from "../../taskbar/taskbar.service";
import {DesktopService} from "../desktop.service";

@Component({
  selector: 'app-widget-imprint',
  templateUrl: './widget-imprint.component.html',
  styleUrls: ['./widget-imprint.component.css', '../widget.css']
})
export class WidgetImprintComponent extends Widget{

    constructor(desktopService: DesktopService, taskbarService: TaskbarService) {
        super(desktopService, taskbarService);
    }

}
