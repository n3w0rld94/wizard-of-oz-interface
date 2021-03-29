import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ActivityModelerComponent } from './activity-modeler.component';

describe('ActivityModelerComponent', () => {
  let component: ActivityModelerComponent;
  let fixture: ComponentFixture<ActivityModelerComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ActivityModelerComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ActivityModelerComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
