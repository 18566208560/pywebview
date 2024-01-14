import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],

  //打包配置
  build: {
    //指定输出路径
    outDir: "../public",
  }
})
