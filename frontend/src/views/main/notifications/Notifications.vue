<template>
  <div>
    <v-toolbar light>
      <v-toolbar-title> Read Notifications </v-toolbar-title>
      <v-spacer></v-spacer>
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
      <template #item.timestamp="{ item }">
        {{ formatDate(item.timestamp) }}
      </template>
    </v-data-table>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";
import { readNotifications } from "@/store/notifications/getters";
import { dispatchGetNotifications, dispatchGetNotificationsUnread } from "@/store/notifications/actions";
import { format } from "date-fns";
import { dispatchUpdateUserProfile } from "@/store/main/actions";
import { readUserProfile } from "@/store/main/getters";

@Component
export default class Notifications extends Vue {
  public headers = [
    {
      text: "Id",
      sortable: true,
      value: "id",
      align: "left",
    },
    {
      text: "Trigger name",
      sortable: true,
      value: "trigger_name",
      align: "left",
    },
    {
      text: "Description",
      sortable: true,
      value: "description",
      align: "left",
    },
    {
      text: "Timestamp",
      sortable: true,
      value: "timestamp",
      align: "left",
    }
  ];
  
  get lots() {
    return readNotifications(this.$store);
  }

  get userProfile() {
    return readUserProfile(this.$store);
  }

  public async mounted() {
    await dispatchGetNotifications(this.$store);
    await dispatchUpdateUserProfile(this.$store, {
        last_read_notifications: new Date(Date.now()).toISOString()
      });
    await dispatchGetNotificationsUnread(this.$store);
  }
  public formatDate(date) {
    return format(new Date(date), "yyyy-MM-dd'T'HH:mm:ss");
  }
}
</script>
