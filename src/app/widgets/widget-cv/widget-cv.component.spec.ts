import {async, ComponentFixture, TestBed} from '@angular/core/testing';

import {WidgetCvComponent} from './widget-cv.component';

describe('WidgetComponent', () => {
  let component: WidgetCvComponent;
  let fixture: ComponentFixture<WidgetCvComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ WidgetCvComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(WidgetCvComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
