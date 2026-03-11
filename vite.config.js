import { resolve } from 'path'
import { defineConfig } from 'vite'

export default defineConfig({
    base: '/',
    build: {
        rollupOptions: {
            input: {
                main: resolve(__dirname, 'index.html'),
                waterHeater: resolve(__dirname, 'water-heater-repair.html'),
                emergency: resolve(__dirname, 'emergency.html'),
                drainCleaning: resolve(__dirname, 'drain-cleaning.html'),
                tankless: resolve(__dirname, 'tankless.html'),
                about: resolve(__dirname, 'about.html'),
                contact: resolve(__dirname, 'contact.html'),
                shastaLake: resolve(__dirname, 'shasta-lake.html'),
                anderson: resolve(__dirname, 'anderson.html'),
                paloCedro: resolve(__dirname, 'palo-cedro.html'),
                bellaVista: resolve(__dirname, 'bella-vista.html')
            }
        }
    }
})
