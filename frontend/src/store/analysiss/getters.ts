import { AnalysisState } from "./state";
import { getStoreAccessors } from "typesafe-vuex";
import { State } from "../state";

export const getters = {
  analysiss: (state: AnalysisState) => state.analysiss,
  analysis: (state: AnalysisState) => state.analysis,
};

const { read } = getStoreAccessors<AnalysisState, State>("");

export const readAnalysiss = read(getters.analysiss);
export const readAnalysis = read(getters.analysis);
