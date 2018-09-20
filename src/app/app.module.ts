import {BrowserModule} from '@angular/platform-browser';
import {NgModule} from '@angular/core';
import {AngularFontAwesomeModule} from "angular-font-awesome";

import {AppComponent} from './app.component';
import {TaskbarComponent} from './taskbar/taskbar.component';
import {AngularDraggableModule} from "angular2-draggable";
import {HttpClientModule} from "@angular/common/http";
import {WidgetComponent} from './widget/widget.component';

@NgModule({
  declarations: [
    AppComponent,
    TaskbarComponent,
    WidgetComponent,
  ],
  imports: [
    BrowserModule,
    AngularFontAwesomeModule,
    AngularDraggableModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
