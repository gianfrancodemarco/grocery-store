import { mutations } from "./mutations";
import { getters } from "./getters";
import { actions } from "./actions";
import { RecipeState } from "./state";

const defaultState: RecipeState = {
  recipes: [],
  recipe: {},
};

export const recipesModule = {
  state: defaultState,
  mutations,
  actions,
  getters,
};
