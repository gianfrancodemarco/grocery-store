import { IAnalysis } from "@/interfaces";
import { AnalysisState } from "./state";
import { getStoreAccessors } from "typesafe-vuex";
import { State } from "../state";

export const mutations = {
  setanalysiss(state: AnalysisState, payload: IAnalysis[]) {
    state.analysiss = payload;
  },
  setanalysis(state: AnalysisState, payload: IAnalysis) {
    state.analysis = payload;
  },
};

const { commit } = getStoreAccessors<AnalysisState, State>("");

export const commitSetAnalysis = commit(mutations.setanalysis);
export const commitSetAnalysiss = commit(mutations.setanalysiss);
