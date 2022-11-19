import { IAllergy } from "@/interfaces";
import { AllergyState } from "./state";
import { getStoreAccessors } from "typesafe-vuex";
import { State } from "../state";

export const mutations = {
  setallergies(state: AllergyState, payload: IAllergy[]) {
    state.allergies = payload;
  },
  setallergy(state: AllergyState, payload: IAllergy) {
    state.allergy = payload;
  },
};

const { commit } = getStoreAccessors<AllergyState, State>("");

export const commitSetAllergy = commit(mutations.setallergy);
export const commitSetAllergies = commit(mutations.setallergies);
