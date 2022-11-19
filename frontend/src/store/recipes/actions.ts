import { api } from "@/api";
import { ActionContext } from "vuex";
import { IAllergyCreate, IAllergyUpdate } from "@/interfaces";
import { State } from "../state";
import { AllergyState } from "./state";
import { getStoreAccessors } from "typesafe-vuex";
import { commitSetRecipes, commitSetAllergy } from "./mutations";
import { dispatchCheckApiError } from "../main/actions";
import { commitAddNotification, commitRemoveNotification } from "../main/mutations";

type MainContext = ActionContext<AllergyState, State>;

export const actions = {
  async actionGetRecipes(context: MainContext) {
    try {
      const response = await api.getRecipes(context.rootState.main.token);
      if (response) {
        commitSetRecipes(context, response.data);
      }
    } catch (error) {
      await dispatchCheckApiError(context, error);
    }
  },
  async actionGetAllergy(context: MainContext, payload: { id: number }) {
    try {
      const response = await api.getAllergy(context.rootState.main.token, payload.id);
      if (response) {
        commitSetAllergy(context, response.data);
      }
    } catch (error) {
      await dispatchCheckApiError(context, error);
    }
  },
  async actionUpdateAllergy(
    context: MainContext,
    payload: { id: number; recipe: IAllergyUpdate },
  ) {
    try {
      const loadingNotification = { content: "saving", showProgress: true };
      commitAddNotification(context, loadingNotification);
      const response = (
        await Promise.all([
          api.updateAllergy(context.rootState.main.token, payload.id, payload.recipe),
          await new Promise<void>((resolve, _) => setTimeout(() => resolve(), 500)),
        ])
      )[0];
      commitSetAllergy(context, response.data);
      commitRemoveNotification(context, loadingNotification);
      commitAddNotification(context, {
        content: "Allergy successfully updated",
        color: "success",
      });
    } catch (error) {
      await dispatchCheckApiError(context, error);
    }
  },
  async actionCreateAllergy(context: MainContext, payload: { recipe: IAllergyCreate }) {
    try {
      const loadingNotification = { content: "saving", showProgress: true };
      commitAddNotification(context, loadingNotification);
      const response = (
        await Promise.all([
          api.createAllergy(context.rootState.main.token, payload.recipe),
          await new Promise<void>((resolve, _) => setTimeout(() => resolve(), 500)),
        ])
      )[0];
      commitSetAllergy(context, response.data);
      commitRemoveNotification(context, loadingNotification);
      commitAddNotification(context, {
        content: "Allergy successfully created",
        color: "success",
      });
    } catch (error) {
      await dispatchCheckApiError(context, error);
    }
  },
};

const { dispatch } = getStoreAccessors<AllergyState, State>("");

export const dispatchCreateAllergy = dispatch(actions.actionCreateAllergy);
export const dispatchGetRecipes = dispatch(actions.actionGetRecipes);
export const dispatchGetAllergy = dispatch(actions.actionGetAllergy);
export const dispatchUpdateAllergy = dispatch(actions.actionUpdateAllergy);
