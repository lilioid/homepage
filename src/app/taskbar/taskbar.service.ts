import {Injectable} from '@angular/core';
import {Widget} from "../widgets/widget";

@Injectable({
  providedIn: 'root'
})
export class TaskbarService {

  constructor() {

  }

  public registerWidget(widget:Widget): void {
    //alert("New widget registered")
  }

}
