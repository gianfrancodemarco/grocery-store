<template>
  <div>
    <v-toolbar light>
      <v-toolbar-title> Manage Allergies </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn color="primary" to="/main/allergies/create">Create Allergy</v-btn>
    </v-toolbar>
    <v-data-table
      :headers="headers"
      :items="allergies"
      sort-by="id"
      :sort-desc="[true]"
    >
      <!-- eslint-disable-next-line vue/valid-v-slot -->
      <template #item.actions="{ item }">
        <v-btn
          slot="activator"
          icon
          :to="{ name: 'main-allergies-allergy-edit', params: { id: item.id } }"
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
import { readAllergies } from "@/store/allergies/getters";
import { dispatchGetAllergies } from "@/store/allergies/actions";

@Component
export default class Allergies extends Vue {
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
      text: "Symptoms",
      sortable: true,
      value: "symptoms",
      align: "left",
    },
    {
      text: "Fruits that can cause this allergy",
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
  get allergies() {
    return readAllergies(this.$store);
  }
  public async mounted() {
    await dispatchGetAllergies(this.$store);
  }
}
</script>
