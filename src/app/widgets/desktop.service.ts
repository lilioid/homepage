import {Injectable} from '@angular/core';
import {Widget} from "./widget";

@Injectable({
  providedIn: 'root'
})
export class DesktopService {

  private widgetStack:Array<Widget> = [];

  constructor() {

  }

  public open (widget:Widget): void {
    if (!this.isOpen(widget)) {
        this.widgetStack.push(widget)

    } else {
      this.close(widget);
      this.open(widget);
    }
  }

  public close (widget:Widget): void {
    this.widgetStack = this.widgetStack.filter(i => widget !== i);
  }

  public isOpen (widget:Widget): boolean {
    return this.widgetStack.includes(widget);
  }

  public isTopWidget (widget: Widget): boolean {
    return this.widgetStack[this.widgetStack.length -1] == widget;
  }

  public getPosition (widget: Widget): number {
    return this.widgetStack.indexOf(widget);
  }

}
