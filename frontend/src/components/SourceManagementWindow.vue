<template>
  <div class="flex w-full justify-center p-6 gap-4 duration-500">
    <div class="fixed w-64 flex-col left-6 z-50">
      <SidebarMain />
    </div>
    <div
      class="flex flex-col min-h-[95vh] duration-500 justify-center ml-72 items-center w-9/12 bg-frameBackground rounded-xl outline-dashed outline-[1px] outline-outlineColor"
    >
      <LoaderBig v-if="isLoading" class="" />

      <div v-else-if="isError" class="flex justify-center">
        <ErrorPage :status="error_info.code" :text="error_info.message" />
      </div>
      <div v-else class="w-full justify-center">
        <div class="mx-2 mb-4 pt-2">
          <p
            class="text-center text-4xl font-black font-mono text-activeText duration-500"
          >
            Управление источниками
          </p>
        </div>
        <div class="w-full px-24">
          <div class="text-activeText flex items-center justify-start">
            <div>
              <div class="w-full flex items-center p-2 h-12">
                Количеcтво источников:
              </div>
            </div>
            <div
              class="w-36 h-12 bg-red-500 rounded-full flex items-center justify-center flex-col hover:bg-red-700 duration-200 ml-2"
            >
              <span class="text-white text-xs font-bold">Пророссийских </span>
              <span class="text-white text-lg font-bold">105</span>
            </div>
            <div
              class="w-36 h-12 bg-blue-500 rounded-full flex items-center justify-center flex-col hover:bg-blue-700 duration-200 ml-2 "
            >
              <span class="text-white text-xs font-bold">Иных</span>
              <span class="text-white text-lg font-bold">30</span>
            </div>
            <div 
              class="static w-60 h-12 bg-green-500 rounded-t-xl ml-96 flex jusify-end flex-col hover:bg-green-700 duration-200 "
            >
              <div  @click="openAddSource" class="cursor-pointer w-full h-full flex items-center justify-center">
                <button  class="text-white text-xl font-bold">Добавить</button>
              </div>
              <div v-if="addSourceIsOpen" class="absolute mt-12 ">
                <AddSource />
              </div>
            </div>
          </div>
          <div
            class="w-full mt-2 px-2 outline-dashed outline-[3px] outline-outlineColor flex justify-center overflow-y-auto custom-scrollbar  h-full"
          >
            <div
              class="text-activeText w-50 grid grid-cols-3 gap-3 mr-2 max-h-[80vh]"
            >
              <SourceCard class="my-2" :bg_hover_color="'red-500'" :bg_color="'red-400'" v-for="el in 30" />
            </div>
            <div
              class="outline-dashed outline-[1px] outline-outlineColor"
            ></div>
            <div
              class="text-activeText w-50 grid grid-cols-3 gap-3 ml-2 max-h-[80vh]"
            >
              <SourceCard
                class="my-2"
                :bg_color="'blue-400'"
                :bg_hover_color="'blue-500'"
                v-for="el in 10"
              />
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import SmallLoader from "./SmallLoader.vue";
import FormsFile from "./FormsFile.vue";
import BaseIcon from "./BaseIcon.vue";
import ErrorPage from "@/components/ErrorPage.vue";
import SidebarMain from "@/components/SidebarMain.vue";
import LoaderBig from "./LoaderBig.vue";
import SourceCard from "./SourceCard.vue";
import AddSource from "./AddSource.vue";
export default {
  components: {
    BaseIcon,
    SmallLoader,
    FormsFile,
    ErrorPage,
    SidebarMain,
    LoaderBig,
    SourceCard,
    AddSource,
  },
  data() {
    return {
      addSourceIsOpen: false,
    };
  },
  methods: {
    openAddSource(){
      this.addSourceIsOpen = this.addSourceIsOpen == false ? true : false
    }
  },
  computed:{
    openAdd(){
      return this.addSourceIsOpen
    }
  }
};
</script>

<style scoped>
.custom-scrollbar {
  scrollbar-width: thin;
  scrollbar-color: #535353 #272727;
}

.custom-scrollbar::-webkit-scrollbar {
  width: 5px;
}

.custom-scrollbar::-webkit-scrollbar-track {
  background: #27272700;
}

.custom-scrollbar::-webkit-scrollbar-thumb {
  background-color: #535353;
  border-radius: 12px;
}

.custom-scrollbar::-webkit-scrollbar-thumb:hover {
  background-color: #858585;
}
</style>
