import { mutations } from "./mutations";
import { getters } from "./getters";
import { actions } from "./actions";
import { SensorState } from "./state";

const defaultState: SensorState = {
  sensors: [],
  sensor: {},
};

export const sensorsModule = {
  state: defaultState,
  mutations,
  actions,
  getters,
};
