import { IAllergy } from "@/interfaces";

export interface AllergyState {
  allergies: IAllergy[];
  allergy: IAllergy | null;
}
