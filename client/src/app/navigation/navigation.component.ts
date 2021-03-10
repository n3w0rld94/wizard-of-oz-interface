import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-navigation',
  templateUrl: './navigation.component.html',
  styleUrls: ['./navigation.component.css']
})
export class NavigationComponent implements OnInit {
  title = 'Tic Tac Toe';
  isAuthenticated: boolean;

  constructor() { }

  ngOnInit(): void {
  }

  logOut() {

  }

}
