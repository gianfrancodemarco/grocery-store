import { mutations } from "./mutations";
import { getters } from "./getters";
import { actions } from "./actions";
import { FruitState } from "./state";

const defaultState: FruitState = {
  fruits: [],
  fruit: null,
};

export const fruitsModule = {
  state: defaultState,
  mutations,
  actions,
  getters,
};
