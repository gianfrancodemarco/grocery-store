import axios from "axios";
import { apiUrl } from "@/env";
import {
  IUserProfile,
  IUserProfileUpdate,
  IUserProfileCreate,
  IFruit,
  IFruitUpdate,
  IFruitCreate,
  ILotUpdate,
  ILotCreate,
  ILot,
  IAllergy,
  IAllergyCreate,
  IAllergyUpdate,
  IRecipe,
  IRecipeCreate,
  IRecipeUpdate,
  ISensor,
  ISensorCreate,
  ISensorUpdate,
  INotification,
  IAnalysis,
  IAnalysisCreate,
  IAnalysisUpdate
} from "./interfaces";

function authHeaders(token: string) {
  return {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  };
}

export const api = {
  async logInGetToken(username: string, password: string) {
    const params = new URLSearchParams();
    params.append("username", username);
    params.append("password", password);

    return axios.post(`${apiUrl}/api/v1/login/access-token`, params);
  },
  async getMe(token: string) {
    return axios.get<IUserProfile>(`${apiUrl}/api/v1/users/me`, authHeaders(token));
  },
  async updateMe(token: string, data: IUserProfileUpdate) {
    return axios.put<IUserProfile>(
      `${apiUrl}/api/v1/users/me`,
      data,
      authHeaders(token),
    );
  },
  async getUsers(token: string) {
    return axios.get<IUserProfile[]>(`${apiUrl}/api/v1/users/`, authHeaders(token));
  },
  async updateUser(token: string, userId: number, data: IUserProfileUpdate) {
    return axios.put(`${apiUrl}/api/v1/users/${userId}`, data, authHeaders(token));
  },
  async createUser(token: string, data: IUserProfileCreate) {
    return axios.post(`${apiUrl}/api/v1/users/`, data, authHeaders(token));
  },
  async passwordRecovery(email: string) {
    return axios.post(`${apiUrl}/api/v1/password-recovery/${email}`);
  },
  async resetPassword(password: string, token: string) {
    return axios.post(`${apiUrl}/api/v1/reset-password/`, {
      new_password: password,
      token,
    });
  },
  //Fruits
  async getFruits(token: string) {
    return axios.get<IFruit[]>(`${apiUrl}/api/v1/fruits/`, authHeaders(token));
  },
  async getFruit(token: string, fruitId: number) {
    return axios.get<IFruit>(`${apiUrl}/api/v1/fruits/${fruitId}`, authHeaders(token));
  },
  async updateFruit(token: string, fruitId: number, data: IFruitUpdate) {
    return axios.put(`${apiUrl}/api/v1/fruits/${fruitId}`, data, authHeaders(token));
  },
  async createFruit(token: string, data: IFruitCreate) {
    return axios.post(`${apiUrl}/api/v1/fruits/`, data, authHeaders(token));
  },
  //Lots
  async getLots(token: string) {
    return axios.get<ILot[]>(`${apiUrl}/api/v1/lots/`, authHeaders(token));
  },
  async getLot(token: string, lotId: number) {
    return axios.get<ILot>(`${apiUrl}/api/v1/lots/${lotId}`, authHeaders(token));
  },
  async updateLot(token: string, lotId: number, data: ILotUpdate) {
    return axios.put(`${apiUrl}/api/v1/lots/${lotId}`, data, authHeaders(token));
  },
  async createLot(token: string, data: ILotCreate) {
    return axios.post(`${apiUrl}/api/v1/lots/`, data, authHeaders(token));
  },
  //Allergies
  async getAllergies(token: string) {
    return axios.get<IAllergy[]>(`${apiUrl}/api/v1/allergies/`, authHeaders(token));
  },
  async getAllergy(token: string, allergyId: number) {
    return axios.get<IAllergy>(
      `${apiUrl}/api/v1/allergies/${allergyId}`,
      authHeaders(token),
    );
  },
  async updateAllergy(token: string, allergyId: number, data: IAllergyUpdate) {
    return axios.put(
      `${apiUrl}/api/v1/allergies/${allergyId}`,
      data,
      authHeaders(token),
    );
  },
  async createAllergy(token: string, data: IAllergyCreate) {
    return axios.post(`${apiUrl}/api/v1/allergies/`, data, authHeaders(token));
  },
  //Recipes
  async getRecipes(token: string) {
    return axios.get<IRecipe[]>(`${apiUrl}/api/v1/recipes/`, authHeaders(token));
  },
  async getRecipe(token: string, allergyId: number) {
    return axios.get<IRecipe>(
      `${apiUrl}/api/v1/recipes/${allergyId}`,
      authHeaders(token),
    );
  },
  async updateRecipe(token: string, allergyId: number, data: IRecipeUpdate) {
    return axios.put(`${apiUrl}/api/v1/recipes/${allergyId}`, data, authHeaders(token));
  },
  async createRecipe(token: string, data: IRecipeCreate) {
    return axios.post(`${apiUrl}/api/v1/recipes/`, data, authHeaders(token));
  },
  //Sensors
  async getSensors(token: string) {
    return axios.get<ISensor[]>(`${apiUrl}/api/v1/sensors/`, authHeaders(token));
  },
  async getSensor(token: string, allergyId: number) {
    return axios.get<ISensor>(
      `${apiUrl}/api/v1/sensors/${allergyId}`,
      authHeaders(token),
    );
  },
  async updateSensor(token: string, allergyId: number, data: ISensorUpdate) {
    return axios.put(`${apiUrl}/api/v1/sensors/${allergyId}`, data, authHeaders(token));
  },
  async createSensor(token: string, data: ISensorCreate) {
    return axios.post(`${apiUrl}/api/v1/sensors/`, data, authHeaders(token));
  },
  //Notifications
  async getNotifications(token: string) {
    return axios.get<INotification[]>(`${apiUrl}/api/v1/notifications/`, authHeaders(token));
  },
  async getNotificationsUnread(token: string) {
    return axios.get<number>(`${apiUrl}/api/v1/notifications/unread/count`, authHeaders(token));
  },
  //Analysis
  async getAnalysiss(token: string) {
    return axios.get<IAnalysis[]>(`${apiUrl}/api/v1/analysiss/`, authHeaders(token));
  },
  async getAnalysis(token: string, allergyId: number) {
    return axios.get<IAnalysis>(
      `${apiUrl}/api/v1/analysiss/${allergyId}`,
      authHeaders(token),
    );
  },
  async updateAnalysis(token: string, allergyId: number, data: IAnalysisUpdate) {
    return axios.put(`${apiUrl}/api/v1/analysiss/${allergyId}`, data, authHeaders(token));
  },
  async createAnalysis(token: string, data: IAnalysisCreate) {
    return axios.post(`${apiUrl}/api/v1/analysiss/`, data, authHeaders(token));
  },
};
