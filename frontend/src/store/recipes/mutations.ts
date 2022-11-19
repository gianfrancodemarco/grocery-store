import { IAllergy } from "@/interfaces";
import { AllergyState } from "./state";
import { getStoreAccessors } from "typesafe-vuex";
import { State } from "../state";

export const mutations = {
  setrecipes(state: AllergyState, payload: IAllergy[]) {
    state.recipes = payload;
  },
  setrecipe(state: AllergyState, payload: IAllergy) {
    state.recipe = payload;
  },
};

const { commit } = getStoreAccessors<AllergyState, State>("");

export const commitSetAllergy = commit(mutations.setrecipe);
export const commitSetRecipes = commit(mutations.setrecipes);
