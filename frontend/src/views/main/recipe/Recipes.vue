<template>
  <div>
    <v-toolbar light>
      <v-toolbar-title> Manage Recipes </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn color="primary" to="/main/recipes/create">Create Recipe</v-btn>
    </v-toolbar>
    <v-data-table :headers="headers" :items="recipes">
      <!-- eslint-disable-next-line vue/valid-v-slot -->
      <template #item.actions="{ item }">
        <v-btn
          slot="activator"
          icon
          :to="{ name: 'main-recipes-recipe-edit', params: { id: item.id } }"
        >
          <v-icon>mdi-pencil</v-icon>
        </v-btn>
      </template>
      <!-- eslint-disable-next-line vue/valid-v-slot -->
      <template #item.fruits="{ item }">
        {{ item.fruits.map((el) => el.name).join(", ") }}
      </template>
    </v-data-table>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";
import { readRecipes } from "@/store/recipes/getters";
import { dispatchGetRecipes } from "@/store/recipes/actions";

@Component
export default class Recipes extends Vue {
  public headers = [
    {
      text: "Id",
      sortable: true,
      value: "id",
      align: "left",
    },
    {
      text: "Name",
      sortable: true,
      value: "name",
      align: "left",
    },
    {
      text: "Description",
      sortable: true,
      value: "description",
      align: "left",
    },
    {
      text: "Budget",
      sortable: true,
      value: "budget",
      align: "left",
    },
    {
      text: "Fruits used by this recipe",
      sortable: true,
      value: "fruits",
      align: "left",
    },
    {
      text: "Actions",
      value: "actions",
      sortable: false,
    },
  ];
  get recipes() {
    return readRecipes(this.$store);
  }
  public async mounted() {
    await dispatchGetRecipes(this.$store);
  }
}
</script>
