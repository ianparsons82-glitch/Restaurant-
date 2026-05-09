import { createSlice, PayloadAction } from '@reduxjs/toolkit';

export interface Meal {
  id: string;
  day: string;
  mealType: 'breakfast' | 'lunch' | 'dinner' | 'snack';
  name: string;
  ingredients?: string;
  calories?: number;
  date: string;
}

export interface ShoppingItem {
  id: string;
  item: string;
  quantity?: number;
  unit?: string;
  category: string;
  isPurchased: boolean;
  date: string;
}

interface NutritionState {
  meals: Meal[];
  shoppingList: ShoppingItem[];
  healthyStaples: string[];
  customMealTypes: string[];
}

const initialState: NutritionState = {
  meals: [],
  shoppingList: [],
  healthyStaples: [],
  customMealTypes: [],
};

const nutritionSlice = createSlice({
  name: 'nutrition',
  initialState,
  reducers: {
    addMeal: (state, action: PayloadAction<Meal>) => {
      state.meals.push(action.payload);
    },
    removeMeal: (state, action: PayloadAction<string>) => {
      state.meals = state.meals.filter(meal => meal.id !== action.payload);
    },
    updateMeal: (state, action: PayloadAction<Meal>) => {
      const index = state.meals.findIndex(meal => meal.id === action.payload.id);
      if (index > -1) {
        state.meals[index] = action.payload;
      }
    },
    addShoppingItem: (state, action: PayloadAction<ShoppingItem>) => {
      state.shoppingList.push(action.payload);
    },
    removeShoppingItem: (state, action: PayloadAction<string>) => {
      state.shoppingList = state.shoppingList.filter(item => item.id !== action.payload);
    },
    toggleShoppingItem: (state, action: PayloadAction<string>) => {
      const item = state.shoppingList.find(item => item.id === action.payload);
      if (item) {
        item.isPurchased = !item.isPurchased;
      }
    },
    clearPurchasedItems: (state) => {
      state.shoppingList = state.shoppingList.filter(item => !item.isPurchased);
    },
    addHealthyStaple: (state, action: PayloadAction<string>) => {
      if (!state.healthyStaples.includes(action.payload)) {
        state.healthyStaples.push(action.payload);
      }
    },
    removeHealthyStaple: (state, action: PayloadAction<string>) => {
      state.healthyStaples = state.healthyStaples.filter(staple => staple !== action.payload);
    },
    addCustomMealType: (state, action: PayloadAction<string>) => {
      if (!state.customMealTypes.includes(action.payload)) {
        state.customMealTypes.push(action.payload);
      }
    },
    removeCustomMealType: (state, action: PayloadAction<string>) => {
      state.customMealTypes = state.customMealTypes.filter(type => type !== action.payload);
    },
  },
});

export const {
  addMeal,
  removeMeal,
  updateMeal,
  addShoppingItem,
  removeShoppingItem,
  toggleShoppingItem,
  clearPurchasedItems,
  addHealthyStaple,
  removeHealthyStaple,
  addCustomMealType,
  removeCustomMealType,
} = nutritionSlice.actions;

export default nutritionSlice.reducer;
