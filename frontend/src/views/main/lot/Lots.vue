<template>
  <div>
    <v-toolbar light>
      <v-toolbar-title> Manage Lots </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn color="primary" to="/main/lots/create">Create Lot</v-btn>
    </v-toolbar>
    <v-data-table :headers="headers" :items="lots">
      <!-- eslint-disable-next-line vue/valid-v-slot -->
      <template #item.actions="{ item }">
        <v-btn
          slot="activator"
          icon
          :to="{ name: 'main-lots-lot-edit', params: { id: item.id } }"
        >
          <v-icon>mdi-pencil</v-icon>
        </v-btn>
      </template>
    </v-data-table>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";
import { readLots } from "@/store/lots/getters";
import { dispatchGetLots } from "@/store/lots/actions";

@Component
export default class Lots extends Vue {
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
      text: "Fruit id",
      sortable: true,
      value: "fruit_id",
      align: "left",
    },
    {
      text: "Actions",
      value: "actions",
      sortable: false,
    },
  ];
  get lots() {
    return readLots(this.$store);
  }
  public async mounted() {
    await dispatchGetLots(this.$store);
  }
}
</script>
