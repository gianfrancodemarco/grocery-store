import { LotState } from "./state";
import { getStoreAccessors } from "typesafe-vuex";
import { State } from "../state";

export const getters = {
  lots: (state: LotState) => state.lots,
  lot: (state: LotState) => state.lot,
};

const { read } = getStoreAccessors<LotState, State>("");

export const readLots = read(getters.lots);
export const readLot = read(getters.lot);
