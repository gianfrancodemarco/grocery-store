<template>
  <div>
    <v-toolbar light>
      <v-toolbar-title> Manage Fruits </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn color="primary" to="/main/fruits/create">Create Fruit</v-btn>
    </v-toolbar>
    <v-data-table :headers="headers" :items="fruits">
      <!-- eslint-disable-next-line vue/valid-v-slot -->
      <template #item.actions="{ item }">
        <v-btn
          slot="activator"
          icon
          :to="{ name: 'main-fruits-fruit-edit', params: { id: item.id } }"
        >
          <v-icon>mdi-pencil</v-icon>
        </v-btn>
      </template>
    </v-data-table>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";
import { readFruits } from "@/store/fruits/getters";
import { dispatchGetFruits } from "@/store/fruits/actions";

@Component
export default class Fruits extends Vue {
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
      text: "Peel Type",
      sortable: true,
      value: "peel_type",
      align: "left",
    },
    {
      text: "Actions",
      value: "actions",
      sortable: false,
    },
  ];
  get fruits() {
    return readFruits(this.$store);
  }
  public async mounted() {
    await dispatchGetFruits(this.$store);
  }
}
</script>
