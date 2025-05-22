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
          Welcome to Materio! 👋🏻
        </h4>
        <p class="mb-0">
          Please sign-in to your account and start the adventure
        </p>
      </VCardText>

      <VCardText>
        <VForm @submit.prevent="() => {}">
          <VRow>
            <!-- email -->
            <VCol cols="12">
              <VTextField
                :id="useId()"
                v-model="form.email_or_username"
                :rules="[$rules.required, $rules.email]"
                label="Email"
                type="email"
              />
            </VCol>

            <!-- password -->
            <VCol cols="12">
              <VTextField
                :id="useId()"
                v-model="form.password"
                label="Password"
                placeholder="············"
                :type="is_password_visible ? 'text' : 'password'"
                autocomplete="password"
                :append-inner-icon="is_password_visible ? 'ri-eye-off-line' : 'ri-eye-line'"
                @click:append-inner="is_password_visible = !is_password_visible"
              />

              <!-- remember me checkbox -->
              <div class="d-flex align-center justify-space-between flex-wrap my-6">
<!--                <VCheckbox-->
<!--                  :id="useId()"-->
<!--                  v-model="form.remember"-->
<!--                  label="Remember me"-->
<!--                />-->

                <a
                  class="text-primary"
                  href="javascript:void(0)"
                >
                  Forgot Password?
                </a>
              </div>

              <!-- login button -->
              <VBtn
                block
                @click="login()"
              >
                Login
              </VBtn>
            </VCol>

            <!-- create account -->
            <VCol
              cols="12"
              class="text-center text-base"
            >
              <span>New on our platform?</span>
              <NuxtLink
                class="text-primary ms-2"
                to="/register"
              >
                Create an account
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
<!--            <VCol-->
<!--              cols="12"-->
<!--              class="text-center"-->
<!--            >-->
<!--              <AuthProvider />-->
<!--            </VCol>-->
          </VRow>
        </VForm>
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

    <!-- bg img -->
<!--    <VImg-->
<!--      class="auth-footer-mask d-none d-md-block"-->
<!--      :src="authThemeMask"-->
<!--    />-->
  </div>
</template>

<script>
import { useAuthStore } from '@/stores/auth'
definePageMeta({ layout: 'blank' })

export default {
  // layout: 'blank',
  // layout: 'test',
  data() {
    return {
      form: { email_or_username: '', password: '' },
      is_password_visible: false
    }
  },
  methods: {
    async login() {
      console.log('cccc')
      try {
        const res = await this.$http.post('/api/authen/login/', this.form)

        const auth = useAuthStore()
        console.log(res.data)
        auth.setTokens(res.data.access, res.data.refresh)

        this.$router.push('/')
      } catch (err) {
        alert('Login failed')
      }
    }
  }
}
</script>

<style lang="scss">
@use "@core/scss/template/pages/page-auth";
</style>
