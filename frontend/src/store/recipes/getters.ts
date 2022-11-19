import { AllergyState } from "./state";
import { getStoreAccessors } from "typesafe-vuex";
import { State } from "../state";

export const getters = {
  recipes: (state: AllergyState) => state.recipes,
  recipe: (state: AllergyState) => state.recipe,
};

const { read } = getStoreAccessors<AllergyState, State>("");

export const readRecipes = read(getters.recipes);
export const readAllergy = read(getters.recipe);
