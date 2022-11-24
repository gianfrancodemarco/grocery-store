import { INotification } from "@/interfaces";
import { NotificationState } from "./state";
import { getStoreAccessors } from "typesafe-vuex";
import { State } from "../state";

export const mutations = {
  setnotifications(state: NotificationState, payload: INotification[]) {
    state.notifications = payload;
  },
  setnotificationsUnread(state: NotificationState, payload: number) {
    state.notificationsUnread = payload;
  },
};

const { commit } = getStoreAccessors<NotificationState, State>("");

export const commitSetNotifications = commit(mutations.setnotifications);
export const commitSetNotificationsUnread = commit(mutations.setnotificationsUnread);