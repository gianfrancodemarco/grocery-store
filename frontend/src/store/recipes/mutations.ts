import { IRecipe } from "@/interfaces";
import { RecipeState } from "./state";
import { getStoreAccessors } from "typesafe-vuex";
import { State } from "../state";

export const mutations = {
  setrecipes(state: RecipeState, payload: IRecipe[]) {
    state.recipes = payload;
  },
  setrecipe(state: RecipeState, payload: IRecipe) {
    state.recipe = payload;
  },
};

const { commit } = getStoreAccessors<RecipeState, State>("");

export const commitSetRecipe = commit(mutations.setrecipe);
export const commitSetRecipes = commit(mutations.setrecipes);
