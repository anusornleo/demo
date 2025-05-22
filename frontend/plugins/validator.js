// plugins/validator.js
export default defineNuxtPlugin(() => {
  const $rules = {
    required: v => !!v || 'This field is required.',

    email: v => {
      const pattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
      return !v || pattern.test(v) || 'Invalid email address.'
    },

    minlength: (min = 3) => v => {
      return !v || v.length >= min || `Minimum ${min} characters required.`
    },

    maxlength: (max = 255) => v => {
      return !v || v.length <= max || `Maximum ${max} characters allowed.`
    },

    sameAs: (value, message = 'Values do not match.') => v => {
      return v === value || message
    },

    numeric: v => {
      return !v || /^\d+$/.test(v) || 'Only numbers allowed.'
    },
  }

  return {
    provide: {
      rules: $rules
    }
  }
})
