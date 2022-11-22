<template>
  <div>
    <v-toolbar light>
      <v-toolbar-title> Manage Sensors </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn color="primary" to="/main/sensors/create">Create Sensor</v-btn>
    </v-toolbar>
    <v-data-table
      :headers="headers"
      :items="sensors"
      sort-by="id"
      :sort-desc="[true]"
    >
      <!-- eslint-disable-next-line vue/valid-v-slot -->
      <template #item.actions="{ item }">
        <v-btn
          slot="activator"
          icon
          :to="{ name: 'main-sensors-sensor-edit', params: { id: item.id } }"
        >
          <v-icon>mdi-pencil</v-icon>
        </v-btn>
      </template>
    </v-data-table>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";
import { readSensors } from "@/store/sensors/getters";
import { dispatchGetSensors } from "@/store/sensors/actions";

@Component
export default class Sensors extends Vue {
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
      text: "Fruit size",
      sortable: true,
      value: "fruit_size",
      align: "left",
    },
    {
      text: "Medium Energy Consumption",
      sortable: true,
      value: "medium_energy_consumption",
      align: "left",
    },
    {
      text: "Cost",
      sortable: true,
      value: "cost",
      align: "left",
    },
    {
      text: "Brand",
      sortable: true,
      value: "brand",
      align: "left",
    },
    {
      text: "Actions",
      value: "actions",
      sortable: false,
    },
  ];
  get sensors() {
    return readSensors(this.$store);
  }
  public async mounted() {
    await dispatchGetSensors(this.$store);
  }
}
</script>
