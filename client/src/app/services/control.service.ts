import { Injectable } from '@angular/core';
import { Socket } from 'ngx-socket-io';
import { webSocket } from 'rxjs/webSocket';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})
export class WoZSocket extends Socket {

  constructor() {
    super({ url: 'ws://127.0.0.1:' + environment.webSocketPort + '/', options: { autoConnect: false} });
  }

}

@Injectable({
  providedIn: 'root'
})
export class ControlService {

  constructor(private socket: WoZSocket) {}

  startVideoStream() {
    console.log('called startVideoStream');
    this.socket.ioSocket.io.opts.query = { username: 'if2002@hw.ac.uk' };
    this.socket.connect();
    this.socket.emit('message', 'start');
    this.socket.fromEvent('message').subscribe({
      next: (result) => console.log('Received: ', result)
    });
  }
}
