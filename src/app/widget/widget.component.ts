import {Component, Input, OnInit} from '@angular/core';
import {DesktopService} from "../desktop/desktop.service";
import {TaskbarService} from "../taskbar/taskbar.service";

@Component({
    selector: 'app-widget',
    templateUrl: './widget.component.html',
    styleUrls: ['./widget.component.css']
})
export class WidgetComponent implements OnInit {

    // Required inputs
    @Input() icon: string;
    @Input() title: string;
    @Input() bounds: HTMLElement;

    // Position inputs
    @Input() height: string = "auto";
    @Input() width: string = "auto";
    @Input() x: string = "5%";
    @Input() y: string = "5%";
    maximized: boolean = false;

    // Misc inputs
    @Input() autoOpen: boolean = true;
    @Input() dragEnabled: boolean = true;
    @Input() displayTopButtons: boolean = true;

    constructor(private desktopService: DesktopService, private taskbarService: TaskbarService) {
    }

    ngOnInit() {
        if (this.autoOpen)
            this.desktopService.open(this, false);

        this.taskbarService.registerWidget(this);
    }

    public zIndex() {
        return this.desktopService.getPosition(this);
    }

    public isOpen() {
        return this.desktopService.isOpen(this);
    }

    public isTopWidget() {
        return this.desktopService.isTopWidget(this);
    }

    public activate() {
        // Reopening this component will place it on top of the window stack
        this.desktopService.open(this);
    }

    public close() {
        this.maximized = false;
        this.desktopService.close(this);
    }

}
