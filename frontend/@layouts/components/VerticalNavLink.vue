<script setup>
import { NuxtLink } from '#components'


const props = defineProps({
  item: {
    type: null,
    required: true,
  },
})
</script>

<template>
  <li
    class="nav-link"
    :class="{ disabled: item.disable }"
  >
    <Component
      :is="item.to ? NuxtLink : 'a'"
      :to="item.to"
      :href="item.href"
      :target="item.target"
    >
      <v-icon>{{item.icon || 'mdi-circle-outline'}}</v-icon>
<!--      <VIcon-->
<!--        :icon="item.icon || 'ri-checkbox-blank-circle-line'"-->
<!--        class="nav-item-icon"-->
<!--      />-->
      <!-- 👉 Title -->
      <span class="nav-item-title">
        {{ item.title }}
      </span>
      <span
        class="nav-item-badge"
        :class="item.badgeClass"
      >
        {{ item.badgeContent }}
      </span>
    </Component>
  </li>
</template>

<style lang="scss">
.layout-vertical-nav {
  .nav-link a {
    display: flex;
    align-items: center;
    cursor: pointer;
  }
}
</style>
