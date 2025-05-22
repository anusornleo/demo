<template>
  <DefaultLayoutWithVerticalNav>
    <slot />
  </DefaultLayoutWithVerticalNav>
</template>

<script>
import DefaultLayoutWithVerticalNav from './components/DefaultLayoutWithVerticalNav.vue'
import { useAuthStore } from '@/stores/auth'

export default {
  components: {
    DefaultLayoutWithVerticalNav,
  },

  async mounted() {
    const auth = useAuthStore()
    auth.loadTokens()

    if (auth.accessToken && !auth.user) {
      await auth.fetchUser()
    }
  }
}
</script>

<style lang="scss">
@use "@layouts/styles/default-layout";
</style>
