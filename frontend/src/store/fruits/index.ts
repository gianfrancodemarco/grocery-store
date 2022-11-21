import { mutations } from "./mutations";
import { getters } from "./getters";
import { actions } from "./actions";
import { FruitState } from "./state";

const defaultState: FruitState = {
  fruits: [],
  fruit: {},
};

export const fruitsModule = {
  state: defaultState,
  mutations,
  actions,
  getters,
};
