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
  maximum_stationary_time: number;
  size: string
}

export interface IFruitUpdate {
  id: number;
  name: string;
  peel_type: string;  
  maximum_stationary_time: number;
  size: string
}

export interface IFruitCreate {
  name: string;
  peel_type: string;  
  maximum_stationary_time: number;
  size: string
}

export interface ILot {
  id: number;
  name: string;
  fruit_id: number;  
  timestamp_arrival: string;
  volume: number;
  weight: number;
  ripens_level: number;
}

export interface ILotUpdate {
  id: number;
  name: string;
  fruit_id: number;
  timestamp_arrival: string;
  volume: number;
  weight: number;
  ripens_level: number;
}

export interface ILotCreate {
  name: string;
  fruit_id: number;  
  timestamp_arrival: string;
  volume: number;
  weight: number;
  ripens_level: number;
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
export interface ISensor {
  id: number;
  name: string;
  fruit_size: string
  medium_energy_consumption: number
  cost: number
  brand: string
}

export interface ISensorUpdate {
  id: number;
  name: string;
  fruit_size: string
  medium_energy_consumption: number
  cost: number
  brand: string
}

export interface ISensorCreate {
  name: string;
  fruit_size: string
  medium_energy_consumption: number
  cost: number
  brand: string
}

export interface INotification {
  id: number;
  trigger_name: string;
  description: string
  timestamp: string;
}

export interface IAnalysis {
  id: number;
  lot_id: number;
  sensor_id: number;
  description: string
}

export interface IAnalysisUpdate {
  id: number;
  lot_id: number;
  sensor_id: number;
  description: string
}

export interface IAnalysisCreate {
  id: number;
  lot_id: number;
  sensor_id: number;
  description: string
}