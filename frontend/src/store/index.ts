import Vue from "vue";
import Vuex, { StoreOptions } from "vuex";

import { mainModule } from "./main";
import { State } from "./state";
import { adminModule } from "./admin";
import { fruitsModule } from "./fruits";
import { lotsModule } from "./lots";
import { allergiesModule } from "./allergies";
import { recipesModule } from "./recipes";
import { sensorsModule } from "./sensors";
import { notificationsModule } from "./notifications";

Vue.use(Vuex);

const storeOptions: StoreOptions<State> = {
  modules: {
    main: mainModule,
    admin: adminModule,
    fruits: fruitsModule,
    lots: lotsModule,
    allergies: allergiesModule,
    recipes: recipesModule,
    sensors: sensorsModule,
    notifications: notificationsModule
  },
};

export const store = new Vuex.Store<State>(storeOptions);

export default store;
