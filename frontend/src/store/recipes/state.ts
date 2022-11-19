import { IAllergy } from "@/interfaces";

export interface AllergyState {
  recipes: IAllergy[];
  recipe: IAllergy | null;
}
