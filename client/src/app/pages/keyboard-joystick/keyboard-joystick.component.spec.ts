import { ComponentFixture, TestBed } from '@angular/core/testing';

import { KeyboardJoystickComponent } from './keyboard-joystick.component';

describe('KeyboardJoystickComponent', () => {
  let component: KeyboardJoystickComponent;
  let fixture: ComponentFixture<KeyboardJoystickComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ KeyboardJoystickComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(KeyboardJoystickComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
