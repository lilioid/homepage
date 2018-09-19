import {BrowserModule} from '@angular/platform-browser';
import {NgModule} from '@angular/core';
import {AngularFontAwesomeModule} from "angular-font-awesome";

import {AppComponent} from './app.component';
import {TaskbarComponent} from './taskbar/taskbar.component';
import {WidgetCvComponent} from './widgets/widget-cv/widget-cv.component';
import {WidgetContactComponent} from './widgets/widget-contact/widget-contact.component';
import {WidgetCodingComponent} from './widgets/widget-coding/widget-coding.component';
import {WidgetImprintComponent} from './widgets/widget-imprint/widget-imprint.component';
import {AngularDraggableModule} from "angular2-draggable";

@NgModule({
  declarations: [
    AppComponent,
    TaskbarComponent,
    WidgetCvComponent,
    WidgetContactComponent,
    WidgetCodingComponent,
    WidgetImprintComponent,
  ],
  imports: [
    BrowserModule,
    AngularFontAwesomeModule,
    AngularDraggableModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
