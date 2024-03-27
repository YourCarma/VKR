<template>
    <div :class="`bg-${bg_color} max-w-xs rounded max-h-xs shadow-lg hover:bg-${bg_hover_color} duration-200`">
        <img class="w-full"
        :src="imageUrl"
            alt="Sunset in the mountains">
        <div class="px-2 py-2 ">
            <div class="font-bold text-sm mb-2 font-roboto">{{ info.title }}</div>
            <div class="w-full flex-col">
                <div class="w-full flex items-center">
                    <BaseIcon :class="'text-white-100 w-6 h-6'" :name="'info'" />
                    <a class="text-purple-700 text-center text-xs font-semibold font-roboto">{{ info.url }}</a>
                </div>
                <div class="w-full flex items-center">
                    <BaseIcon :class="'text-white-100 w-6 h-6'" :name="'user'" />
                    <p class="text-slate-700 text-center text-xs font-semibold font-roboto">{{info.members_count}} подписчиков</p>
                </div>

            </div>
            <p class="text-gray-700 text-xs">
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

    data(){
        return {
            img_url: null
        }
    },


    mounted() {
    this.getImage();
  },
  methods: {
    async getImage() {
      try {
        const response = await fetch('http://localhost:8000/backend/downloads/boris_rozhin_profile_photo.jpg');
        if (!response.ok) {
          throw new Error('Failed to load image');
        }
        const blob = await response.blob();
        const imageUrl = URL.createObjectURL(blob);
        this.imageUrl = imageUrl;
      } catch (error) {
        console.error('Error loading image:', error);
      }
    }
  }
}
</script>

<style></style>