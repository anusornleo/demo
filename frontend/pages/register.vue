<!--<script setup>-->
<!--import { useTheme } from 'vuetify'-->
<!--import AuthProvider from '@/views/pages/authentication/AuthProvider.vue'-->
<!--import logo from '@images/logo.svg?raw'-->
<!--import authV1MaskDark from '@images/pages/auth-v1-mask-dark.png'-->
<!--import authV1MaskLight from '@images/pages/auth-v1-mask-light.png'-->
<!--import authV1Tree2 from '@images/pages/auth-v1-tree-2.png'-->
<!--import authV1Tree from '@images/pages/auth-v1-tree.png'-->

<!--const form = ref({-->
<!--  username: '',-->
<!--  email: '',-->
<!--  password: '',-->
<!--  privacyPolicies: false,-->
<!--})-->

<!--const vuetifyTheme = useTheme()-->

<!--const authThemeMask = computed(() => {-->
<!--  return vuetifyTheme.global.name.value === 'light' ? authV1MaskLight : authV1MaskDark-->
<!--})-->

<!--const isPasswordVisible = ref(false)-->

<!--definePageMeta({ layout: 'blank' })-->
<!--</script>-->
<script>
import logo from '@images/logo.svg?raw'
definePageMeta({ layout: 'blank' })

export default {
  // layout: 'blank',
  data() {
    return {
      form: {
        username: '',
        email: '',
        password: '',
      },
      isPasswordVisible: false
    }
  },
  methods: {
    register() {
      this.$http.post('/api/authen/register/', this.form)
    }
  }
}
</script>

<template>
  <!-- eslint-disable vue/no-v-html -->

  <div class="auth-wrapper d-flex align-center justify-center pa-4">
    <VCard
      class="auth-card pa-4 pt-7"
      max-width="448"
    >
<!--      <VCardItem class="justify-center">-->
<!--        <NuxtLink-->
<!--          to="/"-->
<!--          class="d-flex align-center gap-3"-->
<!--        >-->
<!--          &lt;!&ndash; eslint-disable vue/no-v-html &ndash;&gt;-->
<!--          <div-->
<!--            class="d-flex"-->
<!--            v-html="logo"-->
<!--          />-->
<!--          <h2 class="font-weight-medium text-2xl text-uppercase">-->
<!--            Materio-->
<!--          </h2>-->
<!--        </NuxtLink>-->
<!--      </VCardItem>-->

      <VCardText class="pt-2">
        <h4 class="text-h4 mb-1">
          Adventure starts here 🚀
        </h4>
        <p class="mb-0">
          Make your app management easy and fun!
        </p>
      </VCardText>

      <VCardText>
        <v-form>
          <v-row>
            <!-- email -->
            <VCol cols="12">
              <VTextField
                :id="useId()"
                v-model="form.email"
                label="Email"
                placeholder="johndoe@email.com"
                type="email"
              />
            </VCol>

            <!-- Username -->
            <VCol cols="12">
              <VTextField
                :id="useId()"
                v-model="form.username"
                label="Username"
                placeholder="Johndoe"
              />
            </VCol>

            <!-- password -->
            <VCol cols="12">
              <VTextField
                :id="useId()"
                v-model="form.password"
                label="Password"
                placeholder="············"
                :type="isPasswordVisible ? 'text' : 'password'"
                autocomplete="password"
                :append-inner-icon="isPasswordVisible ? 'ri-eye-off-line' : 'ri-eye-line'"
                @click:append-inner="isPasswordVisible = !isPasswordVisible"
              />
              <div class="d-flex align-center my-6">
                <VCheckbox
                  id="privacy-policy"
                  v-model="form.privacyPolicies"
                  inline
                />
                <VLabel
                  for="privacy-policy"
                  style="opacity: 1;"
                >
                  <span class="me-1">I agree to</span>
                  <a
                    href="javascript:void(0)"
                    class="text-primary"
                  >privacy policy & terms</a>
                </VLabel>
              </div>

<!--              <VBtn-->
<!--                block-->
<!--                type="submit"-->
<!--                to="/"-->
<!--              >-->
<!--                Sign up-->
<!--              </VBtn>-->
              <v-btn @click="register()">Register</v-btn>
            </VCol>

            <!-- login instead -->
            <VCol
              cols="12"
              class="text-center text-base"
            >
              <span>Already have an account?</span>
              <NuxtLink
                class="text-primary ms-2"
                to="login"
              >
                Sign in instead
              </NuxtLink>
            </VCol>

<!--            <VCol-->
<!--              cols="12"-->
<!--              class="d-flex align-center"-->
<!--            >-->
<!--              <VDivider />-->
<!--              <span class="mx-4">or</span>-->
<!--              <VDivider />-->
<!--            </VCol>-->

            <!-- auth providers -->
            <VCol
              cols="12"
              class="text-center"
            >
              <AuthProvider />
            </VCol>
          </v-row>
        </v-form>
      </VCardText>
    </VCard>

<!--    <VImg-->
<!--      class="auth-footer-start-tree d-none d-md-block"-->
<!--      :src="authV1Tree"-->
<!--      :width="250"-->
<!--    />-->

<!--    <VImg-->
<!--      :src="authV1Tree2"-->
<!--      class="auth-footer-end-tree d-none d-md-block"-->
<!--      :width="350"-->
<!--    />-->

<!--    &lt;!&ndash; bg img &ndash;&gt;-->
<!--    <VImg-->
<!--      class="auth-footer-mask d-none d-md-block"-->
<!--      :src="authThemeMask"-->
<!--    />-->
  </div>
</template>

<style lang="scss">
@use "@core/scss/template/pages/page-auth";
</style>
