import {Component, OnInit} from '@angular/core';
import {FormBuilder, FormGroup, Validators} from "@angular/forms"
import {AuthenticationService} from "../services/authentication/authentication.service"
import {Router} from "@angular/router"
import {CookieService} from "angular2-cookie/core";

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {

  loginForm: FormGroup;
  showRegistrationForm = false;

  constructor(private formBuilder: FormBuilder, private authenticationService: AuthenticationService, private router: Router, private cookieService: CookieService) {
    this.loginForm = formBuilder.group({
      'email': [null, Validators.required],
      'password': [null, Validators.compose([Validators.required, Validators.minLength(6)])]
    })
  }

  ngOnInit() {
    this.authenticationService.isLoggedIn().subscribe(response => {
      if (response) {
        this.router.navigate(['/home']);
      }
    });
  }

  loginUser() {
    console.log("Attempting to login user");
    this.authenticationService.loginUser(this.loginForm.value)
      .subscribe((response) => {
        console.log('User successfully logged in, user details below...');
        this.authenticationService.isLoggedInChecker$.next(!!this.cookieService.get('user'));
        this.router.navigate(['/home']);
      }, (err) => {
        console.log('User logged in failed...reasons below...');
        this.authenticationService.isLoggedInChecker$.next(false);
      });
  }

}
