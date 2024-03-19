<template>
  <div class="bg-slate-200 px-2 py-2 rounded-b">
    <label
      for="small-input"
      class="block mb-2 text-sm font-bold text-gray-900 font-roboto"
      >Ссылка</label
    >
    <input
      type="text"
      id="small-input"
      class="block w-full p-2 text-gray-900 border border-gray-300 rounded-lg bg-gray-50 text-xs focus:ring-blue-500 focus:border-blue-500 "
    />
    <label for="countries" class="block mb-2 text-sm font-bold font-roboto text-gray-900 mt-2">Взгляды</label>
  <select id="countries" class="text-gray-900 bg-gray-50 border text-center border-gray-300  font-bold text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5">
    <option selected disabled>Выберите направленность</option>
    <option >Пророссийский</option>
    <option >Иной</option>
  </select>
  <button class="h-full w-full flex items-center  mt-2 text-center justify-center  text-white font-roboto font-bold bg-green-500 hover:bg-green-700 duration-200">
    Добавить
  </button>
  </div>
</template>

<script>
import BaseIcon from './BaseIcon.vue';
export default {
    components:{
        BaseIcon
    }
};
</script>

<style></style>
