import { ISensor } from "@/interfaces";
import { SensorState } from "./state";
import { getStoreAccessors } from "typesafe-vuex";
import { State } from "../state";

export const mutations = {
  setsensors(state: SensorState, payload: ISensor[]) {
    state.sensors = payload;
  },
  setsensor(state: SensorState, payload: ISensor) {
    state.sensor = payload;
  },
};

const { commit } = getStoreAccessors<SensorState, State>("");

export const commitSetSensor = commit(mutations.setsensor);
export const commitSetSensors = commit(mutations.setsensors);
