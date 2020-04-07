import {Route} from 'vue-router';
import _ from 'lodash';
import Vue, {VueConstructor} from 'vue';


export const TaskManager = {
  install: function (vue: VueConstructor, options: any): void {
    vue.prototype.$isAppOpen = this.isAppOpen;
    vue.prototype.$toggleApp = this.toggleApp;
    vue.prototype.$isAppMaximized = this.isAppMaximized;
    vue.prototype.$isAppOnTop = this.isAppOnTop;
    vue.prototype.$raiseApp = this.raiseApp;
    vue.prototype.$toggleAppMaximized = this.toggleAppMaximized;
    vue.prototype.$getAppStackIndex = this.getAppStackIndex;
  },

  isAppOpen: function (this: Vue, appName: string): boolean {
    const query = this.$route.query.app;

    return ((typeof query === 'string' && query.toLowerCase() === appName))
      || (query instanceof Array && query.includes(appName));
  },

  isAppOnTop: function (this: Vue, appName: string): boolean {
    const query = this.$route.query.app;
    const maximized = this.$route.query.maximized;

    return (this.$isAppOpen(appName)
      && maximized === undefined
      && (typeof query === 'string'
        || query[query.length - 1] === appName))
      || this.$isAppMaximized(appName);
  },

  isAppMaximized: function (this: Vue, appName: string): boolean {
    const query = this.$route.query.maximized;
    return query != undefined && (query === appName || query.includes(appName));
  },

  getAppStackIndex: function (this: Vue, appName: string): number {
    const baseIndex = 10;

    if (!this.$isAppOpen(appName)) {
      throw new Error(`App ${appName} is not even open and therefore not on the stack`)
    }

    const query = this.$route.query.app;
    const maximizedApp = this.$route.query.maximized;

    if (typeof query === 'string') {
      return baseIndex;
    } else {
      if (maximizedApp === undefined)
        return baseIndex + query.indexOf(appName);
      else {
        return this.$isAppMaximized(appName) ? baseIndex + 30 : baseIndex;
      }
    }
  },

  toggleApp: function (this: Vue, appName: string): Promise<Route> {
    const query = _.cloneDeep(this.$route.query);

    if (this.$isAppOpen(appName)) {
      if (query.app instanceof Array) {
        query.app = query.app.filter((i) => i && i.toLowerCase() !== appName);
      } else {
        delete query.app;
      }
    } else {
      if (query.app instanceof Array) {
        query.app.push(appName);
      } else if (typeof query.app === 'string') {
        query.app = [query.app, appName];
      } else {
        query.app = appName;
      }
    }

    return this.$router.replace({query});
  },

  raiseApp: function (this: Vue, appName: string): Promise<Route> {
    const query = _.cloneDeep(this.$route.query);

    if (this.$isAppOnTop(appName)) {
      return Promise.resolve(this.$route);
    }

    if (!this.$isAppOpen(appName)) {
      if (query.app instanceof Array) {
        query.app.push(appName);
      } else if (typeof query.app === 'string') {
        query.app = [appName, query.app];
      } else {
        query.app = appName;
      }

    } else {
      if (query.app instanceof Array) {
        query.app = query.app.filter((i) => i && i !== appName);
        query.app.push(appName);
      }
    }

    return this.$router.replace({query});
  },

  toggleAppMaximized: function (this: Vue, appName: string): Promise<Route> {
    const query = _.cloneDeep(this.$route.query);

    if (this.$isAppMaximized(appName)) {
      delete query.maximized;
    } else {
      query.maximized = appName;
    }

    return this.$router.replace({query});
  }
};
export default TaskManager;
