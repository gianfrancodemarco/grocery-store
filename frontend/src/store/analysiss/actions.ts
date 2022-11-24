import { api } from "@/api";
import { ActionContext } from "vuex";
import { IAnalysisCreate, IAnalysisUpdate } from "@/interfaces";
import { State } from "../state";
import { AnalysisState } from "./state";
import { getStoreAccessors } from "typesafe-vuex";
import { commitSetAnalysiss, commitSetAnalysis } from "./mutations";
import { dispatchCheckApiError } from "../main/actions";
import { commitAddNotification, commitRemoveNotification } from "../main/mutations";

type MainContext = ActionContext<AnalysisState, State>;

export const actions = {
  async actionGetAnalysiss(context: MainContext) {
    try {
      const response = await api.getAnalysiss(context.rootState.main.token);
      if (response) {
        commitSetAnalysiss(context, response.data);
      }
    } catch (error) {
      await dispatchCheckApiError(context, error);
    }
  },
  async actionGetAnalysis(context: MainContext, payload: { id: number }) {
    try {
      const response = await api.getAnalysis(context.rootState.main.token, payload.id);
      if (response) {
        commitSetAnalysis(context, response.data);
      }
    } catch (error) {
      await dispatchCheckApiError(context, error);
    }
  },
  async actionUpdateAnalysis(
    context: MainContext,
    payload: { id: number; analysis: IAnalysisUpdate },
  ) {
    try {
      const loadingNotification = { content: "saving", showProgress: true };
      commitAddNotification(context, loadingNotification);
      const response = (
        await Promise.all([
          api.updateAnalysis(context.rootState.main.token, payload.id, payload.analysis),
          await new Promise<void>((resolve, _) => setTimeout(() => resolve(), 500)),
        ])
      )[0];
      commitSetAnalysis(context, response.data);
      commitRemoveNotification(context, loadingNotification);
      commitAddNotification(context, {
        content: "Analysis successfully updated",
        color: "success",
      });
    } catch (error) {
      await dispatchCheckApiError(context, error);
    }
  },
  async actionCreateAnalysis(
    context: MainContext,
    payload: { analysis: IAnalysisCreate },
  ) {
    try {
      const loadingNotification = { content: "saving", showProgress: true };
      commitAddNotification(context, loadingNotification);
      const response = (
        await Promise.all([
          api.createAnalysis(context.rootState.main.token, payload.analysis),
          await new Promise<void>((resolve, _) => setTimeout(() => resolve(), 500)),
        ])
      )[0];
      commitSetAnalysis(context, response.data);
      commitRemoveNotification(context, loadingNotification);
      commitAddNotification(context, {
        content: "Analysis successfully created",
        color: "success",
      });
    } catch (error) {
      await dispatchCheckApiError(context, error);
    }
  },
};

const { dispatch } = getStoreAccessors<AnalysisState, State>("");

export const dispatchCreateAnalysis = dispatch(actions.actionCreateAnalysis);
export const dispatchGetAnalysiss = dispatch(actions.actionGetAnalysiss);
export const dispatchGetAnalysis = dispatch(actions.actionGetAnalysis);
export const dispatchUpdateAnalysis = dispatch(actions.actionUpdateAnalysis);
