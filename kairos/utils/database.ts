import * as SQLite from 'expo-sqlite';

const db = SQLite.openDatabaseSync('kairos.db');

export async function initializeDatabase() {
  try {
    await db.execAsync(`
      CREATE TABLE IF NOT EXISTS budget_items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        category TEXT NOT NULL,
        amount REAL NOT NULL,
        date TEXT DEFAULT CURRENT_TIMESTAMP,
        isCustom INTEGER DEFAULT 0
      );

      CREATE TABLE IF NOT EXISTS debts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        amount REAL NOT NULL,
        interestRate REAL,
        minPayment REAL,
        dueDate TEXT,
        date TEXT DEFAULT CURRENT_TIMESTAMP
      );

      CREATE TABLE IF NOT EXISTS meals (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        day TEXT NOT NULL,
        mealType TEXT NOT NULL,
        name TEXT NOT NULL,
        ingredients TEXT,
        calories REAL,
        date TEXT DEFAULT CURRENT_TIMESTAMP
      );

      CREATE TABLE IF NOT EXISTS shopping_items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        item TEXT NOT NULL,
        quantity REAL,
        unit TEXT,
        category TEXT,
        isPurchased INTEGER DEFAULT 0,
        date TEXT DEFAULT CURRENT_TIMESTAMP
      );

      CREATE TABLE IF NOT EXISTS chores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        assignedTo TEXT,
        frequency TEXT,
        completed INTEGER DEFAULT 0,
        dueDate TEXT,
        date TEXT DEFAULT CURRENT_TIMESTAMP
      );

      CREATE TABLE IF NOT EXISTS rewards (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        childName TEXT NOT NULL,
        targetStars INTEGER,
        currentStars INTEGER DEFAULT 0,
        rewards TEXT,
        date TEXT DEFAULT CURRENT_TIMESTAMP
      );
    `);
  } catch (error) {
    console.error('Database initialization error:', error);
  }
}

export function getDatabase() {
  return db;
}
