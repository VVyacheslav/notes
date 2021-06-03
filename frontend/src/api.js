import Vue from "vue";
import Notes from "@/api/notes";
import axios from "axios";

Vue.prototype.$api = {
    notes: Notes(axios)
};
