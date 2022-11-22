<template>
  <div>
    <v-navigation-drawer
      v-model="showDrawer"
      persistent
      :mini-variant="miniDrawer"
      fixed
      app
    >
      <v-layout column fill-height>
        <v-list>
          <v-subheader>Main menu</v-subheader>
          <v-list-item to="/main/lots">
            <v-list-item-action>
              <v-icon>mdi-land-plots</v-icon>
            </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title>Lots</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
          <v-list-item to="/main/fruits">
            <v-list-item-action>
              <v-icon>mdi-fruit-cherries</v-icon>
            </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title>Fruits</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
          <v-list-item to="/main/allergies">
            <v-list-item-action>
              <v-icon>mdi-flower-pollen</v-icon>
            </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title>Allergies</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
          <v-list-item to="/main/recipes">
            <v-list-item-action>
              <v-icon>mdi-format-list-bulleted</v-icon>
            </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title>Recipes</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
          </v-list>
          <v-list subheader>
            <v-subheader>Profile</v-subheader>   
            <v-list-item to="/main/profile/view">
              <v-list-item-action>
                <v-icon>mdi-account</v-icon>
              </v-list-item-action>
              <v-list-item-content>
                <v-list-item-title>View Profile</v-list-item-title>
              </v-list-item-content>
            </v-list-item>
            <v-list-item to="/main/profile/edit">
              <v-list-item-action>
                <v-icon>mdi-pencil</v-icon>
              </v-list-item-action>
              <v-list-item-content>
                <v-list-item-title>Edit Profile</v-list-item-title>
              </v-list-item-content>
            </v-list-item>
            <v-list-item to="/main/profile/password">
              <v-list-item-action>
                <v-icon>mdi-key</v-icon>
              </v-list-item-action>
              <v-list-item-content>
                <v-list-item-title>Change Password</v-list-item-title>
              </v-list-item-content>
            </v-list-item>
          </v-list>
        <v-divider></v-divider>
        <v-list v-show="hasAdminAccess" subheader>
          <v-subheader>Admin</v-subheader>
          <v-list-item to="/main/admin/users/all">
            <v-list-item-action>
              <v-icon>mdi-account-multiple</v-icon>
            </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title>Manage Operators</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list>
        <v-spacer></v-spacer>
        <v-list>
          <v-list-item @click="logout">
            <v-list-item-action>
              <v-icon>mdi-close</v-icon>
            </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title>Logout</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
          <v-divider></v-divider>
          <v-list-item @click="switchMiniDrawer">
            <v-list-item-action>
              <v-icon>{{
                miniDrawer ? "mdi-chevron-right" : "mdi-chevron-left"
              }}</v-icon>
            </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title>Collapse</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list>
      </v-layout>
    </v-navigation-drawer>
    <v-app-bar dark color="primary" app>
      <v-app-bar-nav-icon @click.stop="switchShowDrawer"></v-app-bar-nav-icon>
      <v-toolbar-title>{{ appName }}</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-menu bottom left offset-y>
        <template #activator="{ on }">
          <v-btn icon v-on="on">
            <v-icon>mdi-dots-vertical</v-icon>
          </v-btn>
        </template>
        <v-list>
          <v-list-item to="/main/profile">
            <v-list-item-content>
              <v-list-item-title>Profile</v-list-item-title>
            </v-list-item-content>
            <v-list-item-action>
              <v-icon>mdi-account</v-icon>
            </v-list-item-action>
          </v-list-item>
          <v-list-item @click="logout">
            <v-list-item-content>
              <v-list-item-title>Logout</v-list-item-title>
            </v-list-item-content>
            <v-list-item-action>
              <v-icon>mdi-close</v-icon>
            </v-list-item-action>
          </v-list-item>
        </v-list>
      </v-menu>
    </v-app-bar>
    <v-main>
      <router-view :key="$route.fullPath"></router-view>
    </v-main>
    <v-footer class="pa-3" fixed app>
      <v-spacer></v-spacer>
      <span>&copy; {{ appName }}</span>
    </v-footer>
  </div>
</template>

<script lang="ts">
import { Vue, Component } from "vue-property-decorator";

import { appName } from "@/env";
import {
  readDashboardMiniDrawer,
  readDashboardShowDrawer,
  readHasAdminAccess,
} from "@/store/main/getters";
import {
  commitSetDashboardShowDrawer,
  commitSetDashboardMiniDrawer,
} from "@/store/main/mutations";
import { dispatchUserLogOut } from "@/store/main/actions";

const routeGuardMain = async (to, from, next) => {
  if (to.path === "/main") {
    next("/main/lots");
  } else {
    next();
  }
};

@Component
export default class Main extends Vue {
  public appName = appName;

  public beforeRouteEnter(to, from, next) {
    routeGuardMain(to, from, next);
  }

  public beforeRouteUpdate(to, from, next) {
    routeGuardMain(to, from, next);
  }

  get miniDrawer() {
    return readDashboardMiniDrawer(this.$store);
  }

  get showDrawer() {
    return readDashboardShowDrawer(this.$store);
  }

  set showDrawer(value) {
    commitSetDashboardShowDrawer(this.$store, value);
  }

  public switchShowDrawer() {
    commitSetDashboardShowDrawer(this.$store, !readDashboardShowDrawer(this.$store));
  }

  public switchMiniDrawer() {
    commitSetDashboardMiniDrawer(this.$store, !readDashboardMiniDrawer(this.$store));
  }

  public get hasAdminAccess() {
    return readHasAdminAccess(this.$store);
  }

  public async logout() {
    await dispatchUserLogOut(this.$store);
  }
}
</script>
