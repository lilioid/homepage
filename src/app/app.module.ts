import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { AngularFontAwesomeModule } from "angular-font-awesome";

import { AppComponent } from './app.component';
import { WidgetComponent } from './widget/widget.component';
import { DesktopComponent } from './desktop/desktop.component';
import { TaskbarComponent } from './taskbar/taskbar.component';

@NgModule({
  declarations: [
    AppComponent,
    WidgetComponent,
    DesktopComponent,
    TaskbarComponent,
  ],
  imports: [
    BrowserModule,
    AngularFontAwesomeModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
