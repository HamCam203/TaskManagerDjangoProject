import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { PublicService} from './services/public.service';

@Component({
  selector: 'app-root',
  imports: [RouterOutlet],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'frontend';
  msg : any;

  constructor(private publicService: PublicService) {
    // Initialization logic can go here if needed

  }

  ngOnInit():void {
    // This method can be used for any initialization after the component is created
    this.showMessage();
  }

  showMessage() {
    this.publicService.getmessage().subscribe(
      (response: any) => {
        this.msg = response;
        console.log(this.msg);
      },
      (error: any) => {
        console.error('Error fetching message:', error);
      }
    );
  }
}
