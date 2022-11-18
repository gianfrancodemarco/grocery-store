import { IFruit } from "@/interfaces";
import { FruitState } from "./state";
import { getStoreAccessors } from "typesafe-vuex";
import { State } from "../state";

export const mutations = {
  setfruits(state: FruitState, payload: IFruit[]) {
    state.fruits = payload;
  },
  setfruit(state: FruitState, payload: IFruit) {
    state.fruit = payload;
  },
};

const { commit } = getStoreAccessors<FruitState, State>("");

export const commitSetFruit = commit(mutations.setfruit);
export const commitSetFruits = commit(mutations.setfruits);
