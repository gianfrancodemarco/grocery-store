import { api } from "@/api";
import { ActionContext } from "vuex";
import { IRecipeCreate, IRecipeUpdate } from "@/interfaces";
import { State } from "../state";
import { RecipeState } from "./state";
import { getStoreAccessors } from "typesafe-vuex";
import { commitSetRecipes, commitSetRecipe } from "./mutations";
import { dispatchCheckApiError } from "../main/actions";
import { commitAddNotification, commitRemoveNotification } from "../main/mutations";

type MainContext = ActionContext<RecipeState, State>;

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
  async actionGetRecipe(context: MainContext, payload: { id: number }) {
    try {
      const response = await api.getRecipe(context.rootState.main.token, payload.id);
      if (response) {
        commitSetRecipe(context, response.data);
      }
    } catch (error) {
      await dispatchCheckApiError(context, error);
    }
  },
  async actionUpdateRecipe(
    context: MainContext,
    payload: { id: number; recipe: IRecipeUpdate },
  ) {
    try {
      const loadingNotification = { content: "saving", showProgress: true };
      commitAddNotification(context, loadingNotification);
      const response = (
        await Promise.all([
          api.updateRecipe(context.rootState.main.token, payload.id, payload.recipe),
          await new Promise<void>((resolve, _) => setTimeout(() => resolve(), 500)),
        ])
      )[0];
      commitSetRecipe(context, response.data);
      commitRemoveNotification(context, loadingNotification);
      commitAddNotification(context, {
        content: "Recipe successfully updated",
        color: "success",
      });
    } catch (error) {
      await dispatchCheckApiError(context, error);
    }
  },
  async actionCreateRecipe(context: MainContext, payload: { recipe: IRecipeCreate }) {
    try {
      const loadingNotification = { content: "saving", showProgress: true };
      commitAddNotification(context, loadingNotification);
      const response = (
        await Promise.all([
          api.createRecipe(context.rootState.main.token, payload.recipe),
          await new Promise<void>((resolve, _) => setTimeout(() => resolve(), 500)),
        ])
      )[0];
      commitSetRecipe(context, response.data);
      commitRemoveNotification(context, loadingNotification);
      commitAddNotification(context, {
        content: "Recipe successfully created",
        color: "success",
      });
    } catch (error) {
      await dispatchCheckApiError(context, error);
    }
  },
};

const { dispatch } = getStoreAccessors<RecipeState, State>("");

export const dispatchCreateRecipe = dispatch(actions.actionCreateRecipe);
export const dispatchGetRecipes = dispatch(actions.actionGetRecipes);
export const dispatchGetRecipe = dispatch(actions.actionGetRecipe);
export const dispatchUpdateRecipe = dispatch(actions.actionUpdateRecipe);
