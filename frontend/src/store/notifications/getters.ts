import { NotificationState } from "./state";
import { getStoreAccessors } from "typesafe-vuex";
import { State } from "../state";

export const getters = {
  notifications: (state: NotificationState) => state.notifications,
  notificationsUnread: (state: NotificationState) => state.notificationsUnread,
};

const { read } = getStoreAccessors<NotificationState, State>("");

export const readNotifications = read(getters.notifications);
export const readNotificationsUnread = read(getters.notificationsUnread);
