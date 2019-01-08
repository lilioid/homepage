import {BrowserModule} from '@angular/platform-browser';
import {NgModule} from '@angular/core';
import {AngularFontAwesomeModule} from "angular-font-awesome";
import {AngularDraggableModule} from "angular2-draggable";

import {AppComponent} from './app.component';
import {DesktopComponent} from './desktop/desktop.component';
import {TaskbarComponent} from './taskbar/taskbar.component';
import {WidgetComponent} from './widget/widget.component';
import {StartMenuComponent} from './taskbar/start-menu/start-menu.component';
import {ContactComponent} from './widget/contents/contact/contact.component';
import {CodingComponent} from './widget/contents/coding/coding.component';
import {CvComponent} from './widget/contents/cv/cv.component';
import {ImprintComponent} from './widget/contents/imprint/imprint.component';

@NgModule({
  declarations: [
    AppComponent,
    DesktopComponent,
    TaskbarComponent,
    WidgetComponent,
    StartMenuComponent,
    ContactComponent,
    CodingComponent,
    CvComponent,
    ImprintComponent,
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
