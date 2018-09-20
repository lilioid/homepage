import {Injectable} from '@angular/core';
import {WidgetComponent} from "./widget.component";

@Injectable({
  providedIn: 'root'
})
export class DesktopService {

  private widgetStack:Array<WidgetComponent> = [];

  constructor() {

  }

  public open (widget:WidgetComponent): void {
    if (!this.isOpen(widget)) {
        this.widgetStack.push(widget)

    } else {
      this.close(widget);
      this.open(widget);
    }
  }

  public close (widget:WidgetComponent): void {
    this.widgetStack = this.widgetStack.filter(i => widget !== i);
  }

  public isOpen (widget:WidgetComponent): boolean {
    return this.widgetStack.includes(widget);
  }

  public isTopWidget (widget: WidgetComponent): boolean {
    return this.widgetStack[this.widgetStack.length -1] == widget;
  }

  public getPosition (widget: WidgetComponent): number {
    return this.widgetStack.indexOf(widget);
  }

}
