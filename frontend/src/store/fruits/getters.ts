import { FruitState } from "./state";
import { getStoreAccessors } from "typesafe-vuex";
import { State } from "../state";

export const getters = {
  fruits: (state: FruitState) => state.fruits,
  fruit: (state: FruitState) => state.fruit,
};

const { read } = getStoreAccessors<FruitState, State>("");

export const readFruits = read(getters.fruits);
export const readFruit = read(getters.fruit);
