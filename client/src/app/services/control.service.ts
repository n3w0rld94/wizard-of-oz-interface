import { Injectable } from '@angular/core';
import { Socket } from 'ngx-socket-io';
import { webSocket } from 'rxjs/webSocket';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})
export class WoZSocket extends Socket {

  constructor() {
    super({ url: 'ws://127.0.0.1:' + environment.webSocketPort + '/', options: {} });
  }

}

@Injectable({
  providedIn: 'root'
})
export class ControlService {

  constructor(private socket: WoZSocket) {}

  startVideoStream() {
    console.log('called startVideoStream');
    const url = 'stream-video';
    this.socket.emit('message', 'start');
    this.socket.fromEvent('message').subscribe({
      next: (result) => console.log('Received: ', result)
    });
  }
}
