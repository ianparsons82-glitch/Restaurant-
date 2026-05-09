import { configureStore } from '@reduxjs/toolkit';
import financeReducer from './slices/financeSlice';
import nutritionReducer from './slices/nutritionSlice';
import familyReducer from './slices/familySlice';

export const store = configureStore({
  reducer: {
    finance: financeReducer,
    nutrition: nutritionReducer,
    family: familyReducer,
  },
});

export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;
