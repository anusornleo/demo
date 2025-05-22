import axios from 'axios'
import { useAuthStore } from '@/stores/auth'

export default defineNuxtPlugin((nuxtApp) => {
  const config = useRuntimeConfig()
  const auth = useAuthStore()

  const instance = axios.create({
    baseURL: config.public.apiBase,
  })

  // ✅ Add access token before request
  instance.interceptors.request.use((request) => {
    auth.loadTokens()
    if (auth.accessToken) {
      request.headers.Authorization = `Bearer ${auth.accessToken}`
    }
    return request
  })

  // ✅ Handle token refresh on 401
  instance.interceptors.response.use(
    response => response,
    async error => {
      const originalRequest = error.config

      if (
        error.response?.status === 401 &&
        !originalRequest._retry &&
        auth.refreshToken
      ) {
        originalRequest._retry = true
        const refreshed = await auth.refreshAccessToken()
        if (refreshed) {
          originalRequest.headers.Authorization = `Bearer ${auth.accessToken}`
          return instance(originalRequest)
        } else {
          auth.clearTokens()
          const router = useRouter()
          router.push('/login')
        }
      }

      return Promise.reject(error)
    }
  )

  nuxtApp.provide('http', instance)
})
