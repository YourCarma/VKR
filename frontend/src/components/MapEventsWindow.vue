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
            <Map :event_news="dynamicNews" />
          </div>
        </div>
      </div>
    </div>
    <div class=" w-3/12 outline-dashed bg-frameBackground rounded-xl outline-[1px] outline-outlineColor duration-500">
      <div class="min-h-full p-3">
        <p class="text-activeText py-2 text-center rounded-xl mb-4 text-xl font-medium duration-500">
          Эфир событий
        </p>
        <div class="mb-2">
          <Toogle @change="openChanel()" :label="'Включить эфир'" v-model:checked="isMonitoring" />
        </div>
        <input
          class="w-full rounded-sm h-10 border-[0.1px] bg-transparent px-4 text-activeText placeholder:text-unactiveText border-neutral-500 dark:border-neutral-200 duration-500"
          type="text" placeholder="Поиск событий" />
        <div class="w-full overflow-y-scroll h-[80vh] custom-scrollbar duration-500">
          <div v-for="event in dynamicNews" :key="event.id" class="text-activeText pt-2 w-full duration-500 ">
            <div class=" px-2 py-2 flex relative items-center hover:bg-slate-300 dark:hover:bg-stone-700  duration-300 transition ease-in-out hover:-translate-y-1 hover:scale-103 bg-slate-200 shadow-xl  outline-dashed dark:bg-background outline-[1.5px] outline-outlineColor ">
              <div class="h-full w-full">
                <div class="flex justify-between text-red-600 uppercase font-bold text-xs font-rale">{{ event.title }}
                </div>
                <p class="text-xs h-full  text-left whitespace-pre-line break-words font-rale">
                  {{ event.text }}
                </p>
                <div class="text-start dark:text-purple-400 text-purple-600 text-xs font-roboto font-bold">{{ event.class }}</div>
                <div class="text-end dark:text-orange-400 text-zink-600 text-xs font-roboto font-bold">{{ dataFromatter(event.date) }}</div>

              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import axios from "axios";
import Map from "./Map.vue";
import Toogle from "./Toogle.vue";
import BaseIcon from "./BaseIcon.vue";
import SidebarMain from "./SidebarMain.vue";
export default {
  components: {
    Map,
    BaseIcon,
    SidebarMain,
    Toogle
  },

  data(){
    return {
      news: [],
      isMonitoring: null,
      isError: false,
      isLoading: false,
    }
  },

  computed: {
    isDarkMode() {
      return this.$store.state.darkMode;
    },

    
    
    dynamicNews(){
      return this.news
    }
  },

  created(){
    axios.get(`http://${process.env.VUE_APP_WARMONGER_IP }/collecting/get_news`)
    .then((response) => {
      this.news = response.data
      console.log(this.news)
    })
  },

    methods:{
      openChanel(){
        if (this.isMonitoring)
          {
            console.log("Мониторинг")
            this.connection.send("True")
          }
        else
        {
          console.log("Отмена")
        }
  },
  dataFromatter(data){
      let date = new Date(data);

      // Получаем день, месяц, год, часы, минуты и секунды
      let day = date.getDate();
      let month = date.getMonth() + 1; // Месяцы начинаются с 0, поэтому добавляем 1
      let year = date.getFullYear();
      let hours = date.getHours();
      let minutes = date.getMinutes();
      let seconds = date.getSeconds();

      // Форматируем день, месяц, часы, минуты и секунды, чтобы они были двузначными, если меньше 10
      day = day < 10 ? "0" + day : day;
      month = month < 10 ? "0" + month : month;
      hours = hours < 10 ? "0" + hours : hours;
      minutes = minutes < 10 ? "0" + minutes : minutes;
      seconds = seconds < 10 ? "0" + seconds : seconds;

      // Создаем строку в формате "день.месяц.год часы:минуты:секунды"
      let formattedDate = hours + ":" + minutes + ":" + seconds + " " + day + "." + month + "." + year
      return formattedDate
    },
    },
  
  mounted() {
    this.connection = new WebSocket(
      `ws://${process.env.VUE_APP_WARMONGER_IP }/collecting/ws`
    );
   
    // setTimeout(() => {
    //   this.isError = false;
    //   this.isReady = false;
    // }, 4000);

    this.connection.onopen = () => {
      console.log("Соединение мониторинга сообщений установлено!");
      this.isLoading = false;
      this.isReady = true;
    };
   

    
    this.connection.onmessage = (event) => {
      console.log(event.data)
      this.dynamicNews.unshift(JSON.parse(event.data))
    };
   

    this.connection.onclose = (event) => {
      console.log(this);
      this.isError = true;
      this.isLoading = false;
    };

    this.connection.onerror = (error) => {
      console.log(this);
      this.isError = true;
      this.isLoading = false;
    };
    
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
