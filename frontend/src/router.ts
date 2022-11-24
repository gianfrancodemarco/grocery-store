import Vue from "vue";
import Router from "vue-router";

import RouterComponent from "./components/RouterComponent.vue";
import Fruits from "./views/main/fruit/Fruits.vue";
import CreateFruit from "./views/main/fruit/CreateFruit.vue";
import EditFruit from "./views/main/fruit/EditFruit.vue";
import Lots from "./views/main/lot/Lots.vue";
import CreateLot from "./views/main/lot/CreateLot.vue";
import EditLot from "./views/main/lot/EditLot.vue";
import Allergies from "./views/main/allergy/Allergies.vue";
import CreateAllergy from "./views/main/allergy/CreateAllergy.vue";
import EditAllergy from "./views/main/allergy/EditAllergy.vue";
import Recipes from "./views/main/recipe/Recipes.vue";
import CreateRecipe from "./views/main/recipe/CreateRecipe.vue";
import EditRecipe from "./views/main/recipe/EditRecipe.vue";
import Sensors from "./views/main/sensor/Sensors.vue";
import CreateSensor from "./views/main/sensor/CreateSensor.vue";
import EditSensor from "./views/main/sensor/EditSensor.vue";
import Notifications from "./views/main/notifications/Notifications.vue";

Vue.use(Router);

export default new Router({
  mode: "history",
  base: process.env.BASE_URL,
  routes: [
    {
      path: "/",
      component: () => import(/* webpackChunkName: "start" */ "./views/main/Start.vue"),
      children: [
        {
          path: "login",
          // route level code-splitting
          // this generates a separate chunk (about.[hash].js) for this route
          // which is lazy-loaded when the route is visited.
          component: () => import(/* webpackChunkName: "login" */ "./views/Login.vue"),
        },
        {
          path: "recover-password",
          component: () =>
            import(
              /* webpackChunkName: "recover-password" */ "./views/PasswordRecovery.vue"
            ),
        },
        {
          path: "reset-password",
          component: () =>
            import(
              /* webpackChunkName: "reset-password" */ "./views/ResetPassword.vue"
            ),
        },
        {
          path: "main",
          component: () =>
            import(/* webpackChunkName: "main" */ "./views/main/Main.vue"),
          children: [
            {
              path: "fruits",
              component: Fruits,
            },
            {
              path: "fruits/edit/:id",
              name: "main-fruits-fruit-edit",
              component: EditFruit,
            },
            {
              path: "fruits/create",
              name: "main-fruits-create",
              component: CreateFruit,
            },
            {
              path: "lots",
              component: Lots,
            },
            {
              path: "lots/edit/:id",
              name: "main-lots-lot-edit",
              component: EditLot,
            },
            {
              path: "lots/create",
              name: "main-lots-create",
              component: CreateLot,
            },
            {
              path: "allergies",
              component: Allergies,
            },
            {
              path: "allergies/edit/:id",
              name: "main-allergies-allergy-edit",
              component: EditAllergy,
            },
            {
              path: "allergies/create",
              name: "main-allergies-create",
              component: CreateAllergy,
            },
            {
              path: "recipes",
              component: Recipes,
            },
            {
              path: "recipes/edit/:id",
              name: "main-recipes-recipe-edit",
              component: EditRecipe,
            },
            {
              path: "recipes/create",
              name: "main-recipes-create",
              component: CreateRecipe,
            },
            {
              path: "sensors",
              component: Sensors,
            },
            {
              path: "sensors/edit/:id",
              name: "main-sensors-sensor-edit",
              component: EditSensor,
            },
            {
              path: "sensors/create",
              name: "main-sensors-create",
              component: CreateSensor,
            },
            {
              path: "profile",
              component: RouterComponent,
              redirect: "profile/view",
              children: [
                {
                  path: "notifications",
                  component: Notifications,
                },
                {
                  path: "view",
                  component: () =>
                    import(
                      /* webpackChunkName: "main-profile" */ "./views/main/profile/UserProfile.vue"
                    ),
                },
                {
                  path: "edit",
                  component: () =>
                    import(
                      /* webpackChunkName: "main-profile-edit" */ "./views/main/profile/UserProfileEdit.vue"
                    ),
                },
                {
                  path: "password",
                  component: () =>
                    import(
                      /* webpackChunkName: "main-profile-password" */ "./views/main/profile/UserProfileEditPassword.vue"
                    ),
                },
              ],
            },
            {
              path: "admin",
              component: () =>
                import(
                  /* webpackChunkName: "main-admin" */ "./views/main/admin/Admin.vue"
                ),
              redirect: "admin/users/all",
              children: [
                {
                  path: "users",
                  redirect: "users/all",
                },
                {
                  path: "users/all",
                  component: () =>
                    import(
                      /* webpackChunkName: "main-admin-users" */ "./views/main/admin/AdminUsers.vue"
                    ),
                },
                {
                  path: "users/edit/:id",
                  name: "main-admin-users-edit",
                  component: () =>
                    import(
                      /* webpackChunkName: "main-admin-users-edit" */ "./views/main/admin/EditUser.vue"
                    ),
                },
                {
                  path: "users/create",
                  name: "main-admin-users-create",
                  component: () =>
                    import(
                      /* webpackChunkName: "main-admin-users-create" */ "./views/main/admin/CreateUser.vue"
                    ),
                },
              ],
            },
          ],
        },
      ],
    },
    {
      path: "/*",
      redirect: "/",
    },
  ],
});
