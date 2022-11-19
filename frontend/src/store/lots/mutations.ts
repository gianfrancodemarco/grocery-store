import { ILot } from "@/interfaces";
import { LotState } from "./state";
import { getStoreAccessors } from "typesafe-vuex";
import { State } from "../state";

export const mutations = {
  setlots(state: LotState, payload: ILot[]) {
    state.lots = payload;
  },
  setlot(state: LotState, payload: ILot) {
    state.lot = payload;
  },
};

const { commit } = getStoreAccessors<LotState, State>("");

export const commitSetLot = commit(mutations.setlot);
export const commitSetLots = commit(mutations.setlots);
