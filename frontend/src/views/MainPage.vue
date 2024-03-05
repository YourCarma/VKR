<template>
  <div class="bg-background bg-whitesmoke duration-500">
    <div class="pb-4">
      <Header />
      <div class="">
        <div class="grid grid-cols-4 gap-2.5 px-4">
          <Card
            v-for="card in datacard"
            :key="card"
            :title="card.name"
            :subtitle="card.subtitle"
            :url="card.url"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Sova from '@/components/Sova.vue'
import Header from '@/components/Header.vue'
import Card from '@/components/Card.vue'
export default {
  data () {
    return {
      datacard: [
        {
          name: 'Переводчик',
          subtitle:
            'Возможность перевода с иностранных языков на русский и наоборот',
          url:"/translater"
        },
        {
          name: 'Распознавание текста',
          subtitle: 'Возможность распознать текст с картинки',
          url:"/scan_from_docs"
        },
        {
          name: 'Ассистент',
          subtitle: 'Информационный справочник',
          url:"/"
        },
        {
          name: 'Поиск документов',
          subtitle:
            'Возможность найти определенный документ из общей базы данных документов',
            url:"/search_document"
        },
        {
          name: 'Распознавание аудио',
          subtitle: 'Преобразование голосовой речи в текстовый формат',
          url:"/audio_recognition"
        },
        {
          name: 'Преобразование текста в аудио',
          subtitle: 'Преобразование текста в аудио',
          url:"/text_to_audio"
        },
        {
          name: 'Распознавание на изображении',
          subtitle: 'Возможность узнать что за объект на фотографии',
          url:"/image_recognition"
        },
        {
          name: 'Формирование документов',
          subtitle: 'хз',
          url:"/"
        }
      ]
    }
  },
  components: {
    Sova,
    Card,
    Header
  }
}
</script>

<style></style>
