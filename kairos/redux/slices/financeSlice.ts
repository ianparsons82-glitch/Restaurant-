import { createSlice, PayloadAction } from '@reduxjs/toolkit';

export interface BudgetItem {
  id: string;
  category: string;
  amount: number;
  date: string;
  isCustom: boolean;
}

export interface Debt {
  id: string;
  name: string;
  amount: number;
  interestRate?: number;
  minPayment?: number;
  dueDate?: string;
  date: string;
}

interface FinanceState {
  budgetItems: BudgetItem[];
  debts: Debt[];
  customCategories: string[];
}

const initialState: FinanceState = {
  budgetItems: [],
  debts: [],
  customCategories: [],
};

const financeSlice = createSlice({
  name: 'finance',
  initialState,
  reducers: {
    addBudgetItem: (state, action: PayloadAction<BudgetItem>) => {
      state.budgetItems.push(action.payload);
    },
    removeBudgetItem: (state, action: PayloadAction<string>) => {
      state.budgetItems = state.budgetItems.filter(item => item.id !== action.payload);
    },
    updateBudgetItem: (state, action: PayloadAction<BudgetItem>) => {
      const index = state.budgetItems.findIndex(item => item.id === action.payload.id);
      if (index > -1) {
        state.budgetItems[index] = action.payload;
      }
    },
    addDebt: (state, action: PayloadAction<Debt>) => {
      state.debts.push(action.payload);
    },
    removeDebt: (state, action: PayloadAction<string>) => {
      state.debts = state.debts.filter(debt => debt.id !== action.payload);
    },
    updateDebt: (state, action: PayloadAction<Debt>) => {
      const index = state.debts.findIndex(debt => debt.id === action.payload.id);
      if (index > -1) {
        state.debts[index] = action.payload;
      }
    },
    addCustomCategory: (state, action: PayloadAction<string>) => {
      if (!state.customCategories.includes(action.payload)) {
        state.customCategories.push(action.payload);
      }
    },
    removeCustomCategory: (state, action: PayloadAction<string>) => {
      state.customCategories = state.customCategories.filter(cat => cat !== action.payload);
    },
  },
});

export const {
  addBudgetItem,
  removeBudgetItem,
  updateBudgetItem,
  addDebt,
  removeDebt,
  updateDebt,
  addCustomCategory,
  removeCustomCategory,
} = financeSlice.actions;

export default financeSlice.reducer;
