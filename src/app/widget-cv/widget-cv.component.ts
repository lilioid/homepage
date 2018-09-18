import {Component, Input, OnInit} from '@angular/core';

@Component({
  selector: 'app-widget-cv',
  templateUrl: './widget-cv.component.html',
  styleUrls: ['./widget-cv.component.css', '../widget.css']
})
export class WidgetCvComponent implements OnInit {
  @Input() height = 'auto';
  @Input() width = 'auto';

  ngOnInit() {

  }

}
