import { defineStore } from 'pinia'

export const useDialogStore = defineStore('dialog', {
  state: () => ({
    show: false,
    title: '',
    message: '',
    resolve: null as null | ((confirmed: boolean) => void),
  }),
  actions: {
    confirm(message: string, title = 'ยืนยันการทำรายการ') {
      this.message = message
      this.title = title
      this.show = true
      return new Promise<boolean>((resolve) => {
        this.resolve = resolve
      })
    },
    resolveDialog(result: boolean) {
      this.show = false
      this.resolve?.(result)
      this.resolve = null
    }
  }
})
