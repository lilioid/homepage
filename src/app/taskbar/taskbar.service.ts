import {Injectable} from '@angular/core';
import {WidgetComponent} from "../widget/widget.component";

@Injectable({
    providedIn: 'root'
})
export class TaskbarService {

    public widgets: WidgetComponent[] = [];

    constructor() {
    }

    public registerWidget(widget: WidgetComponent): void {
        if (!this.widgets.includes(widget))
            this.widgets.push(widget)
    }
}
