import { ComponentFixture, TestBed } from '@angular/core/testing';

import { RobotsTableComponent } from './robots-table.component';

describe('RobotsTableComponent', () => {
  let component: RobotsTableComponent;
  let fixture: ComponentFixture<RobotsTableComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ RobotsTableComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(RobotsTableComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
