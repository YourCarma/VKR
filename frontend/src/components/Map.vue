<template>
    <div class="border-idealBlue border-[6px] rounded-lg shadow-cards w-full h-full">
        <yandex-map :coords="coords" :use-object-manager="true" :object-manager-clusterize="true" :settings="settings"
            :zoom="5">

            <ymap-marker v-for="(item, index) in fromLife" :key="item.date" :balloon-template="balloonTemplate(item)"
                :markerId="index" :cluster-name="1"
                :coords="[item.named_entities.LOC[0].latitude, item.named_entities.LOC[0].longitude]"
                :clusterOptions="clusterOptions" :icon="markerIconLife" />

            <ymap-marker v-for="(item, index) in culture" :key="item.date" :balloon-template="balloonTemplate(item)"
                :markerId="index" :cluster-name="2"
                :coords="[item.named_entities.LOC[0].latitude, item.named_entities.LOC[0].longitude]"
                :clusterOptions="clusterOptions" :icon="markerIconCulture" />

            <ymap-marker v-for="(item, index) in science" :key="item.date" :balloon-template="balloonTemplate(item)"
                :markerId="index" :cluster-name="3"
                :coords="[item.named_entities.LOC[0].latitude, item.named_entities.LOC[0].longitude]"
                :clusterOptions="clusterOptions" :icon="markerIconScience" />

            <ymap-marker v-for="(item, index) in community" :key="item.date" :balloon-template="balloonTemplate(item)"
                :markerId="index" :cluster-name="4"
                :coords="[item.named_entities.LOC[0].latitude, item.named_entities.LOC[0].longitude]"
                :clusterOptions="clusterOptions" :icon="markerIconCommunity" />

            <ymap-marker v-for="(item, index) in politics" :key="item.date" :balloon-template="balloonTemplate(item)"
                :markerId="index" :cluster-name="5"
                :coords="[item.named_entities.LOC[0].latitude, item.named_entities.LOC[0].longitude]"
                :clusterOptions="clusterOptions" :icon="markerIconPolitic" />

            <ymap-marker v-for="(item, index) in zov" :key="item.date" :balloon-template="balloonTemplate(item)"
                :markerId="index" :cluster-name="6"
                :coords="[item.named_entities.LOC[0].latitude, item.named_entities.LOC[0].longitude]"
                :clusterOptions="clusterOptions" :icon="markerIconZov" />

            <ymap-marker v-for="(item, index) in judge" :key="item.date" :balloon-template="balloonTemplate(item)"
                :markerId="index" :cluster-name="7"
                :coords="[item.named_entities.LOC[0].latitude, item.named_entities.LOC[0].longitude]"
                :clusterOptions="clusterOptions" :icon="markerIconJudge" />

            <ymap-marker v-for="(item, index) in habitation" :key="item.date" :balloon-template="balloonTemplate(item)"
                :markerId="index" :cluster-name="8"
                :coords="[item.named_entities.LOC[0].latitude, item.named_entities.LOC[0].longitude]"
                :clusterOptions="clusterOptions" :icon="markerIconHabbitation" />


            <ymap-marker v-for="(item, index) in economic" :key="item.date" :balloon-template="balloonTemplate(item)"
                :markerId="index" :cluster-name="8"
                :coords="[item.named_entities.LOC[0].latitude, item.named_entities.LOC[0].longitude]"
                :clusterOptions="clusterOptions" :icon="markerIconEconomic" />

        </yandex-map>

    </div>
</template>

<script>
import { yandexMap, ymapMarker } from "vue-yandex-maps";

const settings = {
    apiKey: "9b855f9b-6853-4cb2-b2f8-f02951d693c4",
    lang: "ru_RU",
    coordorder: "latlong",
    enterprise: false,
    version: "2.1",
};

export default {
    components: { yandexMap, ymapMarker },

    props: {
        event_news: Array
    },

    computed: {
        fromLife() {
            return this.testEvent.filter((event) => event.class == 'Из жизни')
        },

        culture() {
            return this.testEvent.filter((event) => event.class == 'Культура')
        },

        science() {
            return this.testEvent.filter((event) => event.class == 'Наука и техника')
        },

        community() {
            return this.testEvent.filter((event) => event.class == 'Общество')
        },

        politics() {
            return this.testEvent.filter((event) => event.class == 'Политика')
        },

        zov() {
            return this.testEvent.filter((event) => event.class == 'СВО/Украина')
        },

        judge() {
            return this.testEvent.filter((event) => event.class == 'Следствие и суд')
        },

        habitation() {
            return this.testEvent.filter((event) => event.class == 'Среда обитания')
        },

        economic() {
            return this.testEvent.filter((event) => event.class == 'Экономика')
        },

        testEvent() {
            return this.eventsWithLocs
        },

        eventsWithLocs() {

            let map_events = this.event_news.map(x => ({ ...x }))
            map_events.forEach(element => {
                if (element.named_entities.LOC.length == 0) {
                    map_events.splice(map_events.indexOf(element), 1).map(x => ({ ...x }))
                }

            });

            return map_events
        }

    },

    data() {
        return {
            coords: [55.753215, 36.622504],
            settings: settings,
            raw_events: null,
            clusterOptions: {
                clusterOptions: {
                    1: {
                        clusterDisableClickZoom: false,
                        clusterOpenBalloonOnClick: true,
                        clusterBalloonLayout: [
                            '<ul class=list>',
                            '{% for geoObject in properties.geoObjects %}',
                            '<li><a href=# class="list_item">{{ geoObject.properties.balloonContentHeader|raw }}</a></li>',
                            '{% endfor %}',
                            '</ul>',
                        ].join('')

                    },
                },
            },

            markerIconLife: {
                layout: "default#imageWithContent",
                imageHref: "https://cdn-icons-png.flaticon.com/128/2751/2751758.png",
                imageSize: [40, 40],
                imageOffset: [-20, -20],
                contentOffset: [0, 0],
            },
            markerIconCulture: {
                layout: "default#imageWithContent",
                imageHref: "https://cdn-icons-png.flaticon.com/128/647/647740.png",
                imageSize: [43, 43],
                imageOffset: [0, 0],
                contentOffset: [0, 15],
            },
            markerIconZov: {
                layout: "default#imageWithContent",
                imageHref: "https://cdn-icons-png.flaticon.com/128/3097/3097122.png",
                imageSize: [43, 43],
                imageOffset: [0, 0],
                contentOffset: [0, 15],
            },
            markerIconEconomic: {
                layout: "default#imageWithContent",
                imageHref: "https://cdn-icons-png.flaticon.com/128/1490/1490839.png",
                imageSize: [43, 43],
                imageOffset: [0, 0],
                contentOffset: [0, 15],
            },
            markerIconScience: {
                layout: "default#imageWithContent",
                imageHref: "https://cdn-icons-png.flaticon.com/128/5408/5408783.png",
                imageSize: [43, 43],
                imageOffset: [0, 0],
                contentOffset: [0, 15],
            },
            markerIconCommunity: {
                layout: "default#imageWithContent",
                imageHref: "https://cdn-icons-png.flaticon.com/128/3985/3985098.png",
                imageSize: [43, 43],
                imageOffset: [0, 0],
                contentOffset: [0, 15],
            },
            markerIconJudge: {
                layout: "default#imageWithContent",
                imageHref: "https://cdn-icons-png.flaticon.com/128/3122/3122246.png",
                imageSize: [43, 43],
                imageOffset: [0, 0],
                contentOffset: [0, 30],
            },
            markerIconHabbitation: {
                layout: "default#imageWithContent",
                imageHref: "https://cdn-icons-png.flaticon.com/128/4078/4078446.png",
                imageSize: [43, 43],
                imageOffset: [0, 0],
                contentOffset: [0, 15],
            },
            markerIconPolitic: {
                layout: "default#imageWithContent",
                imageHref: "https://cdn-icons-png.flaticon.com/128/4508/4508978.png",
                imageSize: [43, 43],
                imageOffset: [0, 0],
                contentOffset: [15, 15],
            },

        }
    },
    methods: {

    dataFromatter(data) {
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
    balloonTemplate(item) {
        return `
            <div class=>
                <div class="w-full">
                    <p class="text-lg w-full uppercase font-bold font-rale text-red-600">${item.title}</p>
                    <p class="text-md w-full uppercase font-bold font-rale text-purple-600 border-dotted border-2 
                    border-indigo-600 text-center py-2 bg-purple-100 duration-200 hover:bg-purple-300">${item.class}</p>
                    <hr class="bg-gray-600 border-1 dark:bg-gray-700" />
                </div>
                <div class="flex flex-col h-full items-center">
                    <div class="bg-blue-100 text-center  flex flex-row border-dotted border-2 border-indigo-600 w-full justify-center">
                        <div class="text-xs font-rale font-bold px-1 mx-1">Локации:
                            ${item.named_entities.LOC
                .map((el) => `<li class="whitespace-pre-line break-words text-left px-1 mx-1">${el.text}</li>`)
                .join("")}
                                </div>
                        <div class="text-xs font-rale font-bold px-1 mx-1">Персоны:
                            ${item.named_entities.PER
                .map((el) => `<li class="whitespace-pre-line break-words text-left px-1 mx-1">${el.text}</li>`)
                .join("")}
                            </div>
                        <div class="text-xs font-rale font-bold px-1 mx-1">Организации:
                            ${item.named_entities.ORG
                .map((el) => `<li class="whitespace-pre-line break-words text-left px-1 mx-1">${el.text}</li>`)
                .join("")}
                            </div>
                    </div>
                    <div class="w-full">
                        <p class="text-left text-xs whitespace-pre-line break-words font-montserrat">${item.text}</p>
                    </div>
                </div>
                <hr class="bg-gray-600 border-1 dark:bg-gray-700" />
                <p class="text-end w-full font-bold text-zink-600 text-xs font-roboto">${this.dataFromatter(item.date)}</p>
            </div>
            `;
    },
    eventsWithLocsMeth() {
        let map_events = this.event_news.map(x => ({ ...x }))
        map_events.forEach(element => {
            if (element.named_entities.LOC[0].latitude == undefined) {
                console.log(element)
            }
            if (element.named_entities.LOC.length == 0 || element.named_entities.LOC[0].latitude == undefined) {
                map_events.splice(map_events.indexOf(element), 1).map(x => ({ ...x }))
            }
        });
        return map_events
    }


}
}
</script>

<style>
.red {
    color: red;
}

.ymap-container {
    width: 100%;
    height: 90vh;
}

.ballon_header {
    font-size: 16px;
    margin-top: 0;
    margin-bottom: 10px;
    color: #708090;
}

.ballon_body {
    font-size: 14px;
    text-align: center;
}

.ballon_footer {
    font-size: 12px;
    text-align: right;
    border-top: 1px solid #7d7d7d;
    color: #7d7d7d;
    margin-top: 10px;
}

.description {
    display: block;
    color: #999;
    font-size: 10px;
    line-height: 17px;
}
</style>