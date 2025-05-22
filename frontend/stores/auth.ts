import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'
const router = useRouter()

export const useAuthStore = defineStore('auth', {
  state: () => ({
    accessToken: '',
    refreshToken: '',
    user: null as null | Record<string, any>,
  }),

  getters: {
    isAuthenticated: (state) => !!state.accessToken && !!state.user,
  },

  actions: {
    setTokens(access: string, refresh: string) {
      this.accessToken = access
      this.refreshToken = refresh
      console.log(access)
      console.log(refresh)
      localStorage.setItem('access_token', access)
      localStorage.setItem('refresh_token', refresh)
    },

    loadTokens() {
      console.log('1')
      this.accessToken = localStorage.getItem('access_token') || ''
      this.refreshToken = localStorage.getItem('refresh_token') || ''
      console.log('2')
    },

    clearTokens() {
      this.accessToken = ''
      this.refreshToken = ''
      localStorage.removeItem('access_token')
      localStorage.removeItem('refresh_token')
    },

     async refreshAccessToken(): Promise<boolean> {
      const { $http } = useNuxtApp()
      try {
        const res = await $http.post('api/authen/token/refresh/', {
          refresh: this.refreshToken,
        })

        this.accessToken = res.data.access
        localStorage.setItem('access_token', res.data.access)
        return true
      } catch (err) {
        this.clearTokens()
        return false
      }
    },

    async fetchUser() {
      const { $http } = useNuxtApp()
      try {
        const res = await $http.get('/api/authen/me/')
        this.user = res.data
        return this.user
      } catch (err) {
        this.user = null
        return null
      }
    },

    async logout() {
      this.clearTokens()
      this.user = null
      // await router.push('/login')
    },
  },
})
