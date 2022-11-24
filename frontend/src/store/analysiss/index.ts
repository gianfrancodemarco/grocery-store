import { mutations } from "./mutations";
import { getters } from "./getters";
import { actions } from "./actions";
import { AnalysisState } from "./state";

const defaultState: AnalysisState = {
  analysiss: [],
  analysis: {},
};

export const analysissModule = {
  state: defaultState,
  mutations,
  actions,
  getters,
};
