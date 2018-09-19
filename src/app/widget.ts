import {Input, OnInit} from "@angular/core";

export class Widget implements OnInit {

    @Input() height:String = "auto";
    @Input() width: String = "auto";

    ngOnInit(): void {
    }

}
