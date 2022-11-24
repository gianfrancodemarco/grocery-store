import { api } from "@/api";
import { ActionContext } from "vuex";
import { State } from "../state";
import { NotificationState } from "./state";
import { getStoreAccessors } from "typesafe-vuex";
import { commitSetNotifications, commitSetNotificationsUnread } from "./mutations";
import { dispatchCheckApiError } from "../main/actions";

type MainContext = ActionContext<NotificationState, State>;

export const actions = {
  async actionGetNotifications(context: MainContext) {
    try {
      const response = await api.getNotifications(context.rootState.main.token);
      if (response) {
        commitSetNotifications(context, response.data);
      }
    } catch (error) {
      await dispatchCheckApiError(context, error);
    }
  },
  async actionGetNotificationsUnread(context: MainContext) {
    try {
      const response = await api.getNotificationsUnread(context.rootState.main.token);
      if (response) {
        commitSetNotificationsUnread(context, response.data);
      }
    } catch (error) {
      await dispatchCheckApiError(context, error);
    }
  },
};

const { dispatch } = getStoreAccessors<NotificationState, State>("");

export const dispatchGetNotifications = dispatch(actions.actionGetNotifications);
export const dispatchGetNotificationsUnread = dispatch(actions.actionGetNotificationsUnread);