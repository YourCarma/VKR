<template>
    <div :class="`bg-${bg_color} max-w-xs rounded max-h-xs shadow-lg`">
        <img class="w-full"
            src="https://sun6-21.userapi.com/s/v1/ig2/NzeRweKn932nP043_plx1DWS5rQK9-hk9KOo1m5zfaP6C51WlHDjtEpG4qzlP1SBxevASPZedzd3FkOOidNviuZF.jpg?size=1077x1077&quality=96&crop=1,1,1077,1077&ava=1"
            alt="Sunset in the mountains">
        <div class="px-2 py-2 ">
            <div class="font-bold text-sm mb-2 font-roboto">Повернутые на войне</div>
            <div class="w-full flex-col">
                <div class="w-full flex items-center">
                    <BaseIcon :class="'text-white-100 w-6 h-6'" :name="'info'" />
                    <a class="text-purple-700 text-center text-xs font-semibold font-roboto">https://t.me/voenacher</a>
                </div>
                <div class="w-full flex items-center">
                    <BaseIcon :class="'text-white-100 w-6 h-6'" :name="'user'" />
                    <p class="text-slate-700 text-center text-xs font-semibold font-roboto">1 245 523 подписчиков</p>
                </div>

            </div>
            <p class="text-gray-700 text-xs">
                Предложка и вопросы: @voenacher_zov_bot

                По вопросам рекламы: @VoenacherAdvert_bot

                @pnv_dozor_bot - передай информацию о ВРАГЕ!
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
        bg_color: String
    }
}
</script>

<style></style>