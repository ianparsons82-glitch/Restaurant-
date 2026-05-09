import { createSlice, PayloadAction } from '@reduxjs/toolkit';

export interface Chore {
  id: string;
  name: string;
  assignedTo?: string;
  frequency: 'daily' | 'weekly' | 'monthly' | 'custom';
  completed: boolean;
  dueDate?: string;
  date: string;
}

export interface RewardChart {
  id: string;
  childName: string;
  targetStars: number;
  currentStars: number;
  rewards: string[];
  date: string;
}

interface FamilyState {
  chores: Chore[];
  rewardCharts: RewardChart[];
  customChoreFrequencies: string[];
  familyMembers: string[];
}

const initialState: FamilyState = {
  chores: [],
  rewardCharts: [],
  customChoreFrequencies: [],
  familyMembers: [],
};

const familySlice = createSlice({
  name: 'family',
  initialState,
  reducers: {
    addChore: (state, action: PayloadAction<Chore>) => {
      state.chores.push(action.payload);
    },
    removeChore: (state, action: PayloadAction<string>) => {
      state.chores = state.chores.filter(chore => chore.id !== action.payload);
    },
    updateChore: (state, action: PayloadAction<Chore>) => {
      const index = state.chores.findIndex(chore => chore.id === action.payload.id);
      if (index > -1) {
        state.chores[index] = action.payload;
      }
    },
    toggleChoreComplete: (state, action: PayloadAction<string>) => {
      const chore = state.chores.find(chore => chore.id === action.payload);
      if (chore) {
        chore.completed = !chore.completed;
      }
    },
    addRewardChart: (state, action: PayloadAction<RewardChart>) => {
      state.rewardCharts.push(action.payload);
    },
    removeRewardChart: (state, action: PayloadAction<string>) => {
      state.rewardCharts = state.rewardCharts.filter(chart => chart.id !== action.payload);
    },
    updateRewardChart: (state, action: PayloadAction<RewardChart>) => {
      const index = state.rewardCharts.findIndex(chart => chart.id === action.payload.id);
      if (index > -1) {
        state.rewardCharts[index] = action.payload;
      }
    },
    addStarToChart: (state, action: PayloadAction<string>) => {
      const chart = state.rewardCharts.find(chart => chart.id === action.payload);
      if (chart && chart.currentStars < chart.targetStars) {
        chart.currentStars += 1;
      }
    },
    removeStarFromChart: (state, action: PayloadAction<string>) => {
      const chart = state.rewardCharts.find(chart => chart.id === action.payload);
      if (chart && chart.currentStars > 0) {
        chart.currentStars -= 1;
      }
    },
    addFamilyMember: (state, action: PayloadAction<string>) => {
      if (!state.familyMembers.includes(action.payload)) {
        state.familyMembers.push(action.payload);
      }
    },
    removeFamilyMember: (state, action: PayloadAction<string>) => {
      state.familyMembers = state.familyMembers.filter(member => member !== action.payload);
    },
    addCustomChoreFrequency: (state, action: PayloadAction<string>) => {
      if (!state.customChoreFrequencies.includes(action.payload)) {
        state.customChoreFrequencies.push(action.payload);
      }
    },
    removeCustomChoreFrequency: (state, action: PayloadAction<string>) => {
      state.customChoreFrequencies = state.customChoreFrequencies.filter(
        freq => freq !== action.payload
      );
    },
  },
});

export const {
  addChore,
  removeChore,
  updateChore,
  toggleChoreComplete,
  addRewardChart,
  removeRewardChart,
  updateRewardChart,
  addStarToChart,
  removeStarFromChart,
  addFamilyMember,
  removeFamilyMember,
  addCustomChoreFrequency,
  removeCustomChoreFrequency,
} = familySlice.actions;

export default familySlice.reducer;
