import { mutations } from "./mutations";
import { getters } from "./getters";
import { actions } from "./actions";
import { AllergyState } from "./state";

const defaultState: AllergyState = {
  allergies: [],
  allergy: null,
};

export const allergiesModule = {
  state: defaultState,
  mutations,
  actions,
  getters,
};
