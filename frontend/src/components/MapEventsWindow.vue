<template>
  <div class="flex w-full justify-center p-6 gap-4 duration-500 min-h-screen">
    <div class="fixed w-64 left-6">
      <SidebarMain />
    </div>
    <div
      class="ml-72 w-4/6 outline-dashed bg-frameBackground rounded-xl outline-[1px] outline-outlineColor duration-500">
      <div class="h-full px-2">
        <div class="relative h-full flex justify-center">
          <div class="absolute bottom-3 w-full flex items-center gap-2 justify-center px-2">
            <Map />
          </div>
        </div>
      </div>
    </div>
    <div class=" w-3/12 outline-dashed bg-frameBackground rounded-xl outline-[1px] outline-outlineColor duration-500">
      <div class="min-h-full p-3">
        <p class="text-activeText py-2 text-center rounded-xl mb-4 text-xl font-medium duration-500">
          Эфир событий
        </p>
        <input
          class="w-full rounded-xl h-10 border-[1.5px] bg-transparent px-4 text-activeText placeholder:text-unactiveText border-neutral-500 dark:border-neutral-200 duration-500"
          type="text" placeholder="Поиск событий" />
        <div class="w-full px-2 overflow-y-scroll h-[80vh] custom-scrollbar duration-500">
          <div v-for="i in 40" class="text-activeText pt-2 w-full duration-500">
            <div class="border-2 rounded-xl px-2 py-2 flex relative items-center hover:bg-hoverBackground duration-200">
              <div class="h-full ">

                <div class="flex justify-between text-red-600 uppercase text-bold">Повернутые на войне
                  <div class="flex text-end  text-blue-500 text-xs">17:25 17.03.2024 </div>
                </div>
                <BaseIcon name="chat" class="w-6 h-6 mt-1 absolute " />
                <p class="pl-7 text-xs h-full text-justify">
                  Lorem, ipsum dolor sit amet consectetur adipisicing elit.
                  Asperiores commodi excepturi aut quasi quo enim reprehenderit
                  vero, aperiam quibusdam possimus nostrum, repellat corrupti
                  laboriosam. Consectetur nisi eum eveniet quaerat. Mollitia!
                  Lorem ipsum dolor sit amet consectetur, adipisicing elit. Debitis similique quidem nisi placeat et
                  modi numquam, eligendi consequuntur itaque, vel, officiis totam praesentium dolore ratione accusantium
                  iste illo minima animi.
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import Map from "./Map.vue";
import BaseIcon from "./BaseIcon.vue";
import SidebarMain from "./SidebarMain.vue";
export default {
  components: {
    Map,
    BaseIcon,
    SidebarMain,
  },
  computed: {
    isDarkMode() {
      return this.$store.state.darkMode;
    },
  },
};
</script>
<style>
.rainbows {
  position: relative;
}

@keyframes rainbow {
  0% {
    color: white;
  }

  33% {
    color: blue;
  }

  66% {
    color: red;
  }

  100% {
    color: white;
  }
}

.owl {
  position: absolute;
  width: 40px;
  height: 40px;
  background-image: url("https://freesvg.org/img/1531730612.png");
  background-size: cover;
  animation: fly-around 5s ease-in-out infinite;
}

@keyframes fly-around {
  0% {
    left: 40px;
    top: 0px;
  }

  25% {
    left: 40px;
    top: 20px;
  }

  50% {
    left: 55px;
    top: 5px;
  }

  75% {
    left: 25;
    top: 15px;
  }

  100% {
    left: 40px;
    top: 0px;
  }
}

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
  background-color: #323232;
}
</style>
