<template>
  <div class="flex w-full justify-center p-6 gap-4 duration-500">
    <div class="fixed w-64 left-6 z-50">
      <SidebarMain />
    </div>
    <div
      class="flex flex-col min-h-[95vh] duration-500 justify-center ml-72 items-center w-full bg-frameBackground rounded-xl outline-dashed outline-[1px] outline-outlineColor"
    >
      <LoaderBig v-if="isLoading" class=""/>
      
      <div v-else-if="isError" class="flex justify-center">
        <ErrorPage :status="error_info.code" :text="error_info.message" />
      </div>
      <div v-else class="w-full mx-24 flex flex-col justify-center mb-10">
        <div class="flex justify-center mb-4 pt-2">
          <p
            class="text-center text-4xl font-black font-mono text-activeText duration-500"
          >
            Управление источниками
          </p>
        </div>
        <div class="w-full mx-24  text-activeText flex justify-between"> 
          <div> 
            <div class="w-full outline-dashed outline-[3px] p-2 outline-outlineColor">
              Количетсво источников:
            </div>
          </div>
          <div class="w-full">
              wafwaf
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
import debounce from "lodash/debounce";
import BaseIcon from "./BaseIcon.vue";
import ErrorPage from "@/components/ErrorPage.vue";
import SidebarMain from "@/components/SidebarMain.vue";
import LoaderBig from "./LoaderBig.vue";

export default {
  components: {
    BaseIcon,
    SmallLoader,
    FormsFile,
    ErrorPage,
    SidebarMain,
    LoaderBig,
  },
  data() {
    return {
      origin_language: "Русский",
      target_language: "Английский",
      origin_message: "",
      target_message: "",
      isLoading: false,
      isError: false,
      isTyping: false,
      textisProcessing: false,
      error_info: "",
      origin_languages: [],
    };
  },
  methods: {
    swap_language() {
      this.origin_language = [
        this.target_language,
        (this.target_language = this.origin_language),
      ][0];
      this.origin_message = [
        this.target_message,
        (this.target_message = this.origin_message),
      ][0];
    },
    delete_text() {
      this.origin_message = "";
      this.target_message = "";
    },
    copy_origin_text() {
      this.$refs.myinput.focus();
      document.execCommand("copy");
    },
    copy_target_text() {
      this.$refs.myoutput.focus();
      document.execCommand("copy");
    },

    debounceStopTyping: debounce(function () {
      this.isTyping = false;
    }, 500),

    text_processing() {
      this.isError = false;
      this.isTyping = true;
      this.textisProcessing = true;
      this.debounceStopTyping();
      setTimeout(() => {
        if (this.isTyping == false) {
          axios
            .post(
              `http://${process.env.VUE_APP_TRANSLATE_SERVICE_IP}/translator/translateText/`,
              {
                origin: this.choose_origin_iso639_1,
                target: this.choose_source_iso639_1,
                message: this.origin_message,
              }
            )
            .then((response) => {
              this.target_message = response.data;
              this.textisProcessing = false;
            })
            .catch(function () {
              console.log("Ошибка в обработке");
              this.textisProcessing = false;
              this.isError = true;
            });
        }
      }, 500);
    },
  },
  computed: {
    make_target_languages() {
      try {
        let target_values = this.origin_languages.find(
          (language) => language.name == this.origin_language
        );
        console.log(target_values);
        return target_values.targets;
      } catch (err) {
        console.log(err);
      }
    },
    choose_origin_iso639_1() {
      return this.origin_languages.find(
        (language) => language.name == this.origin_language
      ).iso;
    },
    choose_source_iso639_1() {
      return this.make_target_languages.find(
        (language) => language.name == this.target_language
      ).iso;
    },
    isDarkMode() {
      return this.$store.state.darkMode;
    },
  },
  created() {
    // this.isLoading = true;
    // axios
    //   .get(
    //     `http://${process.env.VUE_APP_TRANSLATE_SERVICE_IP}/translator/modelGarden`
    //   )
    //   .then((response) => {
    //     this.origin_languages = response.data.languages;
    //     console.log(this.origin_languages);
    //     this.isLoading = false;
    //   })
    //   .catch((response) => {
    //     this.isLoading = false;
    //     this.isError = true;
    //     console.log(response);
    //     this.error_info = response;
    //   });
  },
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
  background-color: #323232;
}
</style>
