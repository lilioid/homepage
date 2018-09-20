import {Injectable} from '@angular/core';
import {WidgetComponent} from "../widget/widget.component";

@Injectable({
  providedIn: 'root'
})
export class TaskbarService {

  public programs: Array<WidgetComponent> = [];

  constructor() {

  }

  public registerWidget(widget:WidgetComponent): void {
    if (!this.programs.includes(widget))
      this.programs.push(widget);
  }

}
