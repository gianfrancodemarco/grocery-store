export interface IUserProfile {
  email: string;
  is_active: boolean;
  is_superuser: boolean;
  full_name: string;
  id: number;
}

export interface IUserProfileUpdate {
  email?: string;
  full_name?: string;
  password?: string;
  is_active?: boolean;
  is_superuser?: boolean;
}

export interface IUserProfileCreate {
  email: string;
  full_name?: string;
  password?: string;
  is_active?: boolean;
  is_superuser?: boolean;
}


export interface IFruit {
  id: number;
  name: string;
  peel_type: string;  
}

export interface IFruitUpdate {
  id: number;
  name: string;
  peel_type: string;  
}

export interface IFruitCreate {
  name: string;
  peel_type: string;  
}

export interface ILot {
  id: number;
  name: string;
  fruit_id: number;  
}

export interface ILotUpdate {
  id: number;
  name: string;
  fruit_id: number;  
}

export interface ILotCreate {
  name: string;
  fruit_id: number;  
}

export interface IAllergy {
  id: number;
  name: string;
  fruits: number[]
}

export interface IAllergyUpdate {
  id: number;
  name: string;
  fruits: number[]  
}

export interface IAllergyCreate {
  name: string;
  fruits: number[]
}

export interface IRecipe {
  id: number;
  name: string;
  fruits: number[]
}

export interface IRecipeUpdate {
  id: number;
  name: string;
  fruits: number[]  
}

export interface IRecipeCreate {
  name: string;
  fruits: number[]
}