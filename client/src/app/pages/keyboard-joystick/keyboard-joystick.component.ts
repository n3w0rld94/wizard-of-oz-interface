import { Component, OnDestroy, OnInit } from '@angular/core';
import { fromEvent, interval, Subscription } from 'rxjs';
import { map, throttle } from 'rxjs/operators';
import { RobotService } from 'src/app/services/robot.service';

@Component({
  selector: 'app-keyboard-joystick',
  templateUrl: './keyboard-joystick.component.html',
  styleUrls: ['./keyboard-joystick.component.css']
})
export class KeyboardJoystickComponent implements OnInit, OnDestroy {
  $keyboardSubscription: Subscription | null = null;

  constructor(private robotService: RobotService) { }

  ngOnInit() {
    console.log('Opened controller');
  }

  initialise_keyboard_controller() {
    console.log('Started controller');
    const input = document.getElementById('input') as HTMLElement;

    this.$keyboardSubscription = fromEvent(input, 'onkeydown').pipe(
      throttle(val => interval(300)),
      // filter(val => console.log(e.target.value) )
      map((e: any) => {
        console.log('Joystick value in map', e.target.value)
        return e.target.value;
      }),
      // switchMap(val => of(val))
    ).subscribe({
      next: showResults,
      error: (err) => console.error('error in keyboard controller', err)
    });

    function showResults(data: any[]): void {
      console.log('data from keyboard', data);
      this.control
    }
  }

  stop_keyboard_controller() {
    console.log('Stopped controller');
    if (this.$keyboardSubscription) {
      this.$keyboardSubscription.unsubscribe();
      this.$keyboardSubscription = null;
    }
  }

  ngOnDestroy() {
    console.log('Closed controller');
    this.stop_keyboard_controller();
  }
}
