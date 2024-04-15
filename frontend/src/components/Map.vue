<template>
    <div class="border-idealBlue border-[6px] rounded-lg shadow-cards w-full h-full">
        <yandex-map :coords="coords" :use-object-manager="true" :object-manager-clusterize="true" :settings="settings"
            :zoom="5">
            <ymap-marker v-for="(item, index) in testEvent" :key="index" :balloon-template="balloonTemplate(item)"
                :markerId="index" :cluster-name="1"
                :coords="[item.named_entities.LOC[0].latitude, item.named_entities.LOC[0].longitude]" />
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
        testEvent() {
            return this.eventsWithLocs
        },

        eventsWithLocs() {
            let map_events = this.event_news.map(x => ({ ...x }))
            console.log(map_events)
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
        };
    },

    methods: {
        balloonTemplate(item) {
            return `
            <div class=>
                <div class="w-full">
                    <p class="text-lg w-full uppercase font-bold font-rale text-red-600">${item.title }</p>
                    <p class="text-md w-full uppercase font-bold font-rale text-purple-600 border-dotted border-2 
                    border-indigo-600 text-center py-2 bg-purple-100 duration-200 hover:bg-purple-300">${item.class }</p>
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
                <p class="text-end w-full font-bold text-zink-600 text-xs font-roboto">${item.date }</p>
            </div>

      
    `;
        },
    },

};
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