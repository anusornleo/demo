<template>
  <VDialog v-model="dialog.show" persistent max-width="400">
    <VCard>
      <VCardTitle>{{ dialog.title }}</VCardTitle>
      <VCardText>{{ dialog.message }}</VCardText>
      <VCardActions class="justify-end">
        <VBtn @click="dialog.resolveDialog(false)" color="secondary">ยกเลิก</VBtn>
        <VBtn @click="dialog.resolveDialog(true)" color="primary">ตกลง</VBtn>
      </VCardActions>
    </VCard>
  </VDialog>
</template>

<script setup>
import { useDialogStore } from '@/stores/dialog'
const dialog = useDialogStore()
</script>
