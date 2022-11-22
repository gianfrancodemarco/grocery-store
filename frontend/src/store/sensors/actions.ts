import { api } from "@/api";
import { ActionContext } from "vuex";
import { ISensorCreate, ISensorUpdate } from "@/interfaces";
import { State } from "../state";
import { SensorState } from "./state";
import { getStoreAccessors } from "typesafe-vuex";
import { commitSetSensors, commitSetSensor } from "./mutations";
import { dispatchCheckApiError } from "../main/actions";
import { commitAddNotification, commitRemoveNotification } from "../main/mutations";

type MainContext = ActionContext<SensorState, State>;

export const actions = {
  async actionGetSensors(context: MainContext) {
    try {
      const response = await api.getSensors(context.rootState.main.token);
      if (response) {
        commitSetSensors(context, response.data);
      }
    } catch (error) {
      await dispatchCheckApiError(context, error);
    }
  },
  async actionGetSensor(context: MainContext, payload: { id: number }) {
    try {
      const response = await api.getSensor(context.rootState.main.token, payload.id);
      if (response) {
        commitSetSensor(context, response.data);
      }
    } catch (error) {
      await dispatchCheckApiError(context, error);
    }
  },
  async actionUpdateSensor(
    context: MainContext,
    payload: { id: number; sensor: ISensorUpdate },
  ) {
    try {
      const loadingNotification = { content: "saving", showProgress: true };
      commitAddNotification(context, loadingNotification);
      const response = (
        await Promise.all([
          api.updateSensor(context.rootState.main.token, payload.id, payload.sensor),
          await new Promise<void>((resolve, _) => setTimeout(() => resolve(), 500)),
        ])
      )[0];
      commitSetSensor(context, response.data);
      commitRemoveNotification(context, loadingNotification);
      commitAddNotification(context, {
        content: "Sensor successfully updated",
        color: "success",
      });
    } catch (error) {
      await dispatchCheckApiError(context, error);
    }
  },
  async actionCreateSensor(
    context: MainContext,
    payload: { sensor: ISensorCreate },
  ) {
    try {
      const loadingNotification = { content: "saving", showProgress: true };
      commitAddNotification(context, loadingNotification);
      const response = (
        await Promise.all([
          api.createSensor(context.rootState.main.token, payload.sensor),
          await new Promise<void>((resolve, _) => setTimeout(() => resolve(), 500)),
        ])
      )[0];
      commitSetSensor(context, response.data);
      commitRemoveNotification(context, loadingNotification);
      commitAddNotification(context, {
        content: "Sensor successfully created",
        color: "success",
      });
    } catch (error) {
      await dispatchCheckApiError(context, error);
    }
  },
};

const { dispatch } = getStoreAccessors<SensorState, State>("");

export const dispatchCreateSensor = dispatch(actions.actionCreateSensor);
export const dispatchGetSensors = dispatch(actions.actionGetSensors);
export const dispatchGetSensor = dispatch(actions.actionGetSensor);
export const dispatchUpdateSensor = dispatch(actions.actionUpdateSensor);
