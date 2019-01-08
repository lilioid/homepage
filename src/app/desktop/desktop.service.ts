import {Injectable} from '@angular/core';
import {WidgetComponent} from "../widget/widget.component";

@Injectable({
    providedIn: 'root'
})
export class DesktopService {

    private widgetStack: WidgetComponent[] = [];

    constructor() {
    }

    public open(widget: WidgetComponent) {
        if (!this.isOpen(widget)) {
            this.widgetStack.push(widget);
        } else {
            this.close(widget);
            this.open(widget);
        }
    }

    public isOpen(widget: WidgetComponent) {
        return this.widgetStack.includes(widget);
    }

    public isTopWidget(widget: WidgetComponent) {
        return this.widgetStack[this.widgetStack.length-1] === widget;
    }

    public close(widget: WidgetComponent) {
        this.widgetStack = this.widgetStack.filter( i => i !== widget );
    }

    public getPosition(widget: WidgetComponent) {
        return this.widgetStack.indexOf(widget)
    }

}
