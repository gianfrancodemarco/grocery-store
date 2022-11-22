import { SensorState } from "./state";
import { getStoreAccessors } from "typesafe-vuex";
import { State } from "../state";

export const getters = {
  sensors: (state: SensorState) => state.sensors,
  sensor: (state: SensorState) => state.sensor,
};

const { read } = getStoreAccessors<SensorState, State>("");

export const readSensors = read(getters.sensors);
export const readSensor = read(getters.sensor);
