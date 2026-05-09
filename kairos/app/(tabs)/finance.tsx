import React, { useState } from 'react';
import { View, ScrollView, StyleSheet, TouchableOpacity, Text, Modal, TextInput, FlatList } from 'react-native';
import { useSelector, useDispatch } from 'react-redux';
import { RootState, AppDispatch } from '@/redux/store';
import { addBudgetItem, removeBudgetItem, addCustomCategory } from '@/redux/slices/financeSlice';
import { Colors } from '@/constants/colors';

export default function FinanceScreen() {
  const dispatch = useDispatch<AppDispatch>();
  const { budgetItems, customCategories } = useSelector((state: RootState) => state.finance);
  const [modalVisible, setModalVisible] = useState(false);
  const [newCategory, setNewCategory] = useState('');
  const [newAmount, setNewAmount] = useState('');

  const predefinedCategories = ['Housing', 'Food', 'Transport', 'Utilities', 'Entertainment'];
  const allCategories = [...predefinedCategories, ...customCategories];

  const handleAddBudgetItem = () => {
    if (newCategory && newAmount) {
      dispatch(addBudgetItem({
        id: Date.now().toString(),
        category: newCategory,
        amount: parseFloat(newAmount),
        date: new Date().toISOString(),
        isCustom: !predefinedCategories.includes(newCategory),
      }));
      setNewCategory('');
      setNewAmount('');
      setModalVisible(false);
    }
  };

  const handleAddCustomCategory = () => {
    if (newCategory && !allCategories.includes(newCategory)) {
      dispatch(addCustomCategory(newCategory));
    }
  };

  const totalBudget = budgetItems.reduce((sum, item) => sum + item.amount, 0);

  return (
    <View style={styles.container}>
      <View style={[styles.header, { backgroundColor: Colors.finance.primary }]}>
        <Text style={styles.headerTitle}>Finance Tracker</Text>
        <Text style={styles.totalBudget}>Total: ${totalBudget.toFixed(2)}</Text>
      </View>

      <ScrollView style={styles.content}>
        <TouchableOpacity
          style={[styles.addButton, { backgroundColor: Colors.finance.primary }]}
          onPress={() => setModalVisible(true)}>
          <Text style={styles.addButtonText}>+ Add Budget Item</Text>
        </TouchableOpacity>

        <View style={styles.itemsContainer}>
          {budgetItems.map((item) => (
            <View key={item.id} style={styles.budgetItemCard}>
              <View style={styles.itemInfo}>
                <Text style={styles.itemCategory}>{item.category}</Text>
                <Text style={styles.itemAmount}>${item.amount.toFixed(2)}</Text>
              </View>
              <TouchableOpacity
                onPress={() => dispatch(removeBudgetItem(item.id))}
                style={styles.deleteButton}>
                <Text style={styles.deleteButtonText}>Delete</Text>
              </TouchableOpacity>
            </View>
          ))}
        </View>
      </ScrollView>

      <Modal visible={modalVisible} transparent animationType="slide">
        <View style={styles.modalContainer}>
          <View style={styles.modalContent}>
            <Text style={styles.modalTitle}>Add Budget Item</Text>

            <Text style={styles.label}>Category</Text>
            <FlatList
              data={allCategories}
              keyExtractor={(item, idx) => idx.toString()}
              renderItem={({ item }) => (
                <TouchableOpacity
                  style={[
                    styles.categoryButton,
                    newCategory === item && { backgroundColor: Colors.finance.primary },
                  ]}
                  onPress={() => setNewCategory(item)}>
                  <Text style={[styles.categoryButtonText, newCategory === item && { color: Colors.neutral.white }]}>
                    {item}
                  </Text>
                </TouchableOpacity>
              )}
              scrollEnabled={false}
              numColumns={2}
            />

            <TextInput
              style={styles.customInput}
              placeholder="Custom category (optional)"
              value={newCategory}
              onChangeText={setNewCategory}
            />
            <TouchableOpacity
              style={[styles.smallButton, { backgroundColor: Colors.finance.light }]}
              onPress={handleAddCustomCategory}>
              <Text style={styles.smallButtonText}>+ Add Custom Category</Text>
            </TouchableOpacity>

            <Text style={[styles.label, { marginTop: 20 }]}>Amount</Text>
            <TextInput
              style={styles.input}
              placeholder="Enter amount"
              value={newAmount}
              onChangeText={setNewAmount}
              keyboardType="decimal-pad"
            />

            <View style={styles.buttonRow}>
              <TouchableOpacity
                style={[styles.modalButton, { backgroundColor: Colors.finance.primary }]}
                onPress={handleAddBudgetItem}>
                <Text style={styles.modalButtonText}>Add</Text>
              </TouchableOpacity>
              <TouchableOpacity
                style={[styles.modalButton, { backgroundColor: Colors.neutral.gray }]}
                onPress={() => setModalVisible(false)}>
                <Text style={styles.modalButtonText}>Cancel</Text>
              </TouchableOpacity>
            </View>
          </View>
        </View>
      </Modal>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: Colors.neutral.white,
  },
  header: {
    paddingTop: 50,
    paddingBottom: 20,
    paddingHorizontal: 20,
  },
  headerTitle: {
    fontSize: 28,
    fontWeight: 'bold',
    color: Colors.neutral.white,
    marginBottom: 10,
  },
  totalBudget: {
    fontSize: 24,
    color: Colors.neutral.white,
    fontWeight: '600',
  },
  content: {
    flex: 1,
    padding: 16,
  },
  addButton: {
    padding: 16,
    borderRadius: 12,
    alignItems: 'center',
    marginBottom: 20,
  },
  addButtonText: {
    color: Colors.neutral.white,
    fontSize: 16,
    fontWeight: '600',
  },
  itemsContainer: {
    gap: 12,
  },
  budgetItemCard: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    backgroundColor: Colors.finance.light,
    padding: 16,
    borderRadius: 12,
    borderLeftWidth: 4,
    borderLeftColor: Colors.finance.primary,
  },
  itemInfo: {
    flex: 1,
  },
  itemCategory: {
    fontSize: 16,
    fontWeight: '600',
    color: Colors.finance.dark,
    marginBottom: 4,
  },
  itemAmount: {
    fontSize: 18,
    fontWeight: 'bold',
    color: Colors.finance.primary,
  },
  deleteButton: {
    paddingHorizontal: 12,
    paddingVertical: 6,
    backgroundColor: Colors.error,
    borderRadius: 6,
  },
  deleteButtonText: {
    color: Colors.neutral.white,
    fontSize: 12,
    fontWeight: '600',
  },
  modalContainer: {
    flex: 1,
    backgroundColor: 'rgba(0,0,0,0.5)',
    justifyContent: 'flex-end',
  },
  modalContent: {
    backgroundColor: Colors.neutral.white,
    padding: 20,
    borderTopLeftRadius: 20,
    borderTopRightRadius: 20,
    maxHeight: '90%',
  },
  modalTitle: {
    fontSize: 20,
    fontWeight: 'bold',
    marginBottom: 20,
    color: Colors.finance.primary,
  },
  label: {
    fontSize: 14,
    fontWeight: '600',
    marginBottom: 8,
    color: Colors.neutral.darkGray,
  },
  categoryButton: {
    flex: 1,
    padding: 12,
    margin: 4,
    backgroundColor: Colors.finance.light,
    borderRadius: 8,
    alignItems: 'center',
  },
  categoryButtonText: {
    fontWeight: '600',
    color: Colors.finance.primary,
  },
  customInput: {
    borderWidth: 1,
    borderColor: Colors.neutral.gray,
    borderRadius: 8,
    padding: 12,
    marginTop: 10,
    fontSize: 14,
  },
  smallButton: {
    padding: 10,
    borderRadius: 8,
    alignItems: 'center',
    marginTop: 8,
  },
  smallButtonText: {
    color: Colors.finance.primary,
    fontSize: 12,
    fontWeight: '600',
  },
  input: {
    borderWidth: 1,
    borderColor: Colors.neutral.gray,
    borderRadius: 8,
    padding: 12,
    fontSize: 14,
  },
  buttonRow: {
    flexDirection: 'row',
    gap: 12,
    marginTop: 20,
  },
  modalButton: {
    flex: 1,
    padding: 14,
    borderRadius: 8,
    alignItems: 'center',
  },
  modalButtonText: {
    color: Colors.neutral.white,
    fontSize: 16,
    fontWeight: '600',
  },
});
