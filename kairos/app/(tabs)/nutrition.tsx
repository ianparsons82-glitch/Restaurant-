import React, { useState } from 'react';
import { View, ScrollView, StyleSheet, TouchableOpacity, Text, Modal, TextInput, FlatList } from 'react-native';
import { useSelector, useDispatch } from 'react-redux';
import { RootState, AppDispatch } from '@/redux/store';
import { addShoppingItem, removeShoppingItem, toggleShoppingItem, addMeal, removeMeal } from '@/redux/slices/nutritionSlice';
import { Colors } from '@/constants/colors';

export default function NutritionScreen() {
  const dispatch = useDispatch<AppDispatch>();
  const { meals, shoppingList } = useSelector((state: RootState) => state.nutrition);
  const [activeTab, setActiveTab] = useState<'shopping' | 'meals'>('shopping');
  const [modalVisible, setModalVisible] = useState(false);
  const [itemName, setItemName] = useState('');
  const [itemQuantity, setItemQuantity] = useState('');
  const [itemUnit, setItemUnit] = useState('');
  const [itemCategory, setItemCategory] = useState('Produce');

  const categories = ['Produce', 'Dairy', 'Meat', 'Grains', 'Frozen', 'Pantry'];

  const handleAddShoppingItem = () => {
    if (itemName) {
      dispatch(addShoppingItem({
        id: Date.now().toString(),
        item: itemName,
        quantity: itemQuantity ? parseFloat(itemQuantity) : undefined,
        unit: itemUnit,
        category: itemCategory,
        isPurchased: false,
        date: new Date().toISOString(),
      }));
      setItemName('');
      setItemQuantity('');
      setItemUnit('');
      setItemCategory('Produce');
      setModalVisible(false);
    }
  };

  const unpurchasedItems = shoppingList.filter(item => !item.isPurchased);
  const purchasedItems = shoppingList.filter(item => item.isPurchased);

  return (
    <View style={styles.container}>
      <View style={[styles.header, { backgroundColor: Colors.nutrition.primary }]}>
        <Text style={styles.headerTitle}>Nutrition Hub</Text>
        <View style={styles.tabContainer}>
          <TouchableOpacity
            style={[styles.tab, activeTab === 'shopping' && styles.activeTab]}
            onPress={() => setActiveTab('shopping')}>
            <Text style={[styles.tabText, activeTab === 'shopping' && styles.activeTabText]}>
              Shopping List
            </Text>
          </TouchableOpacity>
          <TouchableOpacity
            style={[styles.tab, activeTab === 'meals' && styles.activeTab]}
            onPress={() => setActiveTab('meals')}>
            <Text style={[styles.tabText, activeTab === 'meals' && styles.activeTabText]}>
              Meal Planner
            </Text>
          </TouchableOpacity>
        </View>
      </View>

      <ScrollView style={styles.content}>
        {activeTab === 'shopping' ? (
          <>
            <TouchableOpacity
              style={[styles.addButton, { backgroundColor: Colors.nutrition.primary }]}
              onPress={() => setModalVisible(true)}>
              <Text style={styles.addButtonText}>+ Add Item</Text>
            </TouchableOpacity>

            {unpurchasedItems.length > 0 && (
              <View>
                <Text style={styles.sectionTitle}>To Buy</Text>
                {unpurchasedItems.map((item) => (
                  <View key={item.id} style={[styles.shoppingItemCard, { borderLeftColor: Colors.nutrition.primary }]}>
                    <TouchableOpacity
                      style={styles.checkboxContainer}
                      onPress={() => dispatch(toggleShoppingItem(item.id))}>
                      <View style={[styles.checkbox, { borderColor: Colors.nutrition.primary }]} />
                    </TouchableOpacity>
                    <View style={styles.itemInfo}>
                      <Text style={styles.itemName}>{item.item}</Text>
                      <Text style={styles.itemCategory}>{item.category}</Text>
                      {item.quantity && <Text style={styles.itemQuantity}>{item.quantity} {item.unit}</Text>}
                    </View>
                    <TouchableOpacity onPress={() => dispatch(removeShoppingItem(item.id))}>
                      <Text style={styles.deleteText}>×</Text>
                    </TouchableOpacity>
                  </View>
                ))}
              </View>
            )}

            {purchasedItems.length > 0 && (
              <View style={{ marginTop: 20 }}>
                <Text style={styles.sectionTitle}>Purchased ({purchasedItems.length})</Text>
                {purchasedItems.map((item) => (
                  <View key={item.id} style={[styles.shoppingItemCard, { opacity: 0.6 }]}>
                    <TouchableOpacity
                      style={styles.checkboxContainer}
                      onPress={() => dispatch(toggleShoppingItem(item.id))}>
                      <View style={[styles.checkbox, styles.checkedCheckbox, { backgroundColor: Colors.nutrition.primary }]} />
                    </TouchableOpacity>
                    <View style={styles.itemInfo}>
                      <Text style={[styles.itemName, { textDecorationLine: 'line-through' }]}>{item.item}</Text>
                    </View>
                    <TouchableOpacity onPress={() => dispatch(removeShoppingItem(item.id))}>
                      <Text style={styles.deleteText}>×</Text>
                    </TouchableOpacity>
                  </View>
                ))}
              </View>
            )}
          </>
        ) : (
          <View>
            <Text style={styles.sectionTitle}>Weekly Meal Planner</Text>
            <Text style={{ textAlign: 'center', marginTop: 40, color: Colors.neutral.gray }}>
              Meal planning coming soon
            </Text>
          </View>
        )}
      </ScrollView>

      <Modal visible={modalVisible} transparent animationType="slide">
        <View style={styles.modalContainer}>
          <View style={styles.modalContent}>
            <Text style={styles.modalTitle}>Add Shopping Item</Text>

            <Text style={styles.label}>Item Name</Text>
            <TextInput
              style={styles.input}
              placeholder="e.g., Milk, Chicken, Carrots"
              value={itemName}
              onChangeText={setItemName}
            />

            <Text style={styles.label}>Category</Text>
            <FlatList
              data={categories}
              keyExtractor={(item) => item}
              renderItem={({ item }) => (
                <TouchableOpacity
                  style={[
                    styles.categoryButton,
                    itemCategory === item && { backgroundColor: Colors.nutrition.primary },
                  ]}
                  onPress={() => setItemCategory(item)}>
                  <Text style={[styles.categoryButtonText, itemCategory === item && { color: Colors.neutral.white }]}>
                    {item}
                  </Text>
                </TouchableOpacity>
              )}
              scrollEnabled={false}
              numColumns={2}
            />

            <Text style={styles.label}>Quantity (optional)</Text>
            <View style={styles.quantityRow}>
              <TextInput
                style={[styles.input, { flex: 1 }]}
                placeholder="Amount"
                value={itemQuantity}
                onChangeText={setItemQuantity}
                keyboardType="decimal-pad"
              />
              <TextInput
                style={[styles.input, { flex: 1, marginLeft: 8 }]}
                placeholder="kg, lbs, etc"
                value={itemUnit}
                onChangeText={setItemUnit}
              />
            </View>

            <View style={styles.buttonRow}>
              <TouchableOpacity
                style={[styles.modalButton, { backgroundColor: Colors.nutrition.primary }]}
                onPress={handleAddShoppingItem}>
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
    marginBottom: 16,
  },
  tabContainer: {
    flexDirection: 'row',
    gap: 8,
  },
  tab: {
    flex: 1,
    paddingVertical: 8,
    paddingHorizontal: 12,
    borderRadius: 8,
    backgroundColor: 'rgba(255,255,255,0.2)',
  },
  activeTab: {
    backgroundColor: Colors.neutral.white,
  },
  tabText: {
    color: 'rgba(255,255,255,0.7)',
    textAlign: 'center',
    fontWeight: '600',
  },
  activeTabText: {
    color: Colors.nutrition.primary,
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
  sectionTitle: {
    fontSize: 18,
    fontWeight: 'bold',
    color: Colors.nutrition.primary,
    marginBottom: 12,
    marginTop: 8,
  },
  shoppingItemCard: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: Colors.nutrition.light,
    padding: 12,
    borderRadius: 12,
    marginBottom: 10,
    borderLeftWidth: 4,
  },
  checkboxContainer: {
    marginRight: 12,
  },
  checkbox: {
    width: 24,
    height: 24,
    borderRadius: 6,
    borderWidth: 2,
  },
  checkedCheckbox: {
    borderWidth: 0,
  },
  itemInfo: {
    flex: 1,
  },
  itemName: {
    fontSize: 16,
    fontWeight: '600',
    color: Colors.nutrition.dark,
    marginBottom: 2,
  },
  itemCategory: {
    fontSize: 12,
    color: Colors.neutral.gray,
  },
  itemQuantity: {
    fontSize: 12,
    color: Colors.nutrition.primary,
    fontWeight: '500',
  },
  deleteText: {
    fontSize: 24,
    color: Colors.error,
    marginLeft: 8,
  },
  categoryButton: {
    flex: 1,
    padding: 12,
    margin: 4,
    backgroundColor: Colors.nutrition.light,
    borderRadius: 8,
    alignItems: 'center',
  },
  categoryButtonText: {
    fontWeight: '600',
    color: Colors.nutrition.primary,
  },
  label: {
    fontSize: 14,
    fontWeight: '600',
    marginBottom: 8,
    color: Colors.neutral.darkGray,
    marginTop: 12,
  },
  input: {
    borderWidth: 1,
    borderColor: Colors.neutral.gray,
    borderRadius: 8,
    padding: 12,
    fontSize: 14,
  },
  quantityRow: {
    flexDirection: 'row',
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
    color: Colors.nutrition.primary,
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
