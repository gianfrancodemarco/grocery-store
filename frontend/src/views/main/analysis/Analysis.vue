<template>
  <div>
    <v-toolbar light>
      <v-toolbar-title> Manage Analysis </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn color="primary" to="/main/analysiss/create">Create Analysis</v-btn>
    </v-toolbar>
    <v-data-table
      :headers="headers"
      :items="analysiss"
      sort-by="id"
      :sort-desc="[true]"
    >
      <!-- eslint-disable-next-line vue/valid-v-slot -->
      <template #item.actions="{ item }">
        <v-btn
          slot="activator"
          icon
          :to="{ name: 'main-analysiss-analysis-edit', params: { id: item.id } }"
        >
          <v-icon>mdi-pencil</v-icon>
        </v-btn>
      </template>
    </v-data-table>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";
import { readAnalysiss } from "@/store/analysiss/getters";
import { dispatchGetAnalysiss } from "@/store/analysiss/actions";

@Component
export default class Analysiss extends Vue {
  public headers = [
    {
      text: "Id",
      sortable: true,
      value: "id",
      align: "left",
    },
    {
      text: "Lot id",
      sortable: true,
      value: "lot_id",
      align: "left",
    },
    {
      text: "Sensor id",
      sortable: true,
      value: "sensor_id",
      align: "left",
    },
    {
      text: "Description",
      sortable: true,
      value: "description",
      align: "left",
    },
    {
      text: "Actions",
      value: "actions",
      sortable: false,
    },
  ];
  get analysiss() {
    return readAnalysiss(this.$store);
  }
  public async mounted() {
    await dispatchGetAnalysiss(this.$store);
  }
}
</script>
