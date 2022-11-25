import { api } from "@/api";
import { ActionContext } from "vuex";
import { ILotCreate, ILotUpdate } from "@/interfaces";
import { State } from "../state";
import { LotState } from "./state";
import { getStoreAccessors } from "typesafe-vuex";
import { commitSetLots, commitSetLot } from "./mutations";
import { dispatchCheckApiError } from "../main/actions";
import { commitAddNotification, commitRemoveNotification } from "../main/mutations";

type MainContext = ActionContext<LotState, State>;

export const actions = {
  async actionGetLots(context: MainContext) {
    try {
      const response = await api.getLots(context.rootState.main.token);
      if (response) {
        commitSetLots(context, response.data);
      }
    } catch (error) {
      await dispatchCheckApiError(context, error);
    }
  },
  async actionGetLot(context: MainContext, payload: { id: number }) {
    try {
      const response = await api.getLot(context.rootState.main.token, payload.id);
      if (response) {
        commitSetLot(context, response.data);
      }
    } catch (error) {
      await dispatchCheckApiError(context, error);
    }
  },
  async actionUpdateLot(
    context: MainContext,
    payload: { id: number; lot: ILotUpdate },
  ) {
    const loadingNotification = { content: "saving", showProgress: true };
    commitAddNotification(context, loadingNotification);
    
    api.updateLot(context.rootState.main.token, payload.id, payload.lot)
    .then(response => {
      commitSetLot(context, response.data);
      commitRemoveNotification(context, loadingNotification);
      commitAddNotification(context, {
        content: "Analysis successfully updated",
        color: "success",
      });
    })
    .catch(error => {
      commitRemoveNotification(context, loadingNotification);

      if (error?.response?.data?.detail){
        commitAddNotification(context, {
          content: error.response.data.detail,
          color: "error",
        });
      } else {
        commitAddNotification(context, {
          content: "Generic error",
          color: "error",
        });
      }
    })
  },
  async actionCreateLot(context: MainContext, payload: { lot: ILotCreate }) {
    const loadingNotification = { content: "saving", showProgress: true };
    commitAddNotification(context, loadingNotification);
    
    api.createLot(context.rootState.main.token, payload.lot)
    .then(response => {
      commitSetLot(context, response.data);
      commitRemoveNotification(context, loadingNotification);
      commitAddNotification(context, {
        content: "Analysis successfully updated",
        color: "success",
      });
    })
    .catch(error => {
      commitRemoveNotification(context, loadingNotification);

      if (error?.response?.data?.detail){
        commitAddNotification(context, {
          content: error.response.data.detail,
          color: "error",
        });
      } else {
        commitAddNotification(context, {
          content: "Generic error",
          color: "error",
        });
      }
    })
  },
};

const { dispatch } = getStoreAccessors<LotState, State>("");

export const dispatchCreateLot = dispatch(actions.actionCreateLot);
export const dispatchGetLots = dispatch(actions.actionGetLots);
export const dispatchGetLot = dispatch(actions.actionGetLot);
export const dispatchUpdateLot = dispatch(actions.actionUpdateLot);
