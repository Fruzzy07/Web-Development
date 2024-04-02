import { Component } from '@angular/core';
// @ts-ignore
import { RouterOutlet } from '@angular/router';

// @ts-ignore
@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css',
})
export class AppComponent {
  title = 'lab6';
}
