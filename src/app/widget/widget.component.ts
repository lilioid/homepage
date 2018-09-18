import {Component, HostBinding, OnInit} from '@angular/core';

@Component({
  selector: 'app-widget',
  templateUrl: './widget.component.html',
  styleUrls: [
      './widget.component.css',
  ]
})
@HostBinding('style.width.px')
export class WidgetComponent implements OnInit {

  title:String = "Curriculum Vitae";

  content:String = "I am <i>some</i> content";

  //height = '500px';
  //width = '600px';
  height = 'auto';
  width = 'auto';

  ngOnInit() {

  }

}
