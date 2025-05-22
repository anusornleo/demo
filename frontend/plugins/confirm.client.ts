import { useDialogStore } from '@/stores/dialog'

export default defineNuxtPlugin(() => {
  const $confirm = (message: string, title?: string): Promise<boolean> => {
    const dialog = useDialogStore()
    return dialog.confirm(message, title)
  }

  return {
    provide: {
      confirm: $confirm,
    }
  }
})
