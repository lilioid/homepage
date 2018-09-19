import {async, ComponentFixture, TestBed} from '@angular/core/testing';

import {WidgetImprintComponent} from './widget-imprint.component';

describe('WidgetImprintComponent', () => {
  let component: WidgetImprintComponent;
  let fixture: ComponentFixture<WidgetImprintComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ WidgetImprintComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(WidgetImprintComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
