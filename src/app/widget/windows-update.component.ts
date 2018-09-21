import {AfterViewInit, Component, ElementRef, Input, QueryList, ViewChildren} from '@angular/core';
import {DesktopService} from "./desktop.service";
import {TaskbarService} from "../taskbar/taskbar.service";
import {WidgetComponent} from "./widget.component";

@Component({
    selector: 'app-windows-update',
    templateUrl: './widget.component.html',
    styleUrls: ['./widget.component.css', './windows-update.compoment.css']
})
export class WindowsUpdateComponent extends WidgetComponent implements AfterViewInit{

    @Input() waitTime: number;

    title: string = "Windows Update";

    width: string = "700px";
    posX: string = "38vw";
    posY: string = "30vh";
    dragEnabled: boolean = false;

    @Input() bounds: HTMLElement = null;

    @ViewChildren("controlButtoncontainer") private controlButtoncontainer: QueryList<ElementRef>;
    @ViewChildren("widgetRoot") private widgetRoot: QueryList<ElementRef>;

    constructor(desktopService: DesktopService, taskbarService: TaskbarService) {
        super(desktopService, taskbarService);
    }

    ngOnInit(): void {
        // Show only after specified time
        setTimeout( _ =>  this.open(),this.waitTime*1000);
    }

    ngAfterViewInit(): void {
        this.controlButtoncontainer.changes.subscribe(_ =>
            this.controlButtoncontainer.first.nativeElement.style.display = "None"
        );
    }

    open(): void {
        this.desktopService.open(this);
    }

}
