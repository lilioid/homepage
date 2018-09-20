import {Component, OnInit} from '@angular/core';
import {DesktopService} from "../widgets/desktop.service";
import {TaskbarService} from "./taskbar.service";
import {Widget} from "../widgets/widget";

@Component({
  selector: 'app-taskbar',
  templateUrl: './taskbar.component.html',
  styleUrls: ['./taskbar.component.css']
})
export class TaskbarComponent implements OnInit {

  constructor(public desktopService: DesktopService, public taskbarService: TaskbarService) { }

  ngOnInit() {
  }

  onProgramClicked(program: Widget) {
    if (this.desktopService.isOpen(program) && this.desktopService.isTopWidget(program))
      this.desktopService.close(program);
    else
      this.desktopService.open(program); // .open() also moves widget to top
  }

}
