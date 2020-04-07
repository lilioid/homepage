import Vue from 'vue';
import {Route} from 'vue-router';

declare module 'vue/types/vue' {
  interface Vue {
    $isAppOpen: (appName: string) => boolean
    $isAppOnTop: (appName: string) => boolean
    $isAppMaximized: (appName: string) => boolean
    $toggleApp: (appName: string) => Promise<Route>
    $raiseApp: (appName: string) => Promise<Route>
    $toggleAppMaximized: (appName: string) => Promise<Route>
    $getAppStackIndex: (appName: string) => number
  }
}
