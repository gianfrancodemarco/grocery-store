import { AllergyState } from "./state";
import { getStoreAccessors } from "typesafe-vuex";
import { State } from "../state";

export const getters = {
  allergies: (state: AllergyState) => state.allergies,
  allergy: (state: AllergyState) => state.allergy,
};

const { read } = getStoreAccessors<AllergyState, State>("");

export const readAllergies = read(getters.allergies);
export const readAllergy = read(getters.allergy);
