import {Injectable} from '@angular/core';
import {Widget} from "../widgets/widget";

@Injectable({
  providedIn: 'root'
})
export class TaskbarService {

  public programs: Array<Widget> = [];

  constructor() {

  }

  public registerWidget(widget:Widget): void {
    if (!this.programs.includes(widget))
      this.programs.push(widget);
  }

}
