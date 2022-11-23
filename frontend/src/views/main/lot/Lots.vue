<template>
  <div>
    <v-toolbar light>
      <v-toolbar-title> Manage Lots </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn color="primary" to="/main/lots/create">Create Lot</v-btn>
    </v-toolbar>
    <v-data-table :headers="headers" :items="lots" sort-by="id" :sort-desc="[true]">
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
      <!-- eslint-disable-next-line vue/valid-v-slot -->
      <template #item.timestamp_arrival="{ item }">
        {{ formatDate(item.timestamp_arrival) }}
      </template>
    </v-data-table>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";
import { readLots } from "@/store/lots/getters";
import { dispatchGetLots } from "@/store/lots/actions";
import { format } from "date-fns";

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
      text: "Fruit",
      sortable: true,
      value: "fruit.name",
      align: "left",
    },
    {
      text: "Arrival",
      sortable: true,
      value: "timestamp_arrival",
      align: "left",
    },
    {
      text: "Volume (m^3)",
      sortable: true,
      value: "volume",
      align: "left",
    },
    {
      text: "Weight (kg)",
      sortable: true,
      value: "weight",
      align: "left",
    },
    {
      text: "Ripens level (0 to 1)",
      sortable: true,
      value: "ripens_level",
      align: "left",
    },
    {
      text: "Price",
      sortable: true,
      value: "price",
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
  public formatDate(date) {
    return format(new Date(date), "yyyy-MM-dd HH:mm:ss");
  }
}
</script>
