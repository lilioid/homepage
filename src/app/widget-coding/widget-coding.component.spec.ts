import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { WidgetCodingComponent } from './widget-coding.component';

describe('WidgetCodingComponent', () => {
  let component: WidgetCodingComponent;
  let fixture: ComponentFixture<WidgetCodingComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ WidgetCodingComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(WidgetCodingComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
