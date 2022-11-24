import { mutations } from "./mutations";
import { getters } from "./getters";
import { actions } from "./actions";
import { NotificationState } from "./state";

const defaultState: NotificationState = {
  notifications: [],
  notificationsUnread: 0,
};

export const notificationsModule = {
  state: defaultState,
  mutations,
  actions,
  getters,
};
