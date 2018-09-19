import {async, ComponentFixture, TestBed} from '@angular/core/testing';

import {WidgetContactComponent} from './widget-contact.component';

describe('WidgetContactComponent', () => {
  let component: WidgetContactComponent;
  let fixture: ComponentFixture<WidgetContactComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ WidgetContactComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(WidgetContactComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
