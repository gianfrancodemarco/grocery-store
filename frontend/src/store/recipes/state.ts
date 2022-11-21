import { IRecipe } from "@/interfaces";

export interface RecipeState {
  recipes: IRecipe[];
  recipe: IRecipe | {};
}
