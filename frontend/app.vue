<script setup>

const { isMobile } = useDevice()
if (isMobile)
  configStore.appContentLayoutNav = 'vertical'
</script>

<template>
  <VApp>
    <NuxtLayout>
      <NuxtPage />
    </NuxtLayout>
<!--    <UpgradeToPro />-->
    <ConfirmDialog />
  </VApp>
</template>
