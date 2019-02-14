import {Component, Input} from '@angular/core';
import {WidgetComponent} from "./widget.component";
import {TaskbarService} from "../taskbar/taskbar.service";
import {DesktopService} from "../desktop/desktop.service";

@Component({
    selector: 'app-windows-update-widget',
    templateUrl: './widget.component.html',
    styleUrls: ['./widget.component.css', './popup.component.css']
})
export class PopupComponent extends WidgetComponent {

    @Input() waitTime: number;
    @Input() postponeTime: number;
    @Input() title: string;

    width = "60vw";
    height = "auto";
    x = "20vw";
    y = "30vh";
    dragEnabled = false;
    displayTopButtons = false;

    private _isOpen = false;

    constructor(desktopService: DesktopService, taskbarService: TaskbarService) {
        super(desktopService, taskbarService);
    }

    ngOnInit() {
        setTimeout(_ => this.activate(), this.waitTime);
    }

    isOpen(): boolean {
        return this._isOpen;
    }

    zIndex(): number {
        return 90;
    }

    activate() {
        this._isOpen = true;
    }

    isTopWidget(): boolean {
        return true;
    }

    close() {
        this._isOpen = false;
    }

    postpone() {
        this._isOpen = false;
        setTimeout(_ => this.activate(), this.postponeTime);
    }

}
