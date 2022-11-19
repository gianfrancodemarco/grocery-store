import { mutations } from "./mutations";
import { getters } from "./getters";
import { actions } from "./actions";
import { AllergyState } from "./state";

const defaultState: AllergyState = {
  recipes: [],
  recipe: null,
};

export const recipesModule = {
  state: defaultState,
  mutations,
  actions,
  getters,
};
