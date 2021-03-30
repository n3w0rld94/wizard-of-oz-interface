import { Component, OnDestroy, OnInit } from '@angular/core';
import { fromEvent, interval, Subscription } from 'rxjs';
import { debounce, filter, map, tap } from 'rxjs/operators';
import { RobotService } from 'src/app/services/robot.service';

@Component({
    selector: 'app-keyboard-joystick',
    templateUrl: './keyboard-joystick.component.html',
    styleUrls: ['./keyboard-joystick.component.css']
})
export class KeyboardJoystickComponent implements OnInit, OnDestroy {
    $keyboardSubscription: Subscription | null = null;
    arrow = 0;

    constructor(private robotService: RobotService) { }

    ngOnInit() {
        console.log('Opened controller');
    }

    initialise_keyboard_controller() {
        console.log('Started controller');
        this.$keyboardSubscription = fromEvent(document, 'keydown').pipe(
            filter((val: any) => [37, 38, 39, 40].includes(val.keyCode)),
            tap(e => e.preventDefault()),
            debounce(val => interval(200)),
            map((e: any) => {
                console.log('Joystick value in map', e.key);
                this.arrow = e.keyCode - 36;
                setTimeout(() => this.arrow = 0, 200);
                return e.keyCode;
            }),
        ).subscribe({
            next: this.showResults.bind(this),
            error: (err) => console.error('error in keyboard controller', err)
        });

    }

    showResults(data: number): void {
        let left = 0;
        let forward = 0;

        if (data === 37) { left = -1; }
        else if (data === 39) { left = +1; }

        if (data === 38) { forward = -1; }
        else if (data === 40) { forward = +1; }

        this.robotService.move(forward, left, 0);
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
