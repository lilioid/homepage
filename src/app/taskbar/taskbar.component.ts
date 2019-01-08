import {Component, OnInit} from '@angular/core';
import {WidgetComponent} from "../widget/widget.component";
import {TaskbarService} from "./taskbar.service";
import {DesktopService} from "../desktop/desktop.service";

@Component({
    selector: 'app-taskbar',
    templateUrl: './taskbar.component.html',
    styleUrls: ['./taskbar.component.css']
})
export class TaskbarComponent implements OnInit {

    constructor(private taskbarService: TaskbarService, private desktopService: DesktopService) {
    }

    ngOnInit() {
    }

    public widgets(): WidgetComponent[] {
        return this.taskbarService.widgets;
    }

    public onWidgetClicked(widget: WidgetComponent) {
        if (this.desktopService.isOpen(widget) && this.desktopService.isTopWidget(widget))
            this.desktopService.close(widget);
        else
            this.desktopService.open(widget);
    }

}
