import { api } from "@/api";
import { ActionContext } from "vuex";
import { IFruitCreate, IFruitUpdate } from "@/interfaces";
import { State } from "../state";
import { FruitState } from "./state";
import { getStoreAccessors } from "typesafe-vuex";
import { commitSetFruits, commitSetFruit } from "./mutations";
import { dispatchCheckApiError } from "../main/actions";
import { commitAddNotification, commitRemoveNotification } from "../main/mutations";

type MainContext = ActionContext<FruitState, State>;

export const actions = {
  async actionGetFruits(context: MainContext) {
    try {
      const response = await api.getFruits(context.rootState.main.token);
      if (response) {
        commitSetFruits(context, response.data);
      }
    } catch (error) {
      await dispatchCheckApiError(context, error);
    }
  },
  async actionGetFruit(context: MainContext, payload: { id: number }) {
    try {
      const response = await api.getFruit(context.rootState.main.token, payload.id);
      if (response) {
        commitSetFruit(context, response.data);
      }
    } catch (error) {
      await dispatchCheckApiError(context, error);
    }
  },
  async actionUpdateFruit(
    context: MainContext,
    payload: { id: number; fruit: IFruitUpdate },
  ) {
    try {
      const loadingNotification = { content: "saving", showProgress: true };
      commitAddNotification(context, loadingNotification);
      const response = (
        await Promise.all([
          api.updateFruit(context.rootState.main.token, payload.id, payload.fruit),
          await new Promise<void>((resolve, _) => setTimeout(() => resolve(), 500)),
        ])
      )[0];
      commitSetFruit(context, response.data);
      commitRemoveNotification(context, loadingNotification);
      commitAddNotification(context, {
        content: "Fruit successfully updated",
        color: "success",
      });
    } catch (error) {
      await dispatchCheckApiError(context, error);
    }
  },
  async actionCreateFruit(context: MainContext, payload: { fruit: IFruitCreate }) {
    try {
      const loadingNotification = { content: "saving", showProgress: true };
      commitAddNotification(context, loadingNotification);
      const response = (
        await Promise.all([
          api.createFruit(context.rootState.main.token, payload.fruit),
          await new Promise<void>((resolve, _) => setTimeout(() => resolve(), 500)),
        ])
      )[0];
      commitSetFruit(context, response.data);
      commitRemoveNotification(context, loadingNotification);
      commitAddNotification(context, {
        content: "Fruit successfully created",
        color: "success",
      });
    } catch (error) {
      await dispatchCheckApiError(context, error);
    }
  },
};

const { dispatch } = getStoreAccessors<FruitState, State>("");

export const dispatchCreateFruit = dispatch(actions.actionCreateFruit);
export const dispatchGetFruits = dispatch(actions.actionGetFruits);
export const dispatchGetFruit = dispatch(actions.actionGetFruit);
export const dispatchUpdateFruit = dispatch(actions.actionUpdateFruit);
