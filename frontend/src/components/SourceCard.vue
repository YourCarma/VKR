<template>
    <div :class="`bg-${bg_color} max-w-xs rounded max-h-xs shadow-lg hover:bg-${bg_hover_color} duration-200 transition ease-in-out hover:-translate-y-1 hover:scale-103`">
        <img class="w-full"
        :src="getImage"
            alt="Sunset in the mountains">
        <div class="px-2 py-2 ">
            <div class="font-bold text-sm mb-2 font-roboto">{{ info.title }}</div>
            <div class="w-full flex-col">
                <div class="w-full flex items-center">
                    <BaseIcon :class="'text-white-100 w-6 h-6'" :name="'info'" />
                    <a :href="info.url" target="_about.blank" class="text-purple-700 text-center text-xs font-semibold font-roboto">Перейти на канал</a>
                </div>
                <div class="w-full flex items-center">
                    <BaseIcon :class="'text-white-100 w-6 h-6'" :name="'user'" />
                    <p class="text-slate-700 text-center text-xs font-semibold font-roboto">{{numberWithSpaces}} подписчиков</p>
                </div>

            </div>
            <p class="text-gray-700 text-xs text-left whitespace-pre-line break-words">
                {{ info.description }}
            </p>
        </div>

    </div>
</template>

<script>
import BaseIcon from './BaseIcon.vue'
export default {
    components:{
        BaseIcon
    },

    props: {
        info: Object,
        bg_color: String,
        bg_hover_color: String
    },
    computed:{
        getImage(){
            return `http://${process.env.VUE_APP_WARMONGER_IP}/downloads/${this.info.photo_profile_path}`
        },

        numberWithSpaces() {
    return this.info.members_count.toString().replace(/\B(?=(\d{3})+(?!\d))/g, " ");
}
    },
    data(){
        return {
            img_url: null
        }
    },
  methods: {
    
  }
}
</script>

<style></style>