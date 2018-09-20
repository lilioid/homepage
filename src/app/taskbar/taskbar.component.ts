import {Component, OnInit} from '@angular/core';
import {DesktopService} from "../widget/desktop.service";
import {TaskbarService} from "./taskbar.service";
import {WidgetComponent} from "../widget/widget.component";

@Component({
  selector: 'app-taskbar',
  templateUrl: './taskbar.component.html',
  styleUrls: ['./taskbar.component.css']
})
export class TaskbarComponent implements OnInit {

  constructor(public desktopService: DesktopService, public taskbarService: TaskbarService) { }

  ngOnInit() {
  }

  onProgramClicked(program: WidgetComponent) {
    if (this.desktopService.isOpen(program) && this.desktopService.isTopWidget(program))
      this.desktopService.close(program);
    else
      this.desktopService.open(program); // .open() also moves widget to top
  }

}
