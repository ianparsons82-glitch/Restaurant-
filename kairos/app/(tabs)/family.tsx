import React, { useState } from 'react';
import { View, ScrollView, StyleSheet, TouchableOpacity, Text, Modal, TextInput, FlatList } from 'react-native';
import { useSelector, useDispatch } from 'react-redux';
import { RootState, AppDispatch } from '@/redux/store';
import {
  addChore,
  removeChore,
  toggleChoreComplete,
  addRewardChart,
  removeRewardChart,
  updateRewardChart,
  addStarToChart,
  removeStarFromChart,
} from '@/redux/slices/familySlice';
import { Colors } from '@/constants/colors';

export default function FamilyScreen() {
  const dispatch = useDispatch<AppDispatch>();
  const { chores, rewardCharts } = useSelector((state: RootState) => state.family);
  const [activeTab, setActiveTab] = useState<'chores' | 'rewards'>('chores');
  const [modalVisible, setModalVisible] = useState(false);
  const [choreData, setChoreData] = useState({ name: '', assignedTo: '', frequency: 'weekly' });
  const [rewardData, setRewardData] = useState({ childName: '', targetStars: '10' });

  const frequencies = ['daily', 'weekly', 'monthly'];

  const handleAddChore = () => {
    if (choreData.name) {
      dispatch(addChore({
        id: Date.now().toString(),
        name: choreData.name,
        assignedTo: choreData.assignedTo || 'Unassigned',
        frequency: choreData.frequency as any,
        completed: false,
        date: new Date().toISOString(),
      }));
      setChoreData({ name: '', assignedTo: '', frequency: 'weekly' });
      setModalVisible(false);
    }
  };

  const handleAddRewardChart = () => {
    if (rewardData.childName) {
      dispatch(addRewardChart({
        id: Date.now().toString(),
        childName: rewardData.childName,
        targetStars: parseInt(rewardData.targetStars) || 10,
        currentStars: 0,
        rewards: [],
        date: new Date().toISOString(),
      }));
      setRewardData({ childName: '', targetStars: '10' });
      setModalVisible(false);
    }
  };

  const completedChores = chores.filter(c => c.completed).length;
  const totalChores = chores.length;

  return (
    <View style={styles.container}>
      <View style={[styles.header, { backgroundColor: Colors.family.primary }]}>
        <Text style={styles.headerTitle}>Family Hub</Text>
        <View style={styles.tabContainer}>
          <TouchableOpacity
            style={[styles.tab, activeTab === 'chores' && styles.activeTab]}
            onPress={() => setActiveTab('chores')}>
            <Text style={[styles.tabText, activeTab === 'chores' && styles.activeTabText]}>
              Chores
            </Text>
          </TouchableOpacity>
          <TouchableOpacity
            style={[styles.tab, activeTab === 'rewards' && styles.activeTab]}
            onPress={() => setActiveTab('rewards')}>
            <Text style={[styles.tabText, activeTab === 'rewards' && styles.activeTabText]}>
              Rewards
            </Text>
          </TouchableOpacity>
        </View>
      </View>

      <ScrollView style={styles.content}>
        {activeTab === 'chores' ? (
          <>
            <View style={styles.statsCard}>
              <Text style={styles.statsTitle}>Completion Rate</Text>
              <Text style={styles.statsValue}>
                {totalChores > 0 ? `${Math.round((completedChores / totalChores) * 100)}%` : 'No chores'}
              </Text>
              <View style={styles.progressBar}>
                <View
                  style={[
                    styles.progressFill,
                    { width: totalChores > 0 ? `${(completedChores / totalChores) * 100}%` : '0%', backgroundColor: Colors.family.primary },
                  ]}
                />
              </View>
            </View>

            <TouchableOpacity
              style={[styles.addButton, { backgroundColor: Colors.family.primary }]}
              onPress={() => setModalVisible(true)}>
              <Text style={styles.addButtonText}>+ Add Chore</Text>
            </TouchableOpacity>

            <View>
              {chores.map((chore) => (
                <View key={chore.id} style={[styles.choreCard, chore.completed && styles.completedChore]}>
                  <TouchableOpacity
                    style={styles.checkboxContainer}
                    onPress={() => dispatch(toggleChoreComplete(chore.id))}>
                    <View
                      style={[
                        styles.checkbox,
                        chore.completed && { backgroundColor: Colors.family.primary, borderWidth: 0 },
                      ]}
                    />
                  </TouchableOpacity>
                  <View style={styles.choreInfo}>
                    <Text style={[styles.choreName, chore.completed && { textDecorationLine: 'line-through' }]}>
                      {chore.name}
                    </Text>
                    <Text style={styles.choreDetails}>
                      {chore.assignedTo} • {chore.frequency}
                    </Text>
                  </View>
                  <TouchableOpacity onPress={() => dispatch(removeChore(chore.id))}>
                    <Text style={styles.deleteText}>×</Text>
                  </TouchableOpacity>
                </View>
              ))}
            </View>
          </>
        ) : (
          <>
            <TouchableOpacity
              style={[styles.addButton, { backgroundColor: Colors.family.primary }]}
              onPress={() => setModalVisible(true)}>
              <Text style={styles.addButtonText}>+ Create Reward Chart</Text>
            </TouchableOpacity>

            {rewardCharts.map((chart) => (
              <View key={chart.id} style={styles.rewardCard}>
                <View style={styles.rewardHeader}>
                  <Text style={styles.childName}>{chart.childName}</Text>
                  <TouchableOpacity onPress={() => dispatch(removeRewardChart(chart.id))}>
                    <Text style={styles.deleteText}>×</Text>
                  </TouchableOpacity>
                </View>

                <View style={styles.starContainer}>
                  {[...Array(chart.targetStars)].map((_, idx) => (
                    <TouchableOpacity
                      key={idx}
                      style={[
                        styles.star,
                        idx < chart.currentStars && { backgroundColor: Colors.family.primary },
                      ]}
                      onPress={() => {
                        if (idx < chart.currentStars) {
                          dispatch(removeStarFromChart(chart.id));
                        } else if (idx === chart.currentStars) {
                          dispatch(addStarToChart(chart.id));
                        }
                      }}>
                      <Text style={styles.starText}>★</Text>
                    </TouchableOpacity>
                  ))}
                </View>

                <Text style={styles.progressText}>
                  {chart.currentStars} / {chart.targetStars} stars
                </Text>

                {chart.currentStars === chart.targetStars && (
                  <View style={styles.successBanner}>
                    <Text style={styles.successText}>🎉 Goal Reached!</Text>
                  </View>
                )}
              </View>
            ))}
          </>
        )}
      </ScrollView>

      <Modal visible={modalVisible} transparent animationType="slide">
        <View style={styles.modalContainer}>
          <View style={styles.modalContent}>
            {activeTab === 'chores' ? (
              <>
                <Text style={styles.modalTitle}>Add Chore</Text>

                <Text style={styles.label}>Chore Name</Text>
                <TextInput
                  style={styles.input}
                  placeholder="e.g., Do dishes, Clean room"
                  value={choreData.name}
                  onChangeText={(text) => setChoreData({ ...choreData, name: text })}
                />

                <Text style={styles.label}>Assigned To</Text>
                <TextInput
                  style={styles.input}
                  placeholder="Family member name"
                  value={choreData.assignedTo}
                  onChangeText={(text) => setChoreData({ ...choreData, assignedTo: text })}
                />

                <Text style={styles.label}>Frequency</Text>
                <FlatList
                  data={frequencies}
                  keyExtractor={(item) => item}
                  renderItem={({ item }) => (
                    <TouchableOpacity
                      style={[
                        styles.frequencyButton,
                        choreData.frequency === item && { backgroundColor: Colors.family.primary },
                      ]}
                      onPress={() => setChoreData({ ...choreData, frequency: item })}>
                      <Text
                        style={[
                          styles.frequencyButtonText,
                          choreData.frequency === item && { color: Colors.neutral.white },
                        ]}>
                        {item.charAt(0).toUpperCase() + item.slice(1)}
                      </Text>
                    </TouchableOpacity>
                  )}
                  scrollEnabled={false}
                  numColumns={3}
                />

                <View style={styles.buttonRow}>
                  <TouchableOpacity
                    style={[styles.modalButton, { backgroundColor: Colors.family.primary }]}
                    onPress={handleAddChore}>
                    <Text style={styles.modalButtonText}>Add</Text>
                  </TouchableOpacity>
                  <TouchableOpacity
                    style={[styles.modalButton, { backgroundColor: Colors.neutral.gray }]}
                    onPress={() => setModalVisible(false)}>
                    <Text style={styles.modalButtonText}>Cancel</Text>
                  </TouchableOpacity>
                </View>
              </>
            ) : (
              <>
                <Text style={styles.modalTitle}>Create Reward Chart</Text>

                <Text style={styles.label}>Child Name</Text>
                <TextInput
                  style={styles.input}
                  placeholder="e.g., Emma, Lucas"
                  value={rewardData.childName}
                  onChangeText={(text) => setRewardData({ ...rewardData, childName: text })}
                />

                <Text style={styles.label}>Target Stars</Text>
                <TextInput
                  style={styles.input}
                  placeholder="10"
                  value={rewardData.targetStars}
                  onChangeText={(text) => setRewardData({ ...rewardData, targetStars: text })}
                  keyboardType="number-pad"
                />

                <View style={styles.buttonRow}>
                  <TouchableOpacity
                    style={[styles.modalButton, { backgroundColor: Colors.family.primary }]}
                    onPress={handleAddRewardChart}>
                    <Text style={styles.modalButtonText}>Create</Text>
                  </TouchableOpacity>
                  <TouchableOpacity
                    style={[styles.modalButton, { backgroundColor: Colors.neutral.gray }]}
                    onPress={() => setModalVisible(false)}>
                    <Text style={styles.modalButtonText}>Cancel</Text>
                  </TouchableOpacity>
                </View>
              </>
            )}
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
    color: Colors.family.primary,
  },
  content: {
    flex: 1,
    padding: 16,
  },
  statsCard: {
    backgroundColor: Colors.family.light,
    padding: 16,
    borderRadius: 12,
    marginBottom: 20,
  },
  statsTitle: {
    fontSize: 14,
    color: Colors.family.primary,
    fontWeight: '600',
    marginBottom: 8,
  },
  statsValue: {
    fontSize: 32,
    fontWeight: 'bold',
    color: Colors.family.primary,
    marginBottom: 12,
  },
  progressBar: {
    height: 8,
    backgroundColor: Colors.neutral.lightGray,
    borderRadius: 4,
    overflow: 'hidden',
  },
  progressFill: {
    height: '100%',
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
  choreCard: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: Colors.family.light,
    padding: 12,
    borderRadius: 12,
    marginBottom: 10,
    borderLeftWidth: 4,
    borderLeftColor: Colors.family.primary,
  },
  completedChore: {
    opacity: 0.6,
  },
  checkboxContainer: {
    marginRight: 12,
  },
  checkbox: {
    width: 24,
    height: 24,
    borderRadius: 6,
    borderWidth: 2,
    borderColor: Colors.family.primary,
  },
  choreInfo: {
    flex: 1,
  },
  choreName: {
    fontSize: 16,
    fontWeight: '600',
    color: Colors.family.dark,
    marginBottom: 2,
  },
  choreDetails: {
    fontSize: 12,
    color: Colors.neutral.gray,
  },
  deleteText: {
    fontSize: 24,
    color: Colors.error,
    marginLeft: 8,
  },
  rewardCard: {
    backgroundColor: Colors.family.light,
    padding: 16,
    borderRadius: 12,
    marginBottom: 16,
  },
  rewardHeader: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: 16,
  },
  childName: {
    fontSize: 18,
    fontWeight: 'bold',
    color: Colors.family.primary,
  },
  starContainer: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    gap: 8,
    marginBottom: 12,
  },
  star: {
    width: 48,
    height: 48,
    borderRadius: 24,
    backgroundColor: Colors.neutral.lightGray,
    justifyContent: 'center',
    alignItems: 'center',
    borderWidth: 2,
    borderColor: Colors.family.primary,
  },
  starText: {
    fontSize: 24,
    color: Colors.family.primary,
  },
  progressText: {
    textAlign: 'center',
    color: Colors.neutral.gray,
    fontSize: 12,
    marginBottom: 8,
  },
  successBanner: {
    backgroundColor: Colors.success,
    padding: 12,
    borderRadius: 8,
    alignItems: 'center',
  },
  successText: {
    color: Colors.neutral.white,
    fontWeight: 'bold',
    fontSize: 14,
  },
  frequencyButton: {
    flex: 1,
    padding: 10,
    margin: 4,
    backgroundColor: Colors.family.light,
    borderRadius: 8,
    alignItems: 'center',
  },
  frequencyButtonText: {
    fontWeight: '600',
    color: Colors.family.primary,
    fontSize: 12,
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
    color: Colors.family.primary,
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
