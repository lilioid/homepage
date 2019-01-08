import {BrowserModule} from '@angular/platform-browser';
import {NgModule} from '@angular/core';
import {AngularFontAwesomeModule} from "angular-font-awesome";
import {AngularDraggableModule} from "angular2-draggable";

import {AppComponent} from './app.component';
import {DesktopComponent} from './desktop/desktop.component';
import {TaskbarComponent} from './taskbar/taskbar.component';
import {WidgetComponent} from './widget/widget.component';
import {StartMenuComponent} from './taskbar/start-menu/start-menu.component';

@NgModule({
  declarations: [
    AppComponent,
    DesktopComponent,
    TaskbarComponent,
    WidgetComponent,
    StartMenuComponent,
  ],
  imports: [
    BrowserModule,
    AngularFontAwesomeModule,
    AngularDraggableModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
