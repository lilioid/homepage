import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { AngularFontAwesomeModule } from "angular-font-awesome";

import { AppComponent } from './app.component';
import { WidgetCvComponent } from './widget-cv/widget-cv.component';
import { DesktopComponent } from './desktop/desktop.component';
import { TaskbarComponent } from './taskbar/taskbar.component';
import { WidgetContactComponent } from './widget-contact/widget-contact.component';

@NgModule({
  declarations: [
    AppComponent,
    WidgetCvComponent,
    DesktopComponent,
    TaskbarComponent,
    WidgetContactComponent,
  ],
  imports: [
    BrowserModule,
    AngularFontAwesomeModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
