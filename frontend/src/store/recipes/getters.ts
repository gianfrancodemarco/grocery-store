import { RecipeState } from "./state";
import { getStoreAccessors } from "typesafe-vuex";
import { State } from "../state";

export const getters = {
  recipes: (state: RecipeState) => state.recipes,
  recipe: (state: RecipeState) => state.recipe,
};

const { read } = getStoreAccessors<RecipeState, State>("");

export const readRecipes = read(getters.recipes);
export const readRecipe = read(getters.recipe);
